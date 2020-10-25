## 1. Cambridge Analytica had no role in Brexit

Cambridge Analytica had no impact on Brexit and simply did bog standard online targeted advertising work, according to a report from the ICO.

> "SCL/CA were purchasing significant volumes of commercially available personal data  in the main about millions of US voters, to combine it with the Facebook derived insight information they had obtained from an academic at Cambridge University, Dr Aleksandr Kogan, and elsewhere. In the main their models were also built from ‘off the shelf’ analytical tools and there was evidence that their own staff were concerned about some of the public statements the leadership of the company were making about their impact and influence."

>  "SCL/CA were not involved in the EU referendum campaign in the UK "

Far from being the all powerful maker of weapons grade propaganda tools (as [Christopher Wylie](https://twitter.com/chrisinsilico) might have you believe) , it seems that on the whole CA was using standard Facebook advertising approaches to do fairly starred targeted advertising. This is simply how Facebook and operate, rather than being some sinister international mind control conspiracy.

[📖 Read more here 📖](https://ico.org.uk/media/action-weve-taken/2618383/20201002_ico-o-ed-l-rtl-0181_to-julian-knight-mp.pdf)


---

## 2. Data infrastructure is maturing

As machine learning becomes a key part of business, the infrastructure that supports it is maturing.

Lots of companies have some sort of data infrastructure.

> "Data infrastructure serves two purposes at a high level: to help business leaders make better decisions through the use of data (analytic use cases) and to build data intelligence into customer-facing applications, including via machine learning (operational use cases).\"

Broadly, the analytics use case is entered around a data warehouse, and the operational approach tends to focus on a data lake. These is some convergence between these, as data lakes become more structured. (Data reservoirs maybe?)

This article gives three useful blueprints for data architectures::

- MODERN BI (cloud based data warehouse+ visualisation tools - suitable for most companies)
- MULTIMODAL DATA PROCESSING (big enterprises or tech firms with complex needs. Uses all the tools.)
- AI/ML (the least mature and most difficult to get right, many companies build their own. Lots of open source projects. Many don't need this.)

[📖 Read more here (2,382 words)📖](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/)


---

## 3. A new way to understand reinforcement learning

Reinforcement learning can be considered a type of supervised learning.

Reinforcement learning is an approach to machine learning that has bee hugely successful in limited domains. Famously it has been used by deep mind to build algorithms that gain achieve superhuman performance in the games of Go, Chess and various computer games. It does this by playing milions of games against itself and making small changes to improve performance.

However, it has tended to have less practical usage than supervised learning (learning from labelled examples).

This article gives a new wy of undertaking RL as supervised ML. I need to read this slowly...

[📖 Read more here (2,511 words)📖](https://bair.berkeley.edu/blog/2020/10/13/supervised-rl/)


---

## 4. GPT-3 performance on a laptop

A new AI algorithm uses a clever trick to complete natural language tasks with much less need for data and computing. 

A team from Germany has bucked the recent trend for bigger and bigger NLP models by clever design.  A common NLP task into label these types of phrases:

- "This was the best pizza I’ve ever had"
- "Pretty bad. You can get better sushi down the road for half the price."
- "Pizza was average. Not worth what they were asking."

The task might be to table these as positive, negative or neutral. Usually this is done by gather lots of examples, manually labelling them and training a model using that data. This new method suggests and alternative approach, where the model has to fill in a sentence like this:

- This was the best pizza I’ve ever had. The restaurant was ___________________

Where the missing word could be either 'good', 'OK', or 'bad'. Because language models are good at competing phrases like this, you can get very good model performance using a very small amount of labelled data.

[📖 Read more here (2,510 words)📖](https://github.com/timoschick/pet)


---

## 5. Healthcare: AI system helps stop sepsis

Building AI systems in healthcare is hard because it involves interacting with and changing complex human organisations.

Sepsis Watch is a system used to predict and prevent cases of sepsis in patients at Duke Hospital in North Carolina. 

AI is hard in healthcare. Making it work involves humans and machine and organisations. Anybody who has tried to implement ML in any organisation will recognise this:

> " in order to be successful, AI interventions must always be thought of as sociotechnical systems, in which social context, relationships, and power dynamics are central, not an afterthought. AI and machine learning technologies are often looked to as being the key to a solution. However, all too often potential solutions remain just that—potential solutions, which may work in theory, given pre-set conditions."

Having tried and largely failed in the past to build a system that would do exactly this I couldn't agree more how

[📖 Read more here 📖](https://datasociety.net/library/repairing-innovation/)


---