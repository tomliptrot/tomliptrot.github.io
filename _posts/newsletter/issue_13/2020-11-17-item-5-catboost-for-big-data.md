---
category: machinelearning
date: 2020-11-17 08:30:00
image: /assets/images/cat-912291_1280 .jpg
layout: post
link: https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00369-8
story_number: 5
title: Catboost for big data
word_count: 22,655
---

For structured, heterogenous data, gradient boosting is the way to go.

For all of the hoo-ha about deep learning, the most widely used machine learning algorithm is either logistic regression or gradient boosted decision trees. Gradient boosting is a method whereby you iteratively fit simple models to your data (typically shallow trees), but weight each iteration based on the errors of the previous iteration. It tends to produce good prediction in medium to large datasets.

This paper reviews [Catboost](https://catboost.ai/) which, alongside [Xgboost](https://xgboost.readthedocs.io/en/latest/) and [LightGBM](https://lightgbm.readthedocs.io/en/latest/), is one of the most popular gradient boosting implementations. It is particularly well suited to categorical data (hence the name) and doesn't work well with homogenous numeric data like images. The paper compares implementation and describes application in fields such as psychology, transport and chemistry.

