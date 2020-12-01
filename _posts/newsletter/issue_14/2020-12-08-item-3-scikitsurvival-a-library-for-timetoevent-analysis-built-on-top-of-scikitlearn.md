---
category: null
date: 2020-12-08 08:30:00
image: /assets/images/hourglass-620397_1280.jpg
layout: post
link: https://jmlr.org/papers/v21/20-729.html
story_number: 3
title: 'scikit-survival: A Library for Time-to-Event Analysis Built on Top of scikit-learn'
word_count: '136'
---

Almost all data has some kind of time-related element. Often this is ignored.

Let's take customer churn as an example: the event we are interested in is a customer cancelling their subscription. Given the data we have today, we can't know if a given user would continue subscribing for years to come or if they might cancel tomorrow. This is called censoring and is handled using survival analysis.

There is a large body of work on how to deal with this type of data, with origins in medicine (time to death or recurrence) and engineering (time to failure). Scikit survival makes it easier to handle this type of data using the scikit-learn machine learning library for Python.

