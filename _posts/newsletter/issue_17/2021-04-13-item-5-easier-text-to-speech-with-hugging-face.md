---
category: null
date: 2021-04-13 08:30:00
image: /assets/images/marco-bianchetti-vzFTmxTl0DQ-unsplash.jpeg
layout: post
link: https://huggingface.co/blog/fine-tune-wav2vec2-english
story_number: 5
title: Easier text to speech with Hugging Face + Wav2Vec
word_count: 5,551
---

Alexa, Siri and the rest have made speaking to computers a natural thing to do. The big tech firms have spent lots of money creating automatic speech recognition (ASR) models that convert speech to text. 

Generally this has been a hard problem needing specialised domain knowledge and large amounts of labelled data. However, the [latest models](https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean) have achieved state of the art performance on much smaller volumes of labelled data by doing unsupervised pre-training on large unlabelled datasets.

Now the marvellous people at [Hugging Face](https://huggingface.co/) have made the best performing of these algorithms, Wave2Vec,  [available](https://huggingface.co/facebook/wav2vec2-base-960h) as part of its open source Transformers library. Hopefully this will make it easier for practitioners to make progress on building audio models using this as a starting point.

**Why this matters:** Speech is the big new way of interacting with computers. The makes development open to all.

