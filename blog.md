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
