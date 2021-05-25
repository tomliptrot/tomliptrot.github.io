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

The current go-to tool for this kind of thing, Airflow,  was first developed by Airbnb. It is a bit tricky to set up and use. Dagster is a replacement. Dagster recently [wrote](https://dagster.io/blog/dagster-airflow) an article about why it's way better than Airflow. Another alternative is Prefect, which also [claims](https://docs.prefect.io/core/getting_started/why-not-airflow.html) to be better than Airflow. I've used Prefect and Airflow, and I preferred Prefect. Maybe Dagster is even better?

🛎️ **Why this matters:** Better than Airflow. Remember cron? How many task schedulers do we need?