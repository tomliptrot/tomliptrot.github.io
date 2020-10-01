## 1. Machine learning engineering book

A new book has been published about building machine learning systems.

Machine Learning Engineering by Andriy Burkov, is a complete guide to building, testing, deploying and maintaining machine learning models in real world settings. Very kindly the book is made available on a "read first, buy later" basis. I'm currently working my way though it but so far have been really impressed. This is a rapidly evolving field and one that has yet to establish many best practices or standardised approaches. I've done quite a lot of work in this areas and everything I've read so far i've either agreed with, or it has been useful information for me.

Rather than focusing on specific algorithms or packages, the book looks at ways of solving problems. It also includes practical code snippets in both R and Python. I think this is a really useful contribution to the field.

[📖 Read more here 📖](http://www.mlebook.com/wiki/doku.php)


## 2. Making language models more efficient

In the last few years, transformer based language models like GPT-3, Bert and others have revolutionised natural language processing.  Here is how to make them more efficient.

The predictive text function on your mobile phone is a type of language model. Recent advances and massive amounts of compute and data have made modifed versions of these good at a range of tasks. They can do tasks like question answering, translation and language generation at near human levels. However, a big drawback is that the cutting edge approaches are too big and slow to use. GPT-3 has 175 Billion parameters and is too large to run on all but the most expensive supercomputers.

This paper is a survey of the huge amount of research that has gone into making these model more efficient. It provides a taxonomy for understanding the literature and an overview of the most promising approaches.

[📖 Read more here (10,903 words)📖](https://www.arxiv-vanity.com/papers/2009.06732/)


## 3. How much computation does a brain need?

How much computation does a brain use? According to a new estimate its about  10<sup>14 </sup> - 10<sup>17 </sup>FLOP/s.  

A FLOP is a 'Floating Point Operation' (basically adding subtracting, dividing or multiplying two numbers). Doing lots of these per second is a good way of measuring computing power, and can (arguably) be a good way of measuring brain power.

For reference an iPhone can produce ~10<sup>10 </sup>FLOP/s and an Nvidia V100 GPU (costing $10,000)  about ~10<sup>14 </sup>FLOP/s. So according to this, a brain could be made using somewhere between 1 and 1,000 GPUs, or a million iPhones. As this article admits, that would also depend on working out the software, data and architecture.

I'm not sure how accurate this is, but its an interesting exercise -  a bit like one of those 'how many piano tuners are there in Birmingham' type interview questions. The latest language models are pushing these limits of computational power, but whether they are doing anything quite like a human brain is an open question.

[📖 Read more here (9,494 words)📖](https://www.openphilanthropy.org/blog/new-report-brain-computation)


## 4. DuckDB - a lightweight analytics database

DuckDB is a new lightweight database, designed to support data science.

The new system has been built by a research group in the Netherlands. It is columnar, which means it is optimised for selecting data from an entire column and doing operations on it. This is in contrast to most standard SQL engines (Postgres, Mysql etc) which are optimised for selecting a single row. This feature makes it perfectly suited to data science and machine learning tasks.

It is also embedded, which means installing its is as easy as running `pip install duckdb`. No need for messing around on dedicated servers. This makes prototyping and developing quick and easy. I've been looking for something like this for a while for supporting applications that use machine learning.

Here is a little code snippet that shows how to make a table from a `.csv` file.

```python
import duckdb
con = duckdb.connect(database='test.db', read_only=False)
con.execute("CREATE TABLE test AS SELECT * FROM read_csv_auto('test.csv');")
con.execute("SELECT * FROM test;")
print(con.fetchall())
```

If you are looking for a database to support your ML project, give it a go.

[📖 Read more here 📖](https://duckdb.org/)


## 5. Neil Ferguson on modelling Covid-19

Prof Neil Ferguson ('Professor Lockdown') gives an overview of his life in science. 

Understandably it focuses on his involvement in modelling Covid-19. It's a really interesting interview, giving insights into how decisions were made and how the SAGE meetings work. He's very sure of himself, and it is clear why he has been so influential. He has some regret about inviting his girlfriend over during lockdown - but not much.

He has a couple of interesting insights into new research on the virus. Specifically: 

- People who are fully asymptotic are not at all infectious.  
- Immunity is not permanent - it lasts few months and decays away.

Worth a listen to hear from a central figure in the Covid crisis give his take on events and 'the science'.

[📖 Read more here 📖](https://www.bbc.co.uk/programmes/m000mt0h)
