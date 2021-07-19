---
category: mlops
date: 2021-07-20 07:30:00
image: /assets/images/newsletter/issue_23/lenny-kuhne-jHZ70nRk7Ns-unsplash.jpeg
important: Useful post, although somewhat light on fully usable details.
layout: post
link: https://eng.uber.com/continuous-integration-deployment-ml/
story_number: 3
title: Uber's approach to deploying machine learning
word_count: 2,251
---

Continuous Integration and Continuous Deployment (CI/CD) are widely used in software development, but doing it for ML can be a bit more tricky.

Machine learning models are a tricky halfway point between data and code. Trained models have similar functionality to  code, but are learnt from and represented by data. Therefore standard approaches to version control, testing and CI/CD have to be tweaked a bit to work.

A recent [blog](https://eng.uber.com/continuous-integration-deployment-ml/) post from Uber describes how they approach this. Uber have many ML models in production, providing critical services. Therefore they need to be both reliable and maintainable. ML engineers need to easily be able to add new features to models or tweak architectures without damaging old models and keeping the service running. Here Uber describe how they use dynamic model loading using a model artefact and config store to decouple model and server development cycles. Doing this allows ML engineers to easily replace models without having to change all of the serving code. To do the syou also need extensive and reliable testing frameworks and it seems like they have the stoo.