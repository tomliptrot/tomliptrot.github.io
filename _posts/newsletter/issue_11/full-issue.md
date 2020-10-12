## 1. What is it like to be a smartphone?

Can we say for sure a smartphone isn't conscious? What about a bacteria? A bat?

In 1974 Thomas Nagel wrote  ["What Is It Like to Be a Bat?"](https://www.sas.upenn.edu/~cavitch/pdf-library/Nagel_Bat.pdf) In the article he argued that no matter how much we might know about the winged mammals we can never know how it feels to be one.  We share common ancestry and biology to these creatures yet they are alien and inaccessible to us.

This article argues that if recognising a bats consciousness is hard, recognising a machine's is impossible. It would be so alien to us we would not be able to recognise it. 

> In all the chatter about the future of artificial intelligence, the question has been glossed over or, worse, treated as settled. The longstanding assumption, a reflection of the anthropomorphic romanticism of computer scientists, science fiction writers, and internet entrepreneurs, has been that a self-aware computer would have a mind, and hence a consciousness, similar to our own. We, supreme programmers, would create machine consciousness in our own image.

I am fascinated by consciousness. We know so little about it, yet is all we do know. We can never know another beings consciousness but we are stuck in out own. 

A great  conjecture with wide ranging implications.

[📖 Read more here (1,449 words)📖](http://www.roughtype.com/?p=8528)


## 2. AI investor reviews 2020

It's been a funny old year so far, and apparently it's already time to start doing roundups. Last week AI investor Matt Turk produced his review of AI and data in 2020.

There are some interesting findings:

- Data infrastructure tooling is getting more mature and stable. I think this only holds for BI and 'analytics'. At the innovation coal face thing are very much in flux. Generally open source rules but there are few firm standards.
- There is some useful stuff on orchestration engines. I will have a look at [Prefect](https://docs.prefect.io/) [Dagster](https://docs.dagster.io/) and [Kedro](https://kedro.readthedocs.io/en/stable/01_introduction/01_introduction.html).
- NLP is big: Transformers all the way. 
- ML in production in enterprise is happening and maturing. I like this quote: 

> Just like “Big Data” before it, ML/AI, at least in its current form, will disappear as a noteworthy and differentiating concept, because it will be everywhere.

Have a look at the big picture of logos the end to see if your favourite data company is there!

[📖 Read more here (4,506 words)📖](https://mattturck.com/data2020/)


## 3. Keep your brain on its toes

A Google employee was bored with how great his life was (poor thing!) so he stared leaving lot of decisions to chance. His life suddenly got even better. Woo hoo!

There is a theory that the brain is a machine for reducing predictive uncertainty. Errors in predictions of our stream of sensory inputs drive action to reduce them, feeding back and creating all of our thoughts and behaviours. 

Hunger is a feeling brought about by the prediction that we are about to eat. Eating food is the action that reduces that predictive error.

Philosopher and cognitive scientist Andy Clark is its biggest proponent of what he calls 'predictive processing'.  In this essay he tell  a story about how increasing short term uncertainty can help reduce long term uncertainty by moving you out of local minima.

This essay gets a bit technical toward the end, bit its worth reading as an account of the different types of uncertainty and their role in our lives.

[📖 Read more here (7,337 words)📖](https://aeon.co/essays/use-uncertainty-to-leverage-the-power-of-your-predictive-brain)


## 4. Tidy modelling book published

A new book on  modelling the tidy way in R has been published.

I love R. Even though I mostly use Python lately.

I still love R and have used it for years.

But. It struggles with Machine Learning. 

And the statistical modelling approaches all have different APIs split over many packages. 

The tidyverse and dplyr are great and their AIS are well though out and consitent.

Enter Tidy Models.

A unified approach to modelling that is tidy and has a consistent API. 

Great stuff. I've been watching the development of these packages for a while and it looks like they have matured a lot. Really good work from [Max Kuhn](https://www.linkedin.com/in/max-kuhn-864a9110/).

[📖 Read more here (1,309 words)📖](https://www.tmwr.org/)


## 5. AI in healthcare lags behind

Very little progress has been made in modelling electronic healthcare data in recent years.

Over the last decade huge improvements have been made in two key areas of machine learning: vision and language. But the holy grail for many is for machine learning to have an equally large impact on a field like medicine. Recent advances of medical machine learning have tended to be on vision based tasks such as radiology and other diagnostics.

However, medical applications of ML on electronic patient records data have not seen a similar leap forward.

A new paper by  a [David Bellmay](https://www.linkedin.com/in/drbellamy/) and colleagues argues some of this is due to a lack of good benchmarks:

>  Through our meta-analysis, we find that the performance of deep recurrent models is only superior to logistic regression on certain tasks. 

Useful modelling using healthcare data is important but hard to do. There are issues with data access, bias, quality and volume. It is hard to validate and apply models in the real world as you need to be pretty sure what you have built works (unlike in e-commerce). 

This paper is a useful contribution but I fear we need more than just benchmarks to drive a revolution.

[📖 Read more here 📖](https://arxiv.org/abs/2010.01149)
