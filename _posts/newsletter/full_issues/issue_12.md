Hi,

Here are this weeks 5 articles on AI, ML and data science I business.

Tom



## 1. Cambridge Analytica had no role in Brexit

Cambridge Analytica had no impact on Brexit and simply did bog standard online targeted advertising work, according to a report from the Informalities nation Commissioner.

Back in 2018 a global scandal erupted over Cambridge Anaytica's  involvement in US and UK elections. Now the UK information Commissioner has published there finding about the episode:

> "SCL/CA [*Cambridge Analytica]* were purchasing significant volumes of commercially available personal data  in the main about millions of US voters.... In the main their models were also built from ‘off the shelf’ analytical tools and there was evidence that their own staff were concerned about some of the public statements the leadership of the company were making about their impact and influence."

On Brexit:

>  "SCL/CA were not involved in the EU referendum campaign in the UK "

Far from being the all powerful maker of weapons grade propaganda tools (as [Christopher Wylie](https://twitter.com/chrisinsilico) might have you believe) , it seems that on the whole CA was using standard Facebook advertising approaches to do fairly standard targeted advertising. This is simply how Facebook and operate, rather than being some sinister international mind control conspiracy.

[📖 Read more here 📖](https://ico.org.uk/media/action-weve-taken/2618383/20201002_ico-o-ed-l-rtl-0181_to-julian-knight-mp.pdf)


---

## 2. Data infrastructure is maturing

As data becomes the key to businesses success, the infrastructure that supports it is maturing.

Nearly all companies have some sort of data infrastructure. This can start with a few excel spreadsheets held on laptops, and can grow to huge data centres managed my internet giants like Google. This infrastructure can serve two main purposes:

> "To help business leaders make better decisions through the use of data (analytic use cases) and to build data intelligence into customer-facing applications, including via machine learning (operational use cases)."

Broadly, the analytics use case tends to be centred around a data warehouse, and the operational approach tends to focus on a data lake. This article gives three useful blueprints for data architectures, depending on your business requirements.:

- Modern BI (cloud based data warehouse + visualisation tools - suitable for most companies)
- Big Data (big enterprises or tech firms with complex needs. )
- AI/ML (the least mature and most difficult to get right, many companies build their own. Lots of open source projects. Many don't need this.)

BEWARE: the article linked is written by A16Z, who have a significant investment in data infrastructure company Databricks, that happens to be at the centre of most of these diagrams. Despite this, it's a useful, if slightly biased, introduction.

[📖 Read more here (2,382 words)📖](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/)


---

## 3. A new way to understand reinforcement learning

Reinforcement learning can be considered a type of supervised learning.

Reinforcement learning is an approach to machine learning that has been hugely successful in limited domains. Famously it has been used by google subsidiary, Deepmind to build algorithms that canachieve superhuman performance in the games of Go, Chess and various computer games. The algorithim learns by playing millions of games against itself and making small changes to improve performance.

However, it has tended to have less practical usage than supervised learning (learning from labelled examples).

This article gives a new way of understanding reinforcement learning as supervised learning. 

> "RL can be viewed as doing supervised learning on the “good data”."

> "The main idea is to view RL as a *joint* optimization problem over the policy and experience: we simultaneously want to find both “good data” and a “good policy.” Intuitively, we expect that “good” data will (1) get high reward, (2) sufficiently explore the environment, and (3) be at least somewhat representative of our policy. We define a good policy as simply a policy that is likely to produce good data."

I need to read this slowly. Gets pretty technical, but interesting stuff.

[📖 Read more here (2,511 words)📖](https://bair.berkeley.edu/blog/2020/10/13/supervised-rl/)


---

## 4. GPT-3 performance on a laptop

A team from Germany has bucked the recent trend for ever bigger NLP models by using a clever design.

 A common NLP task is to give labels to phrase. This type of thing is very common, as in this example involving restaurant reviews:

- "This was the best pizza I’ve ever had"
- "Pretty bad. You can get better sushi down the road for half the price."
- "Pizza was average. Not worth what they were asking."

The task might be to label these reviews as positive, negative or neutral. Usually this is done by gathering lots of examples, manually labelling them and training a model using that data. Usually the model has no undertaking of the meaning of the label. This new method suggests an alternative approach. Here,  each sentence is appended with another unfinished one like this:

- This was the best pizza I’ve ever had. The restaurant was ___________________

And the missing word could be either 'good', 'OK', or 'bad'. Because language models trained on unlabelled data are good at completing phrases like this, you can get very good model performance using a very small amount of labelled data.

On some standard benchmarks this approach out performs cutting edge tech like GPT-3. A really nice idea, well executed.

[📖 Read more here (2,510 words)📖](https://github.com/timoschick/pet)


---

## 5. AI system helps stop sepsis by working with humans

Building AI systems in healthcare is hard because it involves interacting with and changing complex human organisations.

Sepsis Watch is a system used to predict and prevent cases of sepsis in patients at Duke Hospital in North Carolina. 

AI is hard in healthcare. Making it work involves humans and machine and organisations. Anybody who has tried to implement ML in any organisation will recognise this:

> " in order to be successful, AI interventions must always be thought of as sociotechnical systems, in which social context, relationships, and power dynamics are central, not an afterthought. AI and machine learning technologies are often looked to as being the key to a solution. However, all too often potential solutions remain just that—potential solutions, which may work in theory, given pre-set conditions."

Having tried and largely failed in the past to build a system that would do exactly this I couldn't agree more how important it is to think of the entire 'sociotechnical system'. Often, building the model is the easiest part. This article focuses on all of the hard parts after that.

[📖 Read more here 📖](https://datasociety.net/library/repairing-innovation/)


---

