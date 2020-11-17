Hi,

Welcome to this weeks news letter. 5 Great articles on data science, AI, ML and startups. Please share if you enjoy it.

I'm changing my sending day to every second Tuesday morning from now on. I hope you like this weeks articles.

## 1. Data discovery platforms

Platforms are being developed to aid data discovery.

Data discovery is an important part of data science. Often companies hold data across multiple sources and systems. Finding different sources and linking them together takes up a large portion of data scientists' time. So it is understandable why people would want to make the process easier.

Lots of big tech firms have been building platforms to help make this process more efficient. Some, including [Amundsen](https://www.amundsen.io/amundsen/) from Lyft, Apaches [Atlas](https://atlas.apache.org/#/), and [DataHub](https://linkedin.github.io/datahub/) from Linked-in, have open sourced these platforms.

It seems they combine natural language search (based on elastic search mostly) with easily accessible information on how data links together, how and when it has been used, and who owns the data.

I'm not sure how easy it would be to integrate these systems in a new company - datasets are often spread across many systems including multiple clouds and various SaaS systems. These platforms do, however, look like they could be a useful starting point.

[📖 Read more here (3,433 words)📖](https://eugeneyan.com/writing/data-discovery-platforms/)


---

## 2. Frantic man live codes a neural network library

A video of Joel Grus creating a neural network library from scratch in Python. 

Grus is a data scientist and presenter of the Adverserail learning podcast. In this YouTube video he builds a neural network library from scratch. It's really useful to see this - both for coding tips and understanding how neural networks work. He builds a basic library, including all of the key elements of a neural network, and then uses it to solve some simple problems.

It's an impressive feat and demonstrates a deep level of understanding: if you can live code something complex and teach it well you must really know what is going on.

It's also good to see somebody actually coding (along with all the mistakes everybody makes) and how he uses the tools (VS code, mypy, extensive use of type hints). You don't get this in standard static tutorials or blog posts. You will learn more in one hour watching this video than many long online courses that teach a sanitised version of the world.

[📖 Read more here 📖](https://www.youtube.com/watch?v=o64FV-ez6Gw&ab_channel=JoelGrus)


---

## 3. Post election post

Polls got the US election really wrong again.

Here is an early take from Tim Hartford (with reference to Andrew Gelman).

> "The pre-election numbers suggest that in a typical poll with 500 positive responses, 255 went for Mr Biden and 243 for Mr Trump. But typical response rates are 5 in 100 — often lower, says Andrew Gelman, a statistician and prominent election modeller. He says that only around 1 in 100 people respond to opinion polls. So now picture 10,000 people, 255 who called their vote for Mr Biden, 243 for Mr Trump and 9,500 who never responded. How confident are we feeling now?"

I think the key issue is selective non-response. For some reason, Trump supporters are less likely to speak to pollsters. If some characteristic  (say suspicion of the 'establishment') makes people more likely to vote for Trump and also makes them *less* likely to respond to surveys, then it is almost impossible to get polls right. Expect more dodgy polls in the future!

[📖 Read more here (7,573 words)📖](https://timharford.com/2020/11/why-the-polls-got-it-wrong/)


---

## 4. How to hire people

Hiring people in startups is important but is often done badly.

One simple trick: don't hire. As Eric Torenberg explains:

> "One of the biggest mistakes I see founders make is that they hire too quickly. Once their startup raises $1M+, they immediately want to recruit 8-10 people to look "official," when in reality they should be focused on the mechanics of finding product market fit.
>
> One trick is to not mention headcount when telling other people how your startup is going — you want to measure your worth by your customer traction, not the size of your team."

If you do want to hire, plan it well, be methodical, know what you are looking for and move quickly.

[📖 Read more here (4,065 words)📖](https://eriktorenberg.substack.com/p/frameworks-for-hiring)


---

## 5. Catboost for big data

For structured, heterogenous data, gradient boosting is the way to go.

For all of the hoo-ha about deep learning, the most widely used machine learning algorithm is either logistic regression or gradient boosted decision trees. Gradient boosting is a method whereby you iteratively fit simple models to your data (typically shallow trees), but weight each iteration based on the errors of the previous iteration. It tends to produce good prediction in medium to large datasets.

This paper reviews [Catboost](https://catboost.ai/) which, alongside [Xgboost](https://xgboost.readthedocs.io/en/latest/) and [LightGBM](https://lightgbm.readthedocs.io/en/latest/), is one of the most popular gradient boosting implementations. It is particularly well suited to categorical data (hence the name) and doesn't work well with homogenous numeric data like images. The paper compares implementation and describes application in fields such as psychology, transport and chemistry.

[📖 Read more here (22,655 words)📖](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00369-8)


---

