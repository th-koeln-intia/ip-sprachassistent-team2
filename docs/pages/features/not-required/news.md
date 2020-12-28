---
# This top area is to give jekyll information about the page.
layout: page
permalink: /epics/news/
title: News
---

## Goals
Our main goal was to be able to ask Heimdall for the news.  
He should be able to:
- read some headlines
- give us more information about specific headlines

## Rhasspy
In Rhasspy we have to add new lines to the `sentences.ini`:

```textmate
[News]
lies mir die nachrichten vor
was gibt es für neue nachrichten
was gibt es neues

[NextNews]
weiter
zur nächsten nachricht

[MoreNews]
mehr
ich hätte gerne mehr (infos | informationen)
```

#### Example sentences
Some example sentences are:
```textmate

```

## Node-Red

We decided to use the RSS-Feed of the "[Tagesschau](https://www.tagesschau.de/xml/rss2_https/)".