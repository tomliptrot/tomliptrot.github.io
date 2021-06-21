## 1. Don't use deep learning for tabular data

![Don't use deep learning for tabular data](https://ortom.co.uk/assets/images/newsletter/issue_21/nick-fewings-dRCQJZoTYCc-unsplash.jpeg)

Most business data is tabular (think Excel or SQL type data), and deep learning is generally not the tool for modelling it.

I think people already know this, but it's good to hear it again. A new [paper](https://www.arxiv-vanity.com/papers/2106.03253/) shows that XGboost tends to beat DNNs for tabular data. Deep-learning is great, but its not the solution for most problems with data seen in businesses today. If you have images, languages or sound the deep neural networks designed to deal with these are often very effective. But when you have rows and columns made up of a mixture of continuous and categorical data, XGBoost is probably a better bet.

> "Our study shows that XGBoost outperforms these deep models across the datasets, including datasets used in the papers that proposed the deep models. We also demonstrate that XGBoost requires much less tuning."

🛎️ **Why this matters:** Tabular data still rules in most businesses. Use the right tool for the job.

[📖 Read more (4,445 words)📖](https://www.arxiv-vanity.com/papers/2106.03253/)


---

## 2. The 5 types of reccomender system

![The 5 types of reccomender system](https://ortom.co.uk/assets/images/newsletter/issue_21/peter-bond-KfvknMhkmw0-unsplash.jpeg)

Personalisation and recommendation are one of the most most effective applications of machine learning. 

Eugene Yan has written a really useful [review](https://eugeneyan.com/writing/patterns-for-personalization/) of some of the main approaches. He splits them into 5 groups:

➡ Embeddings+MLP: A good simple starting point

➡ Bandits: A way to balance exploration and exploitation

➡ Sequential: If you've got long user histories

➡ Graphs: Not much behaviour data but lots of item/user metadata

➡ User models: Generic embedding for multiple problem.

🛎️ **Why this matters:** There has been a lot of developments in this field here is a really useful map.

[📖 Read more (5,207 words)📖](https://eugeneyan.com/writing/patterns-for-personalization/)


---

## 3. Easy data transformation with dbt

![Easy data transformation with dbt](https://ortom.co.uk/assets/images/newsletter/issue_21/iqram-o-dowla-shawon-Wk2to7RYKHo-unsplash.jpeg)

Data Build Tool (dbt) is a tool that allows easy data transformations.

I keep hearing about [dbt](https://docs.getdbt.com/docs/introduction/) from various people but hadn't really understood what it did. It basically allows you to transform data that is already in a data warehouse using simple select statements. It's the T in ELT (Extract, Transform, Load).

A dbt project is made up of .sql files each with a single select statement. When you run dbt it will build a view in your data warehouse based on the select statement. It takes care of all the boilerplate and ordering of excution. Dbt comes with [connectors](https://docs.getdbt.com/docs/available-adapters) for all the main data warehouses.

🛎️ **Why this matters:** This tool allows anybody who can write select statements to transform data.

[📖 Read more (2,061 words)📖](https://docs.getdbt.com/docs/introduction/)


---

## 4. Do algorithms dream of simulated data?

![Do algorithms dream of simulated data?](https://ortom.co.uk/assets/images/newsletter/issue_21/andrea-lightfoot-Pj6fYNRzRT0-unsplash.jpeg)

Dreams are a way to stop the brain overfitting, according to a new theory.

Overfitting is a concept in machine learning where a model works well on a training dataset but fails to generalise to new applications. This is often seen when a model performs very well on a training set but less well on a test set. Many approaches have been taken to reduce overfitting including weight regularisation, dropout,  noise addition and early stopping. These are part of the standard ML toolkit.

A new [paper](https://www.arxiv-vanity.com/papers/2007.09560/) proposes that the purpose of dreaming in humans and other animals is too stop the brain from overfitting - this is know as the Overfitted Brain Hypothesis. Dreams effectively generate data outside of our usual training set to push the limits of our perceptual models.

🛎️ **Why this matters:** It's a nice theory.

[📖 Read more (12,835 words)📖](https://www.arxiv-vanity.com/papers/2007.09560/)


---

## 5. Open super big language model

![Open super big language model](https://ortom.co.uk/assets/images/newsletter/issue_21/david-clode-Q-8jreAEa-4-unsplash.jpeg)

A new, open, alternative to the super big language model GPT-3 has been released. It wrote the following about itself:

> "rpwlcr = versatile automatic writing – Genesis writing loop based on Peter Overlefsholtz's formula inspired by and derived from MUDCon VoX scribble [Yes; it would be silly for GPT-3 to not even claim that – LD] used for learning to be GPT-3 creator Zihon Rusakowski ; good tools are eternal best biceps ; PrimalScribbler family sed (error recognition and corrective drafting, safe backups); BEGIN UPWARD pointing source prototype literate interpreters ALL MAY READ PROTOTYPE written for aspiring TP. XLIT given-alice paths allowed (eg: Paul Lewis paths; especially handkerchief's application of Katipussi fonts/following sounds to construct Polish apostrophe saving pronoun), even improving usability (Hmmm, N), or paradigm engineering (C, Homolateral exophony ). only practical contemporary POST written in 010, ten seconds – bps · in FRPEH R Q00 xxQ? S9 9993 IRNT AP1ED 15 36 00300 15 O37 B° jí2IMMìGIC à€ c00«JJ©R u é©~ êv "ú_ ®, a"

Hmm - that's not perfect, is it? A sick parrot?

🛎️ **Why this matters:** The singularity is far, but at least it's open.

[📖 Read more 📖](https://6b.eleuther.ai/)


---