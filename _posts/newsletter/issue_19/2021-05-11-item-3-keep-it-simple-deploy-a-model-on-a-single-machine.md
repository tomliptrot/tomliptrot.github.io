---
category: mlops
date: 2021-05-11 08:30:00
image: /assets/images/newsletter/issue_19/david-van-dijk-3LTht2nxd34-unsplash.jpeg
layout: post
link: https://www.comet.ml/site/how-to-10x-throughput-when-serving-hugging-face-models-without-a-gpu/
story_number: 3
title: Keep it simple! Deploy a model on a single machine
word_count: 1,768
---

Deploying ML models doesn't always need GPUs or Kubernetes clusters. Sometimes a simple, single CPU machine is plenty.

In the rush to 'scale' it is possible to ignore simple solutions. A single VM is easy to build, deploy and maintain. It is possible to make a fast and simple model serving system with a single virtual machine and a bit of code optimisation, [writes](https://www.comet.ml/site/how-to-10x-throughput-when-serving-hugging-face-models-without-a-gpu/) Jacques Verré, product manager at Comet ML. Verre describes the process of benchmarking and improving performance of an API that served the [Bert](https://huggingface.co/transformers/model_doc/bert.html) NLP model using [Fast API](https://fastapi.tiangolo.com/), with some really simple modifications he was able to improve performance from 6 requests per second to 100. That is 8.6 million requests per day!

Some of the improvements he made where:

- Turning off gradient computation in Pytorch
- Tuning FastAPI by adding more gunicorn workers and turning off asynchronous processing
- Using model distillation to decrease model size
- Choosing the right cloud instances (30 vCPUs)

🛎️ **Why this matters:** If you can get away with it, keep it simple!