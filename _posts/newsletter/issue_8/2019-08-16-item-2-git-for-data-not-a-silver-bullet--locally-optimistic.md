---
date: 2020-08-16 21:00:00
image: /assets/images/yancy-min-842ofHC6MaI-unsplash.jpg
layout: post
link: https://locallyoptimistic.com/post/git-for-data-not-a-silver-bullet/
story_number: 2
title: 'Git for data: not a silver bullet?'
---

Recently a lot of effort has gone into improving the quality of 'production' machine learning system. One approach that has gained a lot of momentum and that I am a fan of is Data Version Control- a kind of git for data. 

This [article](https://locallyoptimistic.com/post/git-for-data-not-a-silver-bullet/) by Michael Kaminsky argues that it does not solve all problems and may not be necessary. Kaminsky suggests that rather than having muliple copies of data under a version control system it is easier just to have transformation code in version control and keep a log of your data.

> If you have the raw data and you have the transformation code in version control, you can re-create the transformed data from any point in time just by checking out the correct version of the transformation code and applying it to the raw data — assuming your transformations are deterministic (please, please make sure this is the case) you don’t need to version your data because you can always trivially recreate it.

Good point. Well made. Although I don't think his suggestion is a sliver bullet either. His approach works when you have full control over the entire data pipeline. Data used for ML models is not always neatly stored in a data warehouse and often comes from multiple sources in multiple formats. It may be that there isn't a single solution to all problems, but the attention on it should be welcomed.

