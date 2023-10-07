title: my first pull request
tags: programming

Someone linked me to [Compute Cuter](https://computecuter.com/), a set of suggestions for cuter text editor themes, fonts, even keyboards and keycaps. The site is by [sailorhg](https://twitter.com/sailorhg), who makes the [fairyfloss](https://sailorhg.github.io/fairyfloss/) theme I sometimes use. Looking through the suggestions, I was rather taken with the [Witch Hazel](https://witchhazel.thea.codes/) theme, but it didn't have an install option for Atom, my text editor of choice. Digging through [the documentation](https://flight-manual.atom.io/hacking-atom/sections/converting-from-textmate/#convert-the-theme), though, I found out that Atom ships with a way to convert Sublime/TextMate theme bundles to Atom themes.

I contacted [Thea Flowers](https://thea.codes/), the designer of Witch Hazel, about adding the Atom instructions to the landing page, and she invited me to make a pull request. I figured out that I had to fork her repo, make my changes, and then make a pull request between the correct branches. I also needed to turn off linting in my editor to avoid a bunch of unwanted whitespace diffs - I was really only adding about 10 lines of text. I made my request and the next day, it was accepted, easy as pie. Thanks, Thea!

I also want to shoutout Jany Belluz, maker of [Fantasque Sans Mono](https://github.com/belluzj/fantasque-sans), my new favorite Terminal font.
