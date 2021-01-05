title: Advent of Code 2020, in JavaScript
tags: programming

I’m doing Advent of Code this year using JavaScript, with the goal of forcing myself to learn the ins and outs of the language. And boy, does it have a lot of those. Here are some reflections on traps and quirks I’ve discovered.

Initially I wrote JS literally as I would Python, but with JS syntax: parens around conditions, curly braces instead of colons, semicolons at the end of statements. I quickly realized that the equivalent of Python’s `for x in y` statement is not JS’s `for (x in y)`, but `for (x of y)`. The first produces indices of the array, sort of like Python’s `enumerate`, while the second produces elements of the array, which is usually what I want. When I did eventually want `for (x in y)`, I found a second quirk: those indices may be integers that I can use as `Array[i]`, but that doesn’t mean I can add them to other numbers! Adding 1 to the indices produced `01, 11, 21, 31` instead of `1, 2, 3, 4`, suggesting that the indices are some Number/String hybrid.

Explicit casting to `Number` or `String` isn’t so bad, but declaring variables is very strange. Part of the issue is that (again, like I would in Python) I want to use Jupyter Notebooks as my development environment. They’re an easy way to re-run code against different inputs and zero in on sections as I debug, instead of running the whole file every time. I am keeping finished solutions in a [regular JS file](https://github.com/christalee/AoC/blob/master/aoc_2020_code.js) and I have opened it up in the Node REPL (`node -i`) to check that they give the right answer, but it’s such a pain to load in code and run it, I wouldn’t want to do that all the time. Luckily, I found [IJavaScript](https://github.com/n-riesco/ijavascript) and it works fine.

However, I quickly found that declaring variables with `let` and `const` prevents me from re-running a cell, because you can’t re-declare a variable. To avoid having to restart the kernel every time I want to re-run things, I started leaving off `let` and `const`. That’s how I discovered that variables declared without keywords are global. I managed to define a variable in one branch of an `if` statement, but use it in both, which worked sporadically, depending on whether I had previously followed the branch where it was defined or not. Otherwise, it silently failed, returning an empty list. I don’t have a good sense yet of when to expect errors, return values, etc. in JS, but I was not expecting that level of dysfunction. JS frequently tells me when something is undefined, why not in an `else` branch?

So now I put in as many `let` and `const` statements as I can, and put up with restarting the kernel perpetually. It takes away from some of the convenience, for sure. I also noticed that `let` and `const` variables are block-scoped, which means I have to declare them outside a block if I want them to be available later on. I’m pretty sure variables in Python blocks are function-scoped… as are JavaScript `var` declarations. Apparently this is one reason not to use `var` anymore. Regardless, it was a surprise, but I’ve accepted it as part of the general fashion for declaring variables upfront. Thank goodness for iterable unpacking, which works for assignments in Python and JavaScript (`[a, b] = [1, 2]`).

My favorite JavaScript shocker, and the one I find least defensible, came when I wanted to sort an array. I’m trying not to get too bent out of shape at the lack of built-in functions for common operations: `range`, `sum`, etc. But `[40, 50, 100, 200].sort()` should not yield `[ 100, 200, 40, 50 ]`. Why would you sort non-Strings as if they’re Strings? :head_explodes: It turns out you can specify a sort algorithm, which I’ve done sometimes in Python but for more advanced stuff, like “sort on the value of key x”. While I’m griping, I’ll also say that I don’t entirely understand why empty lists sneak in at the end of data I’m loading from file, or why a random `undefined` showed up as the first element of the first list in a list of 300+ lists. Not the rest, just that one.

So I’ve learned to be extra careful in checking my inputs manually but given the inconsistent warning about undefined variables, this is probably going to keep tripping me up and I’m just going to have to roll with it. Or abandon the effort - a couple of days ago I was not entirely sure it was worth learning JS to this degree. But I’d like to feel more comfortable with JS, or at least, some language other than Python. My partner suggested that I’m feeling all the pain of JS without the benefit of the nice graphical stuff it typically enables, and I get that, but adding in more complexity / figuring out a development environment that includes the browser is beyond me right now.

If you’re doing Advent of Code, good luck and have fun! I’m trying to keep up with every day, working in JavaScript; for the first 5 days I allowed myself to switch to Python if I was stuck as long as I ultimately implemented a solution in JS, and also I was doing that day’s puzzles from 2017 in Python as a bonus challenge. But now that I’m working all in JS I don’t really have the energy to do more. Whatever language you’re using, whatever challenge you’ve set for yourself, I hope you find something surprising and wonderful!

Cheatsheet (JavaScript analogues to Python structures I use frequently):

- `Map() -> dict()`
- `Map.get(x) -> dict[x]`
- `Map.set(x, y) -> dict[x] = y`
- `Map.entries() -> dict.items()`
- `Array() -> list()`
- `Array.slice(start, stop) -> list[start:stop]`
- `Array.push(x) -> list.append(x)` (which is different from `list.extend(x)` or `list += x`!)
- `Array.sort((a, b) => a - b) -> sorted(list)` (or `list.sort()` for in-place)
- `String.replace(/old/g, new) -> str.replace(old, new)` (is that `sed` regex syntax?)
- `for (x of y) -> for x in y:`
- `for (x in y) -> for i, x in enumerate(y):`
- `if (f.includes(x)) -> if x in f:`
- `&&, ||, ! -> and, or, not`
