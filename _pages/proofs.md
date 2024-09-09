---
title: List of Proofs
layout: archive
permalink: /list_of_proofs/ #everything in that url has the contents here
---


{% assign everything = site.geometry | concat: site.trigonometry | concat: site.number_theory | concat: site.algebra | concat: site.probability %}
{% for post in everything %}
  {% include archive-single.html %}
{% endfor %}