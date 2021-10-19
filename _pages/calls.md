---
title: Calls
layout: archive
permalink: /calls/
author_profile: false
sidebar: false
read_time: false
share: true
comments: false
---

<ul>
{% for call in site.pages %}
    {% if call.path contains 'calls/' %}
        <li><a href="{{ call.path | replace: '_pages/calls/', ' ' | replace: '.md', ' ' }}">{{ call.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>

