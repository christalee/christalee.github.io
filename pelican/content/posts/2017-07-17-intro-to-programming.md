---
title: Introduction to Programming
tags: computer science, programming, education
summary: Colleagues often consult me for advice on teaching programming as fledgling or non-programmers. Here are capsule reviews of various tools and approaches for beginners.
---

Colleagues often consult me for advice on teaching programming as fledgling or non-programmers. Here are capsule reviews of various tools and approaches for beginners.

### Philosophy

When picking a platform/curriculum for programming, I focus on these criteria:

- how familiar or easy to learn it is for the instructor
- how aligned it is to pre-existing student interests (games, fan/professional/personal webpage, mobile app, robots - all popular)
- whether you want to teach programming in a job context ('learn to make a webpage'), or as a medium for student work on other topics ('use Twine/Scratch to tell a story about...')

My colleagues teach with 1:1 Chromebooks, so they need tools that keep student work in the browser (look out for older tools that use Flash). You know your students best - how well do they type? proofread? read directions (vs. video or interactive hints)? If they are aiming at careers in programming (or other STEM), definitely plan opportunities for "real coding"; but if not, it may be more frustrating than rewarding.

If you want a crash course in CS pedagogy, "computational thinking" is the keyword, but it isn't necessary unless you're looking for some organizing principles/vocabulary.
<!-- (I wrote more about computational thinking here.) -->

### Stuff I've Done
To give you a concrete idea of where I'm coming from, here are CS activities I taught or facilitated with colleagues:

- basic programming in [Scratch](https://scratch.mit.edu/), up through loops and variables (8 weeks)
- basic HTML/CSS -> build a webpage in [Weebly](https://www.weebly.com/)
- students building Android apps in [App Inventor](http://appinventor.mit.edu/explore/)
- students exploring game dev with [Unity 3D](https://unity3d.com/)
- student writing a Python app to display assignment due dates in the classroom, based on the teacher's updated Google Calendar (using OAuth & RasPi)
- students exploring basic programming with [Codecademy](https://www.codecademy.com/), [Code.org](https://code.org/), and [CodeCombat](https://codecombat.com/)
- "dissecting" a broken iMac & other electronics

###Making a Webpage

[Mozilla Thimble](https://thimble.mozilla.org/en-US/) is the most friendly [webpage editor/remixer](https://github.com/mozilla/thimble.mozilla.org/wiki/Using-Thimble-FAQ) I know of. You can write your template "from scratch" and include directions as a tutorial, then publish and send the link to students to remix. Downsides: students might have to make an account; everything will be licensed attribution-only, so this isn't a good platform if students want to use lots of other people's copyrighted photos, etc. (If it's all their own writing and images, or they get permission & give credit, great!)

[Weebly](https://www.weebly.com/) is also popular. Its main mode is drag-and-drop, though you might be able to dig into themes and options to work with the raw HTML.

I haven't used [codepen.io](https://codepen.io/) specifically, but it looks like a decent online web dev editor. You would have to find or write lessons.

The easiest and cheapest option for hosting might be to keep webpages and assets in a public Google Drive folder. If you create in Thimble, you can download instead of publishing; if you'd rather use a different editor, Caret is good, and can save directly to Drive on Chromebooks. If this is meant to be a homepage students can use and update in the future, having it in their Google Drive sounds better than on another site/account they will forget about once the project is over.

###Graphics, Animations

For students new to coding who might not be sure what aspects of programming appeal to them most, I tend to go with Scratch; the floor is low, the community/knowledge base is very robust, and since you can define variables and functions, the ceiling is pretty high. It's the simplest way to get interactive/animated graphics and music, which many students consider important to making games. And students familiar with the block environment can move on to Android apps with App Inventor.

For reference, here is a set of Scratch activities I used in a [freshmen programming elective](https://drive.google.com/drive/folders/0BxkPVQhGc8zXREhxYVJfbTh5aEk?usp=sharing).

I've been interested in Twine but haven't used it with students. My plan was always to focus on storytelling, with the HTML/CSS being enrichment. If you decide to go with Twine, I am super curious to hear how it goes!

###Other Popular Tools

I've only used Code.org's classic [Hour of Code](https://studio.code.org/hoc/1) as a Day 1/Week 1 intro to block programming. I see tutorials there from other familiar resources:

[Codecademy](https://www.codecademy.com/) - scaffolded tutorials on many subjects for a general adult audience; not good for students who don't read or process directions well

[Khan Academy](https://www.khanacademy.org/computing/computer-programming) - not as polished as CodeCademy or Code.org, but if you use Khan for other topics, maybe stick with it!

[CodeCombat](https://codecombat.com/) - Python or Javascript, framed as a hero quest RPG; silly, but ok for self-study

[Blockly Games](https://blockly.games/) - a self-contained online curriculum with a ramp from blocks to text editor, maybe short on guidance for self-study but should be fine in the classroom
