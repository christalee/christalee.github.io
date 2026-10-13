title: Deploying WeLC
tags: javascript, python, programming

On and off for the past few months, I've been building a simple audio player app, with the goal of making our music library accessible from our phones, outside the home - the music itself lives on our home server. I'm calling the project WeLC, a play on VLC, the gold standard program in this domain. (Why not just use VLC? I'm trying to learn by putting concepts into practice, specifically backend API design and system design.) The repo is [here](https://github.com/christalee/welc).

It's reached the point where users can start pressure-testing it, so I decided to deploy it onto the server with the music. (The program is locked down to only be able to access files in a local directory specified by an environment variable, to prevent malicious users from sniffing the filesystem.) The frontend is a React/TypeScript app using [Vite](https://vite.dev/), talking to a [Flask](https://flask.palletsprojects.com/en/stable/) backend and a [Postgres](https://www.postgresql.org/) database. The server is running Ubuntu Desktop 26.04, using [Caddy](https://caddyserver.com/) as a reverse proxy for the backend and a static file server for the frontend, and [Tailscale](https://tailscale.com/) to permit access from authorized machines. This post doesn't cover the Tailscale setup, as that was done previously and didn't need to change. Here's what needed to happen with the rest of it.

1. Clone the repo into your projects folder (or the location of your choice), creating `/home/projects/welc`. 

2. cd into `/home/projects/welc/api` and create a venv (currently on Python 3.14), activate it, then install the backend from the `requirements.txt` file.

3. Postgres is already running (to provide DBs for other projects), so create a user `welc` with a password and create a database `welc` owned by user `welc` (`createdb welc -O welc`).

4. In the project folder, create a file `.env.production` to hold program-specific env vars. The DB name, username, and password all go in there (see the README for details on what else needs to be populated).

5. From inside the venv, run `alembic --name production upgrade head` to create all the necessary DB tables. Optionally, use `psql` to check your work.

6. Create a production frontend build by running `npm run release`, which specifies a base prefix for all paths. This should match whatever path you're expecting to serve your static assets from. In this case, `/welc` as the base allows the static files to be served from `$SERVER_NAME.$TAILSCALE_NAME.ts.net/welc`.

7. You need to add two sections to your `Caddyfile` (if it already exists - if not, create one and an associated systemd service):

        $SERVER_NAME.$TAILSCALE_NAME.ts.net {

          ...

          handle /welc/api/* {
            uri strip_prefix /welc
            reverse_proxy localhost:$PORT
          }

          ...

          file_server
          root /path/to/root
        }

    The first section tells Caddy how to reverse-proxy requests to the backend. You should specify a port where [gunicorn](https://gunicorn.org/) will be running in step 9. The second (which may already exist) will clarify where you need to move the files in the next step.

8. The frontend build output should be in the project folder under `/dist`. Move the contents from there to wherever Caddy will look for it (in our case, `/path/to/root/welc` next to other project static sites.)

9. From inside the venv, run gunicorn manually just to make sure everything is hooked together properly: `PORT=$PORT gunicorn app:app -w 4`

10. Visit WeLC on the web at `$SERVER_NAME.TAILSCALE_NAME.ts.net/welc` and verify that you can play files from both tabs. If not, troubleshoot via system logs and the browser Dev Tools.

11. Shut down gunicorn and set up a systemd `welc.service`[^1] to run it automatically. I ended up with something like this[^2]:

        [Unit]
        Description=gunicorn daemon for welc
        After=network.target

        [Service]
        Type=notify
        NotifyAccess=main
        User=$SERVER_USER
        Group=$SERVER_GROUP
        WorkingDirectory=/path/to/projects/welc/api
        EnvironmentFile=/path/to/projects/welc/.env.production
        Environment="PORT=$PORT"
        ExecStart=/path/to/projects/welc/api/.venv/bin/gunicorn --workers 3 app:app
        ExecReload=/bin/kill -s HUP $MAINPID
        KillMode=mixed
        TimeoutStopSec=5
        Restart=always
        PrivateTmp=true

        [Install]
        WantedBy=multi-user.target

    Update User, Group, and PORT with the correct values, and replace the paths with your system's paths. 

12. Reload everything with `systemctl daemon-reload`, then start the service with `systemctl start welc`. Set it to start on boot with `systemctl enable welc`. Check that all is going well with `systemctl status welc`. Go back to the web and verify that everything is working as expected.

That's a lot, and it's pretty attuned to our specific setup, but I wanted to document it for myself, if nothing else. Along the way I discovered some bugs and potential enhancements that I should work on next. I also plan to collect the above process into a script that I can run every time I want to deploy a new version of the program.

[^1]: On our machine, user-created service files are kept under version control and symlinked into `/etc/systemd/system`.

[^2]: I found the [official systemd site](https://systemd.io/) extremely useless and preferred looking up settings [here](https://www.freedesktop.org/software/systemd/man/latest/systemd.directives.html).