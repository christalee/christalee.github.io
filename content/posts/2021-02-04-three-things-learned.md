title: Three Things Learned
tags: RC, programming, javascript, python

I haven't been keeping up with this blog, but I have been keeping busy. A few things I've learned recently:

- Although JavaScript has a `typeof` command, it doesn't produce very useful output. In particular, it yields `object` no matter whether the structure in question is a Map, an Array, a Set, or an Object. Apparently, `x.constructor` is how to find out what type something actually is.

- On bash, `which` is a program, not a builtin. So it's not aware of aliases, like `python='python3'`. Neither is `sudo`. So you can check `python --version >= 3` but that's no guarantee that `sudo pip install` or `sudo python -m pip install` will be python3. It makes me rethink the utility of aliases, and possibly virtualenvs.

- Python lists are not implemented with pointers like Lisp lists! Per [Peter Norvig](https://norvig.com/python-lisp.html), Python list access is O(1); per the [Python Design and History FAQ](https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython), they are contiguous memory chunks with a head pointer and length value stored up front.

Three things make a post, plus it's dinnertime: fried tofu w/ bbq sauce, risotto, and Sichuan dry-fried mushrooms & peppers.
