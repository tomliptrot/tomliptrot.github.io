## 1. It's not all about machine learning

![It's not all about machine learning](https://ortom.co.uk/assets/images/newsletter/issue_23/myriam-zilles-L3FwT4qMeT0-unsplash.jpeg)

Early stage start-ups tend not to use data to drive decisions because they don't have much.  Once they get some, making the transition to being a data driven organisation can be hard. 

[Erik Bernhardsson](https://www.linkedin.com/in/erikbern/) has written a [short story](https://erikbern.com/2021/07/07/the-data-team-a-short-story.html) written in the second person, a bit like a Choose Your Own Adventure ("You are in a room, there is an axe"). Telling the tale of growing a data team at a mid-stage startup. 

You arrive to find a fragmented picture with various teams having their own "data scientists". The core team is disillusioned as they are not getting to do any cool ML. Management is excited because it wants to do cool AI. What actually needs to happen is months of data cleaning, integration, SQL and infrastructure work.

You get to work, reorganising the team so that resource management is decentralised and people management is centralised. You sort out that data, creating a single unified data warehouse. Some of your data scientists leave. You start to get the basics right, the company starts to learn from data. After a year or so you start to implement some fancy ML.

🛎️ **Why this matters:** A parable that many in data science will find instructive

[📖 Read more (4,979 words)📖](https://erikbern.com/2021/07/07/the-data-team-a-short-story.html)


---

## 2. Deepmind's new variation on the Transformer

![Deepmind's new variation on the Transformer](https://ortom.co.uk/assets/images/newsletter/issue_23/richard-lee-iobEsH91mbk-unsplash.jpeg)

A new modification to the transformer model has been developed to allow usage on raw images, audio and video data.

Transformers are great for NLP tasks, but there is a problem with scale as the size of the input grows. This is fine for language, where a length of about 1,000 is OK for many tasks, but for images, video and audio, the input data size tends to be much larger. This is typically overcome by using architectures specifically designed for the type of data, such as convolutions, that take advantage of our knowledge of the structure of the data.

Google offshoot DeepMind has published a new [paper](https://www.arxiv-vanity.com/papers/2103.03206/) addressing this issue and proposing an architecture that works well with all sorts of input, without making any assumptions about its type. This is more similar to how biological brains function [citation needed].

I can't pretend to keep up with all of the latest developments in deep learning as doing so is a full time job. The paper looked really interesting and a [video](https://www.youtube.com/watch?v=P_xeshTnPZg&ab_channel=YannicKilcher) by Yannic Kilcher helped me understand it. I'll need to reread it to fully understand what's going on.

One thing I'm struck by is how much deep learning is still constrained by hardware capabilities rather than algorithms or data. It's likely that the next big advances will come when the chips get faster/smaller rather than algorithmic development like this.

🛎️ **Why this matters:** A really interesting development from DeepMind

[📖 Read more (11,122 words)📖](https://www.arxiv-vanity.com/papers/2103.03206/)


---

## 3. Uber's approach to deploying machine learning

![Uber's approach to deploying machine learning](https://ortom.co.uk/assets/images/newsletter/issue_23/lenny-kuhne-jHZ70nRk7Ns-unsplash.jpeg)

Continuous Integration and Continuous Deployment (CI/CD) are widely used in software development, but doing it for ML can be a bit more tricky.

Machine learning models are halfway between data and code. Trained models have similar functionality to  code, but are learnt from and represented by data. Therefore standard approaches to version control, testing and CI/CD have to be tweaked a bit to work.

A recent [blog](https://eng.uber.com/continuous-integration-deployment-ml/) post from Uber describes how they approach this. Uber have many ML models in production, providing critical services. Therefore they need to be both reliable and maintainable. ML engineers need to easily be able to add new features to models or tweak architectures without damaging old models and keeping the service running. Here Uber describe how they use dynamic model loading using a model artefact and config store to decouple model and server development cycles. Doing this allows ML engineers to easily replace models without having to change all of the serving code. To do this you also need extensive and reliable testing frameworks and it seems like they have this too.

🛎️ **Why this matters:** Useful primer on CI/CD for ML, although somewhat light on fully usable details

[📖 Read more (2,251 words)📖](https://eng.uber.com/continuous-integration-deployment-ml/)


---

## 4. Pydash: a useful bunch of Python tools

![Pydash: a useful bunch of Python tools](https://ortom.co.uk/assets/images/newsletter/issue_23/cesar-carlevarino-aragon-NL_DF0Klepc-unsplash.jpeg)

Some common tasks in Python are harder than they need to be.

[Pydash](https://pydash.readthedocs.io/en/latest/index.html) is a nice library that attempts to plug some of those gaps as in these examples:

```python
import pydash

# Arrays
pydash.flatten([1, 2, [3, [4, 5, [6, 7]]]])
[1, 2, 3, [4, 5, [6, 7]]]

pydash.flatten_deep([1, 2, [3, [4, 5, [6, 7]]]])
[1, 2, 3, 4, 5, 6, 7]

# Collections
pydash.map_([{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}], 'name')
['moe', 'larry']

# Functions
curried = pydash.curry(lambda a, b, c: a + b + c)
curried(1, 2)(3)
```

🛎️ **Why this matters:** This is a  handy bunch of tools

[📖 Read more (1,026 words)📖](https://pydash.readthedocs.io/en/latest/index.html)


---

## 5. Brickit - ML for old Lego

![Brickit - ML for old Lego](https://ortom.co.uk/assets/images/newsletter/issue_23/xavi-cabrera-kn-UmDZQDjM-unsplash.jpeg)

Do you have loads of old Lego? Can't think what to make with it? Worry no more!

[Brickit](https://www.producthunt.com/posts/brickit) is a new app (for iOS only) that allows you to point your camera at an old pile of Lego bricks. It will identify what types of bricks you have and suggest models you can build based on this. The brick identification uses machine learning to identify and classify each brick.

🛎️ **Why this matters:** A fun application of ML - no need for tiresome use of your imagination!

[📖 Read more (225 words)📖](https://www.producthunt.com/posts/brickit)


---