---
layout: page
title: Contact
permalink: /contact/
---

<div class="contact-list">
  <li class="p-name">
    {%- if site.author -%}
      {{ site.author | escape }}
    {%- else -%}
      {{ site.title | escape }}
    {%- endif -%}
    </li>
    <li>
    35 Cheltenham Road<li>Manchester<li>M21 9GL
    <br>  <br>
     <br>
    {%- if site.email -%}
    <li><a class="u-email" href="mailto:{{ site.email }}">{{ site.email }}</a></li>
    {%- endif -%}
    {%- if site.tel -%}
    <li><a href="tel:{{ site.tel }}">{{ site.tel }}</a></li>
    {%- endif -%}
