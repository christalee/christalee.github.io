title: building a digital breadboard
tags: javascript, programming
img: react_breadboard.png
caption: A simple circuit on my breadboard-simulation frontend.

Earlier this year I was laid off from my job. As I wandered through a morass of job listings and LeetCode, I wanted to write something that demonstrated my React skills more extensively than my rc-niceties portfolio project. I also wanted an excuse to try out Typescript, as I had only previously worked with prop-types. I cast around for some idea that would spark joy, and landed on literal sparks: I would build a digital breadboard that would tell you if the light(s) turn on when you flip the switch.

As this was meant to be a React showpiece, I started with the front end. I roughed out a grid of squares and their click handlers, then turned my attention to the actual components. Initially I drew the grid as `divs` and the circuit elements as `svgs` in a separate layer, but this quickly caused problems: clicks only registered on the front-most component. So I refactored to render everything as an SVG in a parent SVG. Then I added tooltips (anticipating the eventual need to display the voltage and current for each component); a basic control panel for the voltage, grid size, and circuit element selectors; and minimal styling, based on [this blue-gray palette](https://palettes.shecodes.io/palettes/1448#palette). 

With the front-end coming along nicely enough, I turned my attention to the actual circuit solving code. This turned out to be a huge can of worms - I was hoping for a straightforward package I could install and use from a basic backend, ideally Node or Flask... but instead I found a bunch of options, none of which I could figure out how to get working in my environment. I settled pretty early on for not trying to reinvent the wheel, which meant coordinating my input/output format with that of SPICE, the Berkeley Simulation Program with Integrated Circuit Emphasis. I found at least two different Python packages purporting to work with netlists, [PySpice](https://github.com/PySpice-org/PySpice) and [SpicePy](https://github.com/giaccone/SpicePy), but I couldn't get them working. 

I also considered writing my own circuit solver, inspired by / borrowing from existing implementations. This seemed like overkill, however, and like my project would join the graveyard of barely-documented projects I'd already found. Of particular concern was that I wanted to work with LEDs, not regular R lights, which have a nonlinear response curve and would be hard to incorporate into a basic analysis. Ultimately, I put this project down, with the intent to come back to it sometime when I was relishing an intellectual challenge, possibly with a collaborator who could guide me through the pitfalls of modeling physical systems with code. I feel successful in my first foray into Typescript, even if the project is stalled. In the meantime, the project is [here on GitHub](https://github.com/christalee/react-breadboard).

Some additional resources, for the next time I pick this project up:

* [dan-fritchman's Spice21 (Rust, library)](https://github.com/dan-fritchman/Spice21)
* [gatecat's BreadboardSim (C++, project)](https://github.com/gatecat/BreadboardSim)
* [hlorenzi's circuitsim (JS, project)](https://github.com/hlorenzi/circuitsim/tree/master)
* [pfalstad's circuitjs (Java, project)](https://github.com/pfalstad/circuitjs1/tree/master)
* [danchitnis' EEsim (JS, project)](https://github.com/danchitnis/EEsim/tree/main)