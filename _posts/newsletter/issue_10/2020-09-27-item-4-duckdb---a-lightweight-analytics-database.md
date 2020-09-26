---
date: 2020-09-27 21:00:00
image: /assets/images/joshua-coleman-fXls-tVemno-unsplash.jpg
layout: post
link: https://duckdb.org/
story_number: 4
title: DuckDB - a lightweight analytics database
word_count: null
---

DuckDB is a new lightweight database, designed to support data science.

DuckDB is made by a research group in the Netherlands. It is a columnar database, this means it is optimised for selecting data from an entire column and doing operations on it. This is in contrast to most standard SQL engines (Postges, Mysql etc) which are optimised for selecting for a single row. This makes it perfectly suited to adata science and machine learning tasks.

It is also imbedded, which means installing its is as easy as running `pip install duckdb`. No need for separate installations on dedicated servers. This makes prototyping and developing quick and easy. I've been looking for something like this for a while for supporting applications that use machine learning.

Here is a little code snippet that shows how to make a table from a `.csv` file. It's pretty easy.

```python
import duckdb
con = duckdb.connect(database='test.db', read_only=False)
con.execute("CREATE TABLE test AS SELECT * FROM read_csv_auto('test.csv');")
con.execute("SELECT * FROM test;")
print(con.fetchall())
```

If you are looking for a database to support your project, give it a go.

