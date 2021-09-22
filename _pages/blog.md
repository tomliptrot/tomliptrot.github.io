---
layout: page
title: Blog
permalink: /blog/
redirect_to: https://www.ortom.ai/journal
---

<!-- try this https://jekyllrb.com/docs/pagination/ -->
<ul>
  {% for post in site.posts limit:10%}
   <h2 class="post-title p-name" itemprop="name headline">
   <a href="{{ post.url }}">{{ post.title }}</a>
   </h2>
   <p class="post-meta">
      <time class="dt-published" datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        {{ post.date | date: date_format }}
      </time>
      {%- if post.author -%}
        • <span itemprop="author" itemscope itemtype="http://schema.org/Person"><span class="p-author h-card" itemprop="name">{{ post.author }}</span></span>
      {%- endif -%}</p>

    {% if post.image %}
  <img class="post-content img" src="{{ post.image | prepend: site.baseurl }}">
  {% endif %}

  {{ post.excerpt }}
  {% endfor %}
</ul>

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>

### Blogroll
Here are a few blogs I like:
* [R Bloggers](https://www.r-bloggers.com)
* [Statistical Modeling, Causal Inference, and Social Science](https://statmodeling.stat.columbia.edu/)
* [Slate Star Codex](https://slatestarcodex.com/)
