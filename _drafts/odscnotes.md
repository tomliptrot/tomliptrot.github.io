## Day 1: Wednesday

#### Sequence modelling with deep learning

[Natasha Latysheva](https://www.linkedin.com/in/nslatysheva/) Machine Learning Engineer @ Welocalize, language services provider



Really good clear, Pitched right (for me)

Sequence models from first principles. Quickly and clearly we got taken on a tour from feed forward Neural Nets to Recurrent NNs, GRU/LSTMs up to recent advances in encoder-decoders, Bi-RNNS, attention and transformers.

The tutorial (see this [Git Repo](https://github.com/nslatysheva/ODSC_Sequence_Modelling) took us through building a Language model based on the Game of Thrones books. Where we built an LSTM model based on the text from the popular fantasy series. Here is some of the model code:

```python
model = Sequential()
model.add(Embedding(vocabulary_size, 50, input_length=max_sequence_length-1))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocabulary_size, activation='softmax'))
```

We looked at using the model generatively to simulate text from a 'seed' phrase. Here is an example where the seed phrase was

> A dragon, the dead, and Tyrion walk into a...

and the output was:

> A dragon, the dead, and Tyrion walk into a great roast of rubies the wind was the same and the way he had been a man of the harpy

Encoder-decoder architecture better than seq->seq RNN.  seq -> vector -> seq

Bidirectional RNN (BRNN) - two hidden states, read text in both directions...

Problem with encoder/decoder is bottleneck in vector in the middle.

Attention solution to this - removes intermediate vector -> decoder has access to hidden states of encoder.

**Transformers and self-attention**

Transformers are taking over NLP. Still using encoder-decoder. Changing what these do. See paper: [Attention is all you need](https://arxiv.org/abs/1706.03762). More parallel. 

Self-attention is the key part. seq-> seq model within encoder

Attention weighs matrix, converts input to new output Dot produce between word embedding. high values for similar words. Attention weight matrices model word similarities. Different heads different types of similarities - similarity matrix.

Query, Key and Value Transformations??

Are these better because of scalability or is it because of a 'better' model?

Would you recommend skipping RNNs and going to transformers?

Alex Smola lectures on youtube.

[www.talktotransformer.com]

#### scikit-learn

[Andreas Muller](https://amueller.github.io/), Professor at columbine and developer on scikit-learn. [Book: Introduction to Machine Learning with Python](http://shop.oreilly.com/product/0636920030515.do)

Good, knowledgeable speaker:

> "I can ignore the warnings because I wrote them!"

Nice to have  break from neural nets - this is the workhorse of data science.

**Pipelines**

[github repo](https://github.com/amueller/ml-workshop-1-of-4)

Logistic regression in scikit-learn.

This is no fun!

```python
from sklearn.linear_model import LogisticRegression

pipe = make_pipeline(StandardScaler(), LogisticRegression())

param_grid = {'logisticregression__C': [0.01, 0.1, 1, 10, 100]}

X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, random_state=4)
grid = GridSearchCV(pipe, param_grid)
grid.fit(X_train, y_train)
print(grid.best_estimator_.named_steps.logisticregression.coef_)
```

Parameter grid `GridSearchCV` - nice with pipelines

Parameter tuning with [hyperband](https://github.com/zygmuntz/hyperband) [2](https://github.com/thuijskens/scikit-hyperband)

**metrics**

Always specify what is the 'positive' class - no conventions here....

Don't use accuracy - particaulry

#### Pytorch

Difficult post lunch slot - so my notes are a bit more sparse.

[Daniel Voigt Godoy](https://www.linkedin.com/in/dvgodoy/) from Deloitte [twitter](https://twitter.com/dvgodoy)

[colab link](https://colab.research.google.com/github/dvgodoy/PyTorch101_ODSC_London2019/blob/master/PyTorch101_Colab.ipynb)

[github](https://github.com/dvgodoy/PyTorch101_ODSC_London2019)

Basics, from first principles.

![img](http://karlstratos.com/drawings/linear_dogs.jpg)

[source](http://karlstratos.com/)

Implementing linear regression using gradient descent - uses all of pytorch's feature in simple example.

Next step here https://pytorch.org/tutorials/



#### Gaussian Processes

[github](https://github.com/boschresearch/GP_tutorial)

Had to sit on the floor... left early.

#### Dinner



## Thursday

#### Keynote

**IBM**

I guess if you are the 'diamond' sponsor you get to do a sales pitch. Maybe it could be a bit better disguised. I'm never very impressed with Watson - its basically just branding of a fairly standard service. I once was pitch dot by IBM and it was about 25 consultants in suits with 1 statistician on the phone suggesting to use a linear regression. Telling a room full of data scientists about how data can change our organisations is a bit reductive. 85% of statistics are made up on the spot. 

AutoAI -haha. Premature visitor centre I say. Such a small percentage of a data scientists time is spent running through various models to select the best. Professional data science is nothing like a kaggle competition where you are given a dataset nicely formatted in csv. The work is in understanding the business problem and how the data relates to it. Prediction is the quick bit at the end...

To be fair the organiser didn't look too happy with the talk...

Next up is:

**Prof Micheal Woodridge** Turing Institute, Oxford

**The Future is Multi-Agent!**

good speaker, clear, engaging, slightly text heavy slides (academics eh?!)...

Started in Manchester...

Five Trends in Computing

- Ubiquity - computers are everywhere
- Interconnection - everything is connected
- Delegation - Computers making decisions for us. fly by wire, driverless cars
- Human Orientation - Making computers more accessible, like how we interact with people
- Intelligence - NOT an exponential trend, but there is progress. 'Solving' NP complete problems.

The prof reckons this means: Multi-agent systems

intelligent agents that talk to each other. siri->siri, robot->robot etc...

For this to work: agent needs to know what you want/ your preferences. Also needs social skills. cooperate, coordinate, negotiate.

The need to be able to work as a team. Do we know how humans do this?

TOM: Why do humans cooperate? Social/political/evolutionary reasons. It's not just self interest/ quanifiable. Would agents naturally do the same? We don't generally cooperate with animals.

Bunch of applications. meetings, micro-commerce, connected cars, robots in warehouses, car pooling, agent-driven business workflows, agent based simulation.

Profs actual research (not sales) is in unstable equilibria. Flash Crash - Dow Jones lost loads. markets recovered. How do you understand and predict multi-agent dynamics. Option:

1. Treat it as a bug - rational verification. Model checking. Treat program as a graph? Turing award winner 2007. Nash Equilibrium.
2. simulate it: Agent based modelling. For big systems game theory doesn't work. Suggests that approaches to stop flash crash by banks will not work. Takes lots of compute.

He's a singularity skeptic. if you want to lose sleep over something, AI isn't the thing. Nuclear, climate change, fossil fuels.



#### Tools for higher performance python

[Ian Ozvald](https://ianozsvald.com/)

High Performance Python book

Interim chief data scientist. speak to him.

Making python code go faster. 

`%%timeit` for timing stuff in jupyter

`line_profiler` - profiling package. `LineProfiler`

`df.apply(functionalists, axis, raw=True)`faster way of iterating over a pandas df.

[swifter](https://github.com/jmcarpenter2/swifter) - project for running code multicore. sits on dask. `df.swifter.apply`

precompile functions with [numba](http://numba.pydata.org/)

```python
import numba

@numba.jit(nopython=True)
def foo(row):
	dostuff
```

[Dask](https://dask.org/) - multicore vs distributed computing.. dask-ml for distributed sklearn ml. easy to parallelised Pandas functions. 

[shelve](https://docs.python.org/3/library/shelve.html) cache module

[bulwark](https://pypi.org/project/bulwark/) - pandas testing/schema... have a look...

**The Soul of AI**

[Joe Blue](https://twitter.com/joebluems?lang=en) Data Robot

[github](https://github.com/joebluems/Soul_Of_AI)

#### non-supervised learning

Danilo  J Rezende, Deep Mind

@deepspiker

https://DaniloRezende.com

Why it is useful to learn models of the world.

Generative models.

Reinforcment learning in a stochastic and partially observed world.

An action is any change to the world. 

IMPALA: scalable distributed deep-RL (espeholt, soyer). Simulation of agent interacting with environment.

Beyond classification - modelling the inputs, not the outputs. Understanding causal structure.

WaveNet is state of art generative text to speech model. Used in every google voice product.

Generative model - learn a simulator.

Future of modelling is integrating models with agents.

paper:"[One-shot generalisation in deep generative models](https://arxiv.org/abs/1603.05106)", Danilo Rezende

paper:"[neural scene representation and rendering](https://deepmind.com/blog/article/neural-scene-representation-and-rendering)": really interesting. Generative Query Network (GQN), . Filling in 3-d scenes from small number of images. Actions driven by reducing uncertainty (a la Friston). GQN, learns factorised representation of a scene. [full paper](https://storage.googleapis.com/deepmind-media/papers/Neural_Scene_Representation_and_Rendering_preprint.pdf)

Paper: "Shaping beliefs with xxxx"

Success is due to: bigger compute, better models.

Stream of video prediction - not working yet. Next big challenge.

**Making robust business decisions with sparse data**

[Sarah Jarvis](https://www.linkedin.com/in/sarah-jarvis-9411264/), Head of Data Science, prowler.io

Not all big problems are solved by big data...

1. Many data points, but many combinations. Eg. Millions of shipping routes, thousands of ports, so not that many between 2 specific routes.
2. Not all data is directly observable. 

We should quantify uncertainty in our models. Use Gaussian Processes + Bayesian inference.

Why gaussian processes are useful: 

1. extremely versatile (lots of kernels available)
2. data efficient
3. transparent and explainable
4. Can quantify uncertainty.

Uncertainty is a feature not a bug... because, it can :tell you where to collect data, can tell you how confident you are

Four Levels of AI:

1. Predictive
2. Instructive
3. Integrated
4. Autonomous

CASE STUDY: pallets. AIM: reduce the number of failed collections from retailers.

**Ethical AI**

@vincent_spruyt

Vincent Spruyt from Sentiance

See slides for links...

Ethical AI is not about ethical business or AI in general??

EEC - High Level Expert Group...

Focus on Fairness: Bias. Cognitive Bias vs Statistical Bias.

Prejudicial Bias.

Avoiding Disparate treatment...

Equalise across some metric eg, equal precision or equal recall. There are costs to this...

Compass (northpoint inc) used to aid judges on recidivism. Predictive parity - equal precision in each group....

q: what happened when there are multiple groups?

q: what happens if you don't collect the data on the groups? Can get it for a smaller subgroup. Or Some sort of representation/ latent space modelling.

Papers on pre-processing. IBM toolbox for this.

Can change loss function.


## Friday

**AI for price optimisation** 

David Adey and Alexey Drozdetskiy

[Altius](https://www.altiusdata.com/) data consultancy

Keeps talking about "older operational research stuff" wonder what he means and how it differs from what he is pedalling?

steps:

- Standardise (replicate existing approaches)
- Optimise
- Explore

Algorithm choices... time based regression... is it a causal model? Does it include competitor dynamics? Any hierarchical modelling?

How is binary different from 1-hot?

Seems to be just 'predicting price' from a bunch of features...





#### Missed Tutorial on Tuesday

 ["Latest Deep Learning Models for NLP"](https://odsc.com/training/portfolio/latest-deep-learning-models-for-natural-language-processing/) @ the European Open Data Science Conference 2019 (London)

https://github.com/AMDonati/ODSC2019-DL-models-NLP