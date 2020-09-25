---
date: 2020-09-27 21:00:00
image: /assets/images/joshua-coleman-fXls-tVemno-unsplash.jpg
layout: post
link: https://duckdb.org/
story_number: 4
title: DuckDB - a lightweight analytics database
word_count: null
---

DuckDB is a new embeddable analytics database. A cross between sqlite and redshift. 

 It is a columnar data base, this means it is optimised for selecting data from an entire column and doing operations on them. This is in contrast to most standard SQL engines (Postges, mysql etc) which are optimised for selecting for a single row. It is also imbedded, this means installing its is as easy as running `pip install duckdb`. No need for operate inhalations on dedicated servers. This makes plotting and developing quick and easy. I've been looking for something like this for a while for supporting applications that use machine learning.

Here is a little code snippet that shows how to make a table from a .csv file. It's pretty easy.

```python
import duckdb
con = duckdb.connect(database='test.db', read_only=False)
con.execute("CREATE TABLE test AS SELECT * FROM read_csv_auto('test.csv');")
con.execute("SELECT * FROM test;")
print(con.fetchall())
```

It is an open source project being run by academics in the Netherlands, if you are looking for a database to support an analytics project, give it a go.

