---
date: 2020-09-13 21:00:00
image: /assets/images/mountain.jpg
layout: post
link: https://a16z.com/2020/08/12/taming-the-tail-adventures-in-improving-ai-economics/
story_number: 1
title: Why it's hard to scale AI
word_count: '4,217'
---

Business that use machine learning and artcifial intelligentce in their products are harder to scale, argues a recent article from US based VC Anderseen Horowitz. 


> "AI development is a process of experimenting, much like chemistry or physics. The job of an AI developer is to fit a statistical model to a dataset, test how well the model performs on new data, and repeat. This is essentially an attempt to reign in the complexity of the real world.

> Software development, on the other hand, is a process of building and engineering."

The data for building supervised models often has long fat tails -  there are a few very common cases but lots of uncommon cases. This means you can never have enough data: whenever more is collected you uncover more edge cases. Often this means it is hard to build models tag work in all situation and conies end up building large numbers of bespoke models. This means its hard to scale in the ways software companies have been able to. Some advice here:

- Use simple models where you can
- Make operations efficient and repeatable
- Compartmentalise models
- Use meta models or transfer learning

No easy solutions here, but it's an interesting discussion. One thing that it leaves out as a solution is to automate th head and manually do the tail. This tends to reduce work by around 80%

