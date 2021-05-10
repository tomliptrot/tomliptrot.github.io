---
category: mlops
date: 2021-05-11 08:30:00
image: /assets/images/newsletter/issue_19/jessica-johnston-nnH2l-k77nc-unsplash.jpeg
layout: post
link: https://docs.featurestore.org/
story_number: 5
title: What the hell is a feature store?
word_count: '628'
---

A feature store is an emerging concept for storing and retrieving data in Machine Learning applications.

There are competing requirements for a database that supports a machine learning application. For training tasks it needs to work well offline on large datasets. For inference it needs to work quickly for smaller number of rows of data. It also needs to store metadata and support feature engineering. 

Various products already exist that support each of these requirements, and feature stores bring these together under a single system that keeps data synchronised. [Feast](https://github.com/feast-dev/feast) and [Hopsworks](https://github.com/feast-dev/feast) are two open source products that look promising. Various big tech firms (Uber, Netflix, Twitter, Facebook, Pinterest) have also open sourced their products.

🛎️ **Why this matters:** Feature stores may become a key element of ML infrastructure.