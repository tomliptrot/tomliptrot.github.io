## 1. The 28 billion dollar private AI companies

![The 28 billion dollar private AI companies](https://ortom.co.uk/assets/images/newsletter/issue_19/james-lee-qSf_4bNsoWc-unsplash.jpeg)

There are 28 privately held ML, AI and data companies, that are nearing IPO. Their total valuation is around $119B.

US investor [Matt Turk](https://www.linkedin.com/in/turck/) has put together a  [list](https://mattturck.com/emergingmad/) of these so-called unicorns that compliments his [other list](https://mattturck.com/madindex/) of public traded firms.  They seem to split into three main groups:

- Databases (eg [Airtable](https://airtable.com/), [Redis](https://redislabs.com/), [Couchbase](https://www.couchbase.com/))
- AI platforms  ([Databricks](https://databricks.com/), [Dataiku](https://www.dataiku.com/), [Datarobot](https://www.datarobot.com/))
- Process Automation ([Celonis](https://www.celonis.com/), [Hypersciene](https://hyperscience.com/), [Instabase](https://instabase.com/?ib=v2))

Many of these companies do not use AI and ML in their products: they make tools to make it easier to use for other businesses - selling picks and shovels in a gold rush. Many are overlapping and competing and it will be interesting to see which take off in a huge way and which disappear over the next few years.

🛎️ **Why this matters:** This list shows where companies have been successful so far in using AI and ML. It's mostly in building tools.

[📖 Read more (1,300 words)📖](https://mattturck.com/emergingmad/)


---

## 2. Should we stop hiring data scientists?

![Should we stop hiring data scientists?](https://ortom.co.uk/assets/images/newsletter/issue_19/clem-onojeghuo-fY8Jr4iuPQM-unsplash.jpeg)

Over the last decade, companies have hired thousands of data scientists. These teams often fail to deliver. 

To solve this problem, we need analysts and data engineers and software engineers, not more data scientists, [writes](https://towardsdatascience.com/why-you-shouldnt-hire-more-data-scientists-3188a1597fa3) data scientist [Adam Sroka](https://www.linkedin.com/in/aesroka/). Data scientists tend to be inquisitive researchers with a broad, but shallow skill set. For open-ended tasks that require understanding of novel, complex concepts, they can be very good. Often, however, other skill sets would be more suitable.  

For writing business reports and presenting financical information, an analyst would be better. For building and managing data infrastructure and pipeline, a data engineer would be better. And for building robust scalable, interactive software, a software engineer would be better. 

Often data scientists end up doing the work that would better be done by other people. These specialists would probably do a better job faster and cost less. 

🛎️ **Why this matters:** Before you hire a data scientist, work out if you really need one.

[📖 Read more (2,073 words)📖](https://towardsdatascience.com/why-you-shouldnt-hire-more-data-scientists-3188a1597fa3)


---

## 3. Keep it simple! Deploy a model on a single machine

![Keep it simple! Deploy a model on a single machine](https://ortom.co.uk/assets/images/newsletter/issue_19/david-van-dijk-3LTht2nxd34-unsplash.jpeg)

Deploying ML models doesn't always need GPUs or Kubernetes clusters. Sometimes a simple, single machine is plenty.

In the rush to 'scale' it is possible to ignore simple solutions. A single virtula machine (VM) is easy to build, deploy and maintain. It is possible to make a fast and simple model serving system with a single virtual machine and a bit of code optimisation, [writes](https://www.comet.ml/site/how-to-10x-throughput-when-serving-hugging-face-models-without-a-gpu/) Jacques Verré, product manager at Comet ML. Verré describes the process of benchmarking and improving performance of an API that served the [Bert](https://huggingface.co/transformers/model_doc/bert.html) NLP model using [Fast API](https://fastapi.tiangolo.com/); with some really simple modifications he was able to improve performance from 6 requests per second to 100. That is 8.6 million requests per day!

Some of the improvements he made were:

- Turning off gradient computation in Pytorch
- Tuning FastAPI by adding more gunicorn workers and turning off asynchronous processing
- Using model distillation to decrease model size
- Choosing the right cloud instances (30 vCPUs)

🛎️ **Why this matters:** If you can get away with it, keep it simple!

[📖 Read more (1,768 words)📖](https://www.comet.ml/site/how-to-10x-throughput-when-serving-hugging-face-models-without-a-gpu/)


---

## 4. Your brain is an internet

![Your brain is an internet](https://ortom.co.uk/assets/images/newsletter/issue_19/640px-Gray's_Anatomy_plate_517_brain.png)

The brain has been compared to a plumbing system, a watch, a computer and now the internet.

Metaphors are useful in framing our understating of one phenomena in terms of another. A new [book](https://www.berfrois.com/2021/05/an-internet-in-your-head-by-daniel-graham/) by Daniel Graham argues that the internet is a more useful metaphor for the brain than a computer.

Computers have become a dominant metaphor for how our brains work, we 'store' and 'retrieve' memories,  we try to 'reboot' or 'upgrade' our minds. This way of thinking has been helpful but has limitation. The process has gone two ways: the brain has been used to inspire how we program computers. Neural networks are based on a simple conception of how neurons in the brain work and have been hugely successful.

But perhaps the internet, a loosely connected network of independent components, is a better way to think of our brain, and allows us to get insights into why we can't always understand why we do what we do.

🛎️ **Why this matters:** If your brain is an internet, how do you filter spam?

[📖 Read more (2,533 words)📖](https://www.berfrois.com/2021/05/an-internet-in-your-head-by-daniel-graham/)


---

## 5. What the hell is a feature store?

![What the hell is a feature store?](https://ortom.co.uk/assets/images/newsletter/issue_19/jessica-johnston-nnH2l-k77nc-unsplash.jpeg)

A feature store is an emerging concept for storing and retrieving data in Machine Learning applications.

There are competing requirements for a database that supports a machine learning application. For training tasks it needs to work well offline on large datasets. For inference it needs to work quickly for a smaller number of rows of data. It also needs to store metadata and support feature engineering. 

Various products already exist that support each of these requirements, and feature stores bring these together under a single system that keeps data synchronised. [Feast](https://github.com/feast-dev/feast) and [Hopsworks](https://github.com/feast-dev/feast) are two open source products that look promising. Various big tech firms (Uber, Netflix, Twitter, Facebook, Pinterest) have also open sourced their products.

🛎️ **Why this matters:** Feature stores may become a key element of ML infrastructure.

[📖 Read more (628 words)📖](https://docs.featurestore.org/)


---