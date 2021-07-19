---
category: machinelearning
date: 2021-07-20 07:30:00
image: /assets/images/newsletter/issue_23/richard-lee-iobEsH91mbk-unsplash.jpeg
important: A really interesting development from DeepMind
layout: post
link: https://www.arxiv-vanity.com/papers/2103.03206/
story_number: 2
title: Deepmind's new multimodal variation on the Transformer
word_count: 11,122
---

A new modification the the transformer model has been developed to allow usage on raw images, audio and video data.

Transformers are great for NLP tasks, but there is a problem with scale as the size of the input grows. This is fine for language, where a length of about 1,000 is OK for many tasks, but for images, video and audio, the input data size tends to be much larger. This is typically overcome by using architectures specifically designed for the type of data, such as convolutions, that take advantage of out knowledge of the stricture of the data.

Google offshoot, DeepMind have published a new [paper](https://www.arxiv-vanity.com/papers/2103.03206/) addressing this issue and proposing an architecture that works well with all sorts of input, without making any assumptions about its structure. This its more similar to how biological brains function [citation needed].

I can't pretend to keep up with all of the latest development in deep learning. Keeping up to date with this stuff is a full time job. The paper looked really interesting and a [video](https://www.youtube.com/watch?v=P_xeshTnPZg&ab_channel=YannicKilcher) by Yannic Kilcher helped me understand it. I'll need to reread it to fully understand what's going on.

One thing I'm struck by is how much deep learning is still constrained by hardware capabilities rather than algorithms or data. It's likely that the next big advances will come when the chips get faster/smaller rather than algorithmic development like this.