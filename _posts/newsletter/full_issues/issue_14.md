## 1. Learning like people

Up until recently models learnt using labelled data but humans learnt using language. This is starting to change.

It is starting to become possible to describe tasks using natural language so that the machines can learn. This allows much faster learning using less data. Which is similar to how humans operate. This opens the possibility of interacting with and trading computers in exactly the same way we do with humans. Models like GPT-2 and 3 and BERT have made this possible.

This research is similar to the [PET](https://github.com/timoschick/pet) paper linked to a couple of weeks ago and is a really exciting avenue of research. As the authors say:

> "We envision a future where in order to solve a machine learning task, we no longer have to collect a large labeled dataset, but instead interact naturally and expressively with a model in the same way that humans have interacted with each other for millennia—*through language*."

[📖 Read more here (750 words)📖](http://ai.stanford.edu/blog/learning-from-language/)


---

## 2. Neurips 2020

NeurIPS Thirty-fourth Annual *Conference* on *Neural Information Processing System* takes place next week. This year you can get a ticket (virtually).

Over the last few years NeurIPS has become the hottest academic conference on the planet. In 2018 all of the ticket sold out in 10 minutes and after that they started giving out tickets using a lottery. It features all of the latest and greatest research and application of machine learning and AI.

This year, due to Covid, the conference is taking place virtually and anybody can go (if you want to spend £100 to watch videos/ go on zoom). The conference will use [Gather Town](https://gather.town/) and various other innovations to allow some way for people to meet each other.  I'm going to give it a go. Maybe I'll see you in the 'virtual poster session!' and have a 'virtual awkward exchange'.

[📖 Read more here (996 words)📖](https://neuripsconf.medium.com/introducing-the-neurips-2020-main-program-1c3a3de85226)


---

## 3. scikit-survival: A Library for Time-to-Event Analysis Built on Top of scikit-learn

Almost all we data has some kind of time related element. Often this is ignored.

For example, when looking at customer churn. The event we are interested in is a customer cancelling their subscription. But given our data today we can't know if a given user would continue subscribing for years to come or if they might cancel tomorrow. This is called censoring and is handles using survival analysis.

There is large body of work on how to deal wit this type of data, with origins in medicine (time to death or recurrence) and engineering (time to failure) . Scikit survival makes it easier to handle this type of data using the scikit-learn machine learning library for python.

[📖 Read more here (136 words)📖](https://jmlr.org/papers/v21/20-729.html)


---

## 4. AI for enterprise platforms

There has been lots of recent activity amongst 'AI platform' companies planning IPOs: see Databricks, Data Robot, Domino, Palantir, now C3.ai.

C3.ai provides AI services to large companies.  C3 has worked with Shell, AstraZeneca, conEdison, Koch Industries, Raytheon, and the US Airforce.   The company is focused one a small number of large clients and seems to do a bit of everything for them. Their main customer is  oil and gas service company Baker Hughes. It's not clear from this document what the company competitive advantage is.

>  "As often for AI companies, there is some level of questioning about what part of their activity is actually AI, vs more traditional software, and C3 is no exception. See for example this piece in ZDNet: [Dissecting C3.ai’s secret sauce: less about AI, more about fixing Hadoop](https://www.zdnet.com/article/dissecting-c3-ais-secret-sauce-less-about-ai-more-about-fixing-hadoop/)"

I think a problem for this type of company is that 'AI' is such a loosely defined term that any attempt to build a platform for it leaves to a lack of focus. Often they are trading more on hype that actual outcomes. I'm sure there will be eventual big winners here, but I'm not sure they exist just yet.

[📖 Read more here (1,988 words)📖](https://mattturck.com/c3/)


---

## 5. Vaccine science by press release

AstraZeneca kind of messed up their virus announcement. 

It got one of either 62%, 90% or 70% efficacy. They made a mistake with the dosing of a small number of trial participants and then found that there was a better result in that group. Generally with clinical trials a protocol is pre-regsitred and results are reported against that. Any 'findings' outside of that protocol should be taken with a large pinch of salt. 

AZ only registered one dosage regimen.  Th problem with they type of subgroup analysis that they have done here is that there are many way it can result in spurious results. If you analyse enough subgroups eventually you will fins one where the drug worked better just due to chance. This is OK, and you can control for this, but the results are only valid once they have been confimenbrf thought further trials.

Maybe we shouldn't do science by press release.

[📖 Read more here (2,078 words)📖](https://junkcharts.typepad.com/numbersruleyourworld/2020/11/good-vaccine-news-without-glorifying-faux-precision.html)


---