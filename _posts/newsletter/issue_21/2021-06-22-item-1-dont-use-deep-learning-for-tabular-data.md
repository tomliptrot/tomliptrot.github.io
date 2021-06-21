---
category: machinelearning
date: 2021-06-22 08:30:00
image: /assets/images/newsletter/issue_21/nick-fewings-dRCQJZoTYCc-unsplash.jpeg
layout: post
link: https://www.arxiv-vanity.com/papers/2106.03253/
story_number: 1
title: Don't use deep learning for tabular data
word_count: 4,445
---

Most business data is tabular (think Excel or SQL type data), and deep learning is generally not the tool for modelling it.

I think people already know this, but it's good to hear it again. A new [paper](https://www.arxiv-vanity.com/papers/2106.03253/) shows that XGboost tends to beat DNNs for tabular data. Deep-learning is great, but its not the solution for most problems with data seen in businesses today. If you have images, languages or sound the deep neural networks designed to deal with these are often very effective. But when you have rows and columns made up of a mixture of continuous and categorical data, XGBoost is probably a better bet.

> "Our study shows that XGBoost outperforms these deep models across the datasets, including datasets used in the papers that proposed the deep models. We also demonstrate that XGBoost requires much less tuning."

🛎️ **Why this matters:** Tabular data still rules in most businesses. Use the right tool for the job.

