---
category: machine learning
date: 2020-10-25 21:00:00
image: /assets/images/national-cancer-institute-N_aihp118p8-unsplash.jpg
layout: post
link: https://bair.berkeley.edu/blog/2020/10/13/supervised-rl/
story_number: 3
title: A new way to understand reinforcement learning
word_count: '2,511'
---

Reinforcement learning can be considered a type of supervised learning.

Reinforcement learning is an approach to machine learning that has been hugely successful in limited domains. Famously it has been used by google subsidiary, Deepmind to build algorithms that canachieve superhuman performance in the games of Go, Chess and various computer games. The algorithim learns by playing millions of games against itself and making small changes to improve performance.

However, it has tended to have less practical usage than supervised learning (learning from labelled examples).

This article gives a new way of understanding reinforcement learning as supervised learning. 

> "RL can be viewed as doing supervised learning on the “good data”."

> "The main idea is to view RL as a *joint* optimization problem over the policy and experience: we simultaneously want to find both “good data” and a “good policy.” Intuitively, we expect that “good” data will (1) get high reward, (2) sufficiently explore the environment, and (3) be at least somewhat representative of our policy. We define a good policy as simply a policy that is likely to produce good data."

I need to read this slowly. Gets pretty technical, but interesting stuff.

