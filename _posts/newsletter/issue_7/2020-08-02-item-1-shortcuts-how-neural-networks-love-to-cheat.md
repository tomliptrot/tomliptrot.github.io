---
date: 2020-08-02 21:00:00
image_url: null
layout: post
link: https://thegradient.pub/shortcuts-neural-networks-love-to-cheat/
story_number: 1
title: "Shortcuts: How Neural Networks Love to Cheat"
---

If you’ve ever built a machine learning model that failed to work in production, it might have been taking a shortcut. [This article ]( https://thegradient.pub/shortcuts-neural-networks-love-to-cheat/) defines ‘shortcuts’ as:

> decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions. Shortcut opportunities come in many flavors and are ubiquitous across datasets and application domains

Often models will learn based on artefacts of the dataset used for training rather than the underlying causal structure. This can lead to problems when you try to use the model in a real setting.

It's nice to see some attention given to this problem. I think the key takeaway from this article is to take a skeptical approach and to test things thoroughly on independent data. Machine learning literature has a somewhat unhealthy obsession with obtaining 'State Of The Art' performance on benchmark datasets. I think that is partly responsible for this problem. In the real world, robustness, simplicity and explainability have much more value than an extra percentage accuracy.

