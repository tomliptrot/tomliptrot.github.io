---
date: 2020-08-02 21:00:00
image_url: null
layout: post
link: https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
story_number: 4
title: "How to build RESTful APIs"
---

A REST API is a common method for interacting with a computer program over the internet. REST (short for representational state transfer) is a set of guidelines and principles for creating Web services.

[This](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api) is the clearest guide to building good REST APIs that I have found. It provides a set of practical guidelines that are easy to follow.

> RESTful principles provide strategies to handle [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) actions using HTTP methods mapped as follows:
>    - GET /tickets - Retrieves a list of tickets
>    - GET /tickets/12 - Retrieves a specific ticket
> - POST /tickets - Creates a new ticket
> - PUT /tickets/12 - Updates ticket #12
> - PATCH /tickets/12 - Partially updates ticket #12
> - DELETE /tickets/12 - Deletes ticket #12
>
> The great thing about REST is that you're leveraging existing HTTP methods to implement significant functionality on just a single /tickets endpoint. There are no method naming conventions to follow and the URL structure is clean & clear. *REST FTW!*

Increasingly, the output of a data science or AI project is a cloud based API. A user will enter some data and a model will return a prediction or label. I have been building various machine learning APIs for years and calling them REST APIs. It turns out they weren't! After reading this, they will be.

