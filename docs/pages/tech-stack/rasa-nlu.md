---
# This top area is to give jekyll information about the page.
layout: page
permalink: /info/rasa-nlu/
title: Rasa-NLU
hero_height: is-low
---

# What was our problem with Rasa?

We tried to use Rasa as our intent-recognition.  
As we are looking at the documentation of Rhasspy, it says we should run a single docker command, add a few lines to our ``profile.json`` and we would be ready to go.
That was not the case.  
When we start Rhasspy with our profile (after we started our Rasa-server), it shows the log-message that Rhasspy cannot find the command: ``rhasspy-rasa-nlu-hermes``, which should be located at: ``/usr/lib/rhasspy/bin/``.

````textmate
2020-10-14 16:44:54,856 INFO spawnerr: can't find command 'rhasspy-rasa-nlu-hermes'
2020-10-14 16:44:57,861 INFO spawnerr: can't find command 'rhasspy-rasa-nlu-hermes'
2020-10-14 16:44:57,861 INFO gave up: intent_recognition entered FATAL state, too many start retries too quickly
````

# Is there a solution for this problem?

We installed Rhasspy via the [rhasspy_2.5.6_armhf.deb](https://github.com/rhasspy/rhasspy/releases) and the previous version: [rhasspy_2.5_armhf.deb](https://github.com/rhasspy/rhasspy/releases).  
Both of these versions had the same problem.  
So we decided to use "FuzzyWuzzy" as our intent-recognition, but our instructions to install Rasa and to train a model will stay [here](../unused/rasanlu.md).  
