---
layout: post
date:  2020-03-10 12:00:00
url: https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00318-5
story_number: 4
title: "Cybersecurity data science: an overview from machine learning perspective"
---

[Useful survey of cybersecurity in data science](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00318-5). There is an increasing trend for using big datasets to automate and augment aspects of online security.

The most common application are in malware removal and intrusion detection. Common approaches seem fairly standard supervised ML approaches like regression, SVMs, Random Forests, and ANNs. These are trained on large historical datasets Some approaches use unsupervised methods like anomaly detection.

I have not done much work in this areas, but I'd guess it is complicated by its adversarial nature. Any potential attackers are trying to not be detected. An algorithm trained on historic data will quickly be out of date. How you prevent zero day attacks  (new unknown types)  is hard. Anomaly detection approaches might work , but would likely also result in many false positives as there are many tips of anomaly that are not necessarily malicious. This paper is a useful guide to the state of research, from a quick glance it looks like it is an area that could be improved. More research is needed, as they say.
