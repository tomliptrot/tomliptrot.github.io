---
category: mlops
date: 2021-06-22 08:30:00
image: /assets/images/newsletter/issue_21/iqram-o-dowla-shawon-Wk2to7RYKHo-unsplash.jpeg
layout: post
link: https://docs.getdbt.com/docs/introduction/
story_number: 3
title: Easy data transformation with dbt
word_count: 2,061
---

Data Build Tool (dbt) is a tool that allows easy data transformations.

I keep hearing about [dbt](https://docs.getdbt.com/docs/introduction/) from various people but hadn't really understood what it did. It basically allows you to transform data that is already in a data warehouse using simple select statements. It's the T in ELT (Extract, Transform, Load).

A dbt project is made up of .sql files each with a single select statement. When you run dbt it will build a view in your data warehouse based on the select statement. It takes care of all the boilerplate and ordering of excution. Dbt comes with [connectors](https://docs.getdbt.com/docs/available-adapters) for all the main data warehouses.

🛎️ **Why this matters:** This tool allows anybody who can write select statements to transform data.