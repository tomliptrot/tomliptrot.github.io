## 1. Why your AI is not working

![Why your AI is not working](https://ortom.co.uk/assets/images/newsletter/issue_22/belinda-fewings-H5zhUJz9DnQ-unsplash.jpeg)

Your AI isn't working because you have asked it the wrong question.

In the *[Hitchhikers Guide to the Galaxy](https://www.amazon.co.uk/dp/B003GK2180)*, mice (who are actually super intelligent aliens) build a huge computer to find the answer to the Ultimate Question. After 7.5 million years the answer was finally produced. 

It was 42. Unfortunately no one knew what the question was. 

So the mice build a computer the size of a small planet (called "Earth") to calculate the Ultimate Question. That turned out to be "*What do you get when you multiply six by nine?*".

This type of problem is know in AI circles as the "Alignment Problem" and is commonly faced in business.

A company used ML  to predict which customers would leave. The results were then used to target promotions at those customers enticing them to stay. They did not. The company should have asked a more focused question like “Given a budget of $x million, which customers should we target with a retention campaign?”.

This [article](https://hbr.org/2021/07/why-you-arent-getting-more-from-your-marketing-ai) provides some useful pointers on how to arrive at the right question.

🛎️ **Why this matters:** Asking the wrong question is the most common reason ML projects fail.

[📖 Read more (3,815 words)📖](https://hbr.org/2021/07/why-you-arent-getting-more-from-your-marketing-ai)


---

## 2. Don't use neural nets for recommenders either (maybe)

![Don't use neural nets for recommenders either (maybe)](https://ortom.co.uk/assets/images/newsletter/issue_22/franki-chamaki-wkvKZR4e2OI-unsplash.jpeg)

Recommender systems are used extensively by online businesses. Systems using neural networks may not be as effective as advertised.

Over the last 4-5 years deep learning has become a popular technique in recommender systems. Recent [research](https://thedataexchange.media/questioning-the-efficacy-of-neural-recommendation-systems) conducted by [Paolo Cremonesi](https://paolocremonesi.faculty.polimi.it/) and [Maurizio Ferrari Dacrema](https://mauriziofd.github.io/) has found that many pulsed findings are difficult to replicate and tend not to prove significant improvement over simpler methods like K-nearest neighbours.

The difficulty in reproducing research is a broad problem faced across science. Another problem for recommender systems is that there is not a single, large data set like Imagenet that is used by all researchers. Lots of published results use deep learning, but it is not the best for performance - at least some of the reason for this is that deep-learning is 'trendy' and more likely to get accepted by journals and conferences.

🛎️ **Why this matters:** Unfortunately, we should take all published research with a pinch of salt. Beware fashions!

[📖 Read more (1,129 words)📖](https://thedataexchange.media/questioning-the-efficacy-of-neural-recommendation-systems)


---

## 3. AI is eating the world

![AI is eating the world](https://ortom.co.uk/assets/images/newsletter/issue_22/pacman-151558_1280.png)

Is a future coming where AI will write the code that will build new AI that will build new AI? Maybe...

Github, the leading version control hosting site (owned by Microsoft) has released a new [tool](https://copilot.github.com/) that has been built with the AI research company OpenAI. You enter a small amount of code, or even a description of what you want, and the tool fills in the rest. Examples shown are pretty impressive.

The tool is built using the same types of language model behind GPT-3 and BERT, and they have been trained on millions of lines of open source code. It is not perfect and we don't all have to worry about our jobs just yet, but it is only a matter of time.

🛎️ **Why this matters:** First application by Microsoft of their collaboration with OpenAI. Beginning of the end for software developers?

[📖 Read more (2,436 words)📖](https://copilot.github.com/)


---

## 4. Applied AI is more like running a restaurant than boiling an egg

![Applied AI is more like running a restaurant than boiling an egg](https://ortom.co.uk/assets/images/newsletter/issue_22/peter-bond-zmsR0qeKQyo-unsplash.jpeg)

Using machine learning models in a business setting is very different from academia or Kaggle.

Instead of trying to work out HOW to do things, you often have to work out WHAT to do. According to a new [article](https://explosion.ai/blog/applied-nlp-thinking) by [Ines Montani](https://www.linkedin.com/in/inesmontani/) at Explosion AI, applied ML is more like running a restaurant than knowing how to cook. When you cook, you need to know how to use equipment, work with ingredients and reproduce recipes. When you run a restaurant you need to know how to cook but you also need to select dishes that work well together, source ingredients, optimise profit and ensure reliability.

Applied ML is more about deciding what to cook, and less about how to cook it. This is something that doesn't tend to get taught and can take a long time to learn.

🛎️ **Why this matters:** Applying technologies is the key to getting value from them. It is a separate skill from building and undertaking them.

[📖 Read more (3,984 words)📖](https://explosion.ai/blog/applied-nlp-thinking)


---

## 5. Where's my self driving car?!

![Where's my self driving car!?](https://ortom.co.uk/assets/images/newsletter/issue_22/aditya-chinchure-H0OSpZ4vJDo-unsplash.jpeg)

Over the last decade we have been promised self driving cars 'soon' - what's going on?

AI pioneer Andrej Karpathy, Director of AI at Tesla, gives a fascinating [talk](https://youtu.be/g6bOwQdCJrc) at the Conference on Computer Vision and Pattern Recognition. Updating us on where they are. It has some interesting titbits:

➡ Using vision to predict depth and velocity. No need for RADAR or detailed 3d maps.

➡ Collecting real data from Tesla fleet, labelling very well and carefully.

➡ Auto labelling as a good source of data. Using complex models with low latency to build training data from lighter, more specialist models.

➡ Separate networks for each type of output - detection, attributes, kinematics, trajectory, etc.

➡ Nice release and validation process. Unit tests, shadow modes.

🛎️ **Why this matters:** An interesting look behind the scenes at Tesla, but full autonomy is still just over the horizon...

[📖 Read more (23 words)📖](https://youtu.be/g6bOwQdCJrc)


---