---
layout: page
title: Blog
permalink: /blog/
---
{% for post in site.posts %}
 <article>
 <time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time> :
     <a href="{{ post.url }}">
       {{ post.title }}
     </a>
 </article>
{% endfor %}
<br>
<br>
<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>

### Blogroll
Here are a few blogs I like:
* [R Bloggers](https://www.r-bloggers.com)
* [Statistical Modeling, Causal Inference, and Social Science](https://statmodeling.stat.columbia.edu/)
* [Slate Star Codex](https://slatestarcodex.com/)
