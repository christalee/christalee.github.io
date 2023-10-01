title: the joy of react
tags: javascript, programming

I've recently started some PD at work with [The Joy of React](https://www.joyofreact.com/), a course by React maven Josh Comeau. It promises to teach me not just the basics but also some "happy practices" (hedging on "best practices") that I'm expected to bring back to my daily practice. Several of my coworkers have joined, mostly backend devs who want to expand their skills (being on a full-stack team).

Since I haven't written in this blog since starting work, basically, I should probably describe what I do. I work at a health tech startup, building reasonable interfaces for a complex, data-rich system. After focusing on our page that summarizes all the available information for a specific patient (in digital and print!), I've shifted into rebuilding that view, optimized now for being rendered responsively in an iframe inside a medical records program. We're targeting Epic first, but hoping to extend our work to other EMRs without much additional work. This work relies on open protocols like OAuth and SMART on FHIR, but I haven't had to grapple much with that. Primarily I've been doing the React side, pulling together action items and presenting them to the provider to be filled out. (We hope to minimize dual documentation in a future project.)

Taking this Joy of React course, so far I am reminded not to take anything for granted - just because I use React every day, doesn't mean I have nothing to learn! Some of it is down to differences in our codebase - for example, we use [styled-components](https://styled-components.com/) while the course uses [CSS Modules](https://github.com/css-modules/css-modules). A recent lesson on forms was frustrating because we use a library / base components for forms instead of the raw HTML elements, so I don't remember the syntax of regular forms particularly well. But I'm moving along with it, in my downtime. My goals look something like:

- get a model of how to design complex state without drowning (we have some complex components in our codebase, primarily because everyone was focused on adding one more feature and never stepped back to say, is it time to refactor now?)
- gain confidence in my ability to design my own hooks (this is more about error handling and possibly working with Promises)
- understand better how to organize functions and components for readability and ease-of-use

Hopefully I'll learn these lessons and find opportunities to apply them straightforwardly.