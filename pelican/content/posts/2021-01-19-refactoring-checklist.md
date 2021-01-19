title: refactoring checklist; ML project ideas
tags: programming, RC

In a recent conversation I mentioned that when I meet a new Python feature, I add it to my refactoring checklist. Someone asked me to share that checklist, and here it is, slightly expanded:

- write all comments/docstrings
- resolve all TODOs
- add types to all fn declarations and key local vars
- expand short names to something explanatory
- for loops -> list comprehensions
- use dict comprehensions
- use generator or lazy iterator?
- use collections.Counter to count things
- use map, filter, reduce?

Obviously this doesn't address the "main" work of refactoring, like moving chunks of code around. But it's a list of stuff to look out for before pushing for public consumption, to encourage my code to be elegant, concise, and useable.

<hr />

In other news, I'm looking for excuses to use the Heap computing cluster, which means a machine learning problem with significant HD or processor requirements. So far I'm considering:

- restarting my Bengali.AI OCR project
- doing something involving text prediction/generation, like Byronic poetry or Shakespearean sonnets or murder ballads
    - definitely want a PD corpus
    - pairing with a colleague taught me about beam search, which generates several high-scoring text strings rather than simply the best token-by-token one
    - inspiration: [text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation), Coursera NLP with Tensorflow Week 4
- helping experiment with a colleague's image captioning AI
- some Kaggle competition TBD?
