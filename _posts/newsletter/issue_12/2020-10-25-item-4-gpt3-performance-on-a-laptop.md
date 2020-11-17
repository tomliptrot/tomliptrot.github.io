---
category: machine learning
date: 2020-10-25 21:00:00
image: /assets/images/daniel-lonn-Regf9o7r_ZM-unsplash.jpg
layout: post
link: https://github.com/timoschick/pet
story_number: 4
title: GPT-3 performance on a laptop
word_count: '2,510'
---

A team from Germany has bucked the recent trend for ever bigger NLP models by using a clever design.

 A common NLP task is to give labels to phrase. This type of thing is very common, as in this example involving restaurant reviews:

- "This was the best pizza I’ve ever had"
- "Pretty bad. You can get better sushi down the road for half the price."
- "Pizza was average. Not worth what they were asking."

The task might be to label these reviews as positive, negative or neutral. Usually this is done by gathering lots of examples, manually labelling them and training a model using that data. Usually the model has no undertaking of the meaning of the label. This new method suggests an alternative approach. Here,  each sentence is appended with another unfinished one like this:

- This was the best pizza I’ve ever had. The restaurant was _____________

And the missing word could be either 'good', 'OK', or 'bad'. Because language models trained on unlabelled data are good at completing phrases like this, you can get very good model performance using a very small amount of labelled data.

On some standard benchmarks this approach out performs cutting edge tech like GPT-3. A really nice idea, well executed.



