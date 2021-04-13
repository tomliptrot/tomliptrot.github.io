---
category: null
date: 2021-04-13 08:30:00
image: /assets/images/martin-sattler-mBz6QjRZKvc-unsplash.jpeg
layout: post
link: https://medium.com/distributed-computing-with-ray/faster-and-cheaper-pytorch-with-raysgd-a5a44d4fd220
story_number: 2
title: "Ray: Easier distributed computing"
word_count: 1,292
---

Ray is a framework that makes distributed computing using Python easy to set up and run.

Often, when handling large datasets or models, it is useful to run processes on multiple computers. This can speed up training models by parallelising things like hyper-parameter search or batch gradient descent. There are a number of ways of doing this, but they all tend to be fairly difficult to set up and require significant changes to single threaded code.

Ray makes this [easier](https://medium.com/distributed-computing-with-ray/faster-and-cheaper-pytorch-with-raysgd-a5a44d4fd220). By adding a couple of lines of code it it possible to run code on a cluster of machines running in the cloud.

**Why this matters:**  distributed computing can be done quickly and easily without changing existing code (much).
