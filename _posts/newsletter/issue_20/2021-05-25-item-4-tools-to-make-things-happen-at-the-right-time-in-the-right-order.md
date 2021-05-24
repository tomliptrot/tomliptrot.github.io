---
category: mlops
date: 2021-05-25 08:30:00
image: /assets/images/newsletter/issue_20/1024px-Drag_Race_-_2019241185431_2019-08-29_Werner_Rennen_-_1281_-_AK8I8316.jpeg
layout: post
link: https://dagster.io/blog/dagster-airflow
story_number: 4
title: Tools to make things happen at the right time in the right order
word_count: 4,116
---

Making things happen at the right time in the right order is much harder than it ought to be. Dagster is the latest attempt to make it easier.

A DAG is a Directed Acyclic Graph, a fancy name for a sequence of tasks that depend on each other. These types of jobs are the bread and butter of MLOps, controlling data pipelines, transformations and prediction jobs.

The current goto tool for this kind of thing, Airflow,  was first developed by Airbnb. It is a bit tricky to set up and use. Dagster is a replacement. They recently [wrote](https://dagster.io/blog/dagster-airflow) an article about why they're way was better than Airflow. Another alternative is prefect which also [claims](https://docs.prefect.io/core/getting_started/why-not-airflow.html) to be better than Airflow.

🛎️ **Why this matters:** Better than Airflow. Remember cron?

