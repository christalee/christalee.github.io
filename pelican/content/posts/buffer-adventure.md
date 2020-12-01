title: Buffer the Slayer
date: April 2019
tags: portfolio, programming
img: buffer-adventure.png

When I was teaching programming at the [Workshop School](https://www.workshopschool.org/), I eventually expected my students to learn about object-oriented programming (OOP). As it’s not a paradigm I use frequently, I wanted to refresh my memory, both about OOP and about how to teach it. So I dug up a project from my own student days: a text adventure game featuring Buffer the Vampire Slayer. We were given a basic object system for locations and NPCs, and asked to implement magic objects, secret locations, and our own creative game ideas. The project was re-themed shortly afterward to feature Hairy Cdr and the Chamber of Stata, but otherwise is well described on [MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/projects/st05project4.pdf)

Unfortunately this project was written in [Scheme](https://groups.csail.mit.edu/mac/projects/scheme/), a LISP variant, not a language I was teaching at the time. So I decided to rewrite it in Python, and re-teach myself about objects at the same time. After the initial, fairly literal, translation, I added a test suite to prevent regression while refactoring. Currently, the game is playable but perhaps not very fun; it lacks a win condition, for one thing. I imagine I'll add that next. In the meantime, you can check it out [on Github](https://github.com/christalee/buffer-adventure).
