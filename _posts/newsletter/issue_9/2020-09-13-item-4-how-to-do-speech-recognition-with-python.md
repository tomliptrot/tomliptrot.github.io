---
date: 2020-09-13 21:00:00
image: /assets/images/jason-rosewell-ASKeuOZqhYU-unsplash.jpg
layout: post
link: https://github.com/Uberi/speech_recognition
story_number: 4
title: How to do speech recognition with Python
word_count: '3,502'
---

Easily convert speech to text in Python with the SpeechRecognition library. Add voice to you application with a few lines of code:

```python
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("Sphinx thinks you said " + r.recognize_sphinx(audio))

print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
```
Thats it!  It has built in support for 7 different speech recognition engines (from Google, IBM, Microsoft and others), most are cloud based, but 2 work off-line as well.

