## 1. Billion dollar computer vision startups

![Billion dollar computer vision startups](https://ortom.co.uk/assets/images/mostafa-meraji-cUxF-FcFwL4-unsplash.jpeg)

Computer vision is where it all began. In 2012 Geoff Hinton and his team built a neural network that massively out-perfomed all other aproaches to recognising images. This breakthrough started the deep learning revolution.

Now 10 years later, this technology is being commercialised by a group of hugely successful startups. The applications attend to be specific to particular industry and range from agriculture, retail, insurance and construction. Some examples:

 - [Ceres Imaging]( https://www.ceresimaging.net/) can accurately identify crops that need more or less water
 - [Standard](https://standard.ai/) make systems for checkout free shopping
 - [Tractable](https://tractable.ai/) a London based company that allows instant damage estimates for insurers

I have not been hugely involved in computer vision, but it is intresting to see it's progress from experimental breakthrough technology, to an increasingly stable and mature  set of tools, though to eventual comercialisation over about 10 years. Making these businesses work is not about a general purpose models or algorithm so much as finding a niche application and specialising in it. I expect a similar trajectory for other areas (like NLP) over the next 5-10 years. 

**Why this matters:** AI has long overpromised and under-delivered, that might be beginning to change.

[📖 Read more (2,372 words)📖](https://www.forbes.com/sites/robtoews/2021/02/28/a-wave-of-billion-dollar-computer-vision-startups-is-coming)


---

## 2. Ray: Easier distributed computing

![Ray: Easier distributed computing](https://ortom.co.uk/assets/images/martin-sattler-mBz6QjRZKvc-unsplash.jpeg)

Ray is a framework that makes distributed computing using Python easy to set up and run.

Often when handling large datasets or models it is useful to run processes on multiple computers. This can speed up training models by parallelising things like hyper-parameter search or batch gradient descent. There are a number of ways of doing this, but they all tend to be fairy difficult to set up and require significant changes to single threaded code.

Ray makes this [easier](https://medium.com/distributed-computing-with-ray/faster-and-cheaper-pytorch-with-raysgd-a5a44d4fd220). By adding a couple of lines of code it it possible to run code on a cluster of machines running in the cloud.

**Why this matters:**  Distributed computing can be done quickly and easily without changing existing code (much)

[📖 Read more (1,292 words)📖](https://medium.com/distributed-computing-with-ray/faster-and-cheaper-pytorch-with-raysgd-a5a44d4fd220)


---

## 3. Andrew Ng says: "Sort out your data!"

![Andrew Ng says: "Sort out your data!"](https://ortom.co.uk/assets/images/16841620756_c042a071a4_c.jpeg)

Machine learning is algorithms + data. A lot of focus goes on improving algorithms, not enough goes on improving data.

Machine learning pioneer Andrew Ng recently gave a [talk](https://www.youtube.com/watch?v=06-AZXmwHjo&ab_channel=DeepLearningAI)  where he  gave several examples where algorithmic improvements made little difference but improving data made a big difference. This is contrary to the usual focus on algorithmic tweaks. Often, by improving the consistency of labelling in training data we can improve model dramatically.

I agree wholeheartedly with this point of view. In ML research (and Kaggle type competitions) there is very little focus on data exploration and understanding. This is because so many ML papers focus on improving model performance on a static benchmark dataset. This has been a useful approach but bears little resemblance to how ML is used in the real world. Time and again I have seen cases where extensive hyperparater tuning gives virtually no improvement but simple improvement to data give huge improvements. 

**Why this matters:** Taking a more systematic approach to data quality is essential to making ML work

[📖 Read more 📖](https://www.youtube.com/watch?v=06-AZXmwHjo&ab_channel=DeepLearningAI)


---

## 4. Video - the next frontier of AI

![Video - the next frontier of AI](https://ortom.co.uk/assets/images/jakob-owens-CiUR8zISX60-unsplash.jpeg)

We perceive the world more like video - a stream of audio and visual signals from a single point of view - than any other medium. Most internet traffic is video and a large proportion of time online is spent looking at video.

However, ML models tend to focus on static images and written or spoken language. This is largely down to the complexity of handling video. Recent [work](https://ai.facebook.com/blog/learning-from-videos-to-understand-the-world) by researchers at Facebook may start to change that. They have developed a method for building joint representations of audio and video data and have used it for clustering and classifying videos on Instagram. The key development, like many recent advanced in ML, is the use of large unlabelled datasets for unsupervised pre-training. 

This research is still in fairly early stages and I don't think we are quite at the stage of building rich temporal video representations of the world in the way our brains work, but it is a step forward.

**Why this matters:** Most of the data on the web is video. Now it can be used to train AI.

[📖 Read more (2,537 words)📖](https://ai.facebook.com/blog/learning-from-videos-to-understand-the-world)


---

## 5. Easier text to speech with Hugging Face + Wav2Vec

![Easier text to speech with Hugging Face + Wav2Vec](https://ortom.co.uk/assets/images/marco-bianchetti-vzFTmxTl0DQ-unsplash.jpeg)

Alexa, Siri and the rest have made speaking to computers a natural thing to do. The big tech firms have spent lots of money creating automatic speech recognition (ASR) models that convert speech to text. 

Generally this has been a hard problem needing specialised domain knowledge and large amounts of labelled data. However, the [latest models](https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean) have achieved state of the art performance on much smaller volumes of labelled data by doing unsupervised pre-training on large unlabelled datasets.

Now the marvellous people at [Hugging Face](https://huggingface.co/) have made the best performing of these algorithms, Wave2Vec,  [available](https://huggingface.co/facebook/wav2vec2-base-960h) as part of its open source Transformers library. Hopefully this will make it easier for practitioners to make progress on building audio models using this as a starting point.

**Why this matters:** Speech is the big new way of interacting with computers. The makes development open to all.

[📖 Read more (5,551 words)📖](https://huggingface.co/blog/fine-tune-wav2vec2-english)


---