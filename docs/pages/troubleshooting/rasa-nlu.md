---
# This top area is to give jekyll information about the page.
layout: single
---

# Troubleshooting Rasa-NLU

We have some problems using Rasa-NLU for the intent-recognition.  
As we are looking at the documentation of Rhasspy, it says we should run a single docker command, add a few lines to our ``profile.json`` and we would be ready to go.  
That was not the case. When we start Rhasspy with our profile (after we started our Rasa-server), it shows the log-message that Rhasspy cannot find the command: ``rhasspy-rasa-nlu-hermes``, which should be located at: ``/usr/lib/rhasspy/bin/``.
For reasons, we do not know Rhasspy does not install this command, even though it is in the repository.
We installed Rhasspy via the [rhasspy_2.5.6_armhf.deb](https://github.com/rhasspy/rhasspy/releases) and the previous version: [rhasspy_2.5_armhf.deb](https://github.com/rhasspy/rhasspy/releases).

````bash
2020-10-14 16:44:54,856 INFO spawnerr: can't find command 'rhasspy-rasa-nlu-hermes'
2020-10-14 16:44:57,861 INFO spawnerr: can't find command 'rhasspy-rasa-nlu-hermes'
2020-10-14 16:44:57,861 INFO gave up: intent_recognition entered FATAL state, too many start retries too quickly
````

We decided to change the intent recognition to "FuzzyWuzzy". The instructions to install Rasa and to train a model will stay [here](../unused/rasanlu.md).