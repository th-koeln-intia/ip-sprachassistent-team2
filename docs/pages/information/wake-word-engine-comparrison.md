---
# This top area is to give jekyll information about the page.
layout: single
---

# Wake Word Engine

For our project we need a Wake-Word or Hot Word Engine, which is local and always listens 
for the user to start all the other processes.

## Criteria

Since the finished product is supposed to be used by probably vulnerable individuals in charity organisations, we need 
to consider following criteria:
-	Local and private
-	Open source and free to use
-	Supported by a bigger community or company

Furthermore, it would be nice if its easy to use and we could monetize the product, because we cannot limit the use to 
charity.


## Options

There are several possible engines which are the following:
- Precise by Mycroft
- Pocketsphinx 
- Porcupine
- Raven
- Snips
- Snowboy

### precise by mycroft

Available on Github under the Apache 2.0 license. It is maintained by Mycroft AI Inc Kansas City, who sell AI assistant
 hardware with their software and merchandise to support them self’s. It is possible to train custom wake words as 
 documented [here]( https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#how-to-train-your-own-wake-word).

### pocketsphinx by Carnegie Mellon University

Pocketsphinx is available on github and is meant for use on mobile and desktop devices. It is maintained by a team of 
Carnegie Mellon University and partially funded by the Defense Advanced Research Projects Agency and National Science 
Foundation and the CMU Sphinx Speech Consortium. Team one already uses it for their speech recognition.

### Porcupine by Picovoice

Porcupine is open-source and available on [github](https://github.com/Picovoice/porcupine) under the Apache 2.0 license. 
Training custom wake words is restricted to x86_64 CPU architecture. 

### Rhasspy Wake Raven

Raven is available on [github](https://github.com/rhasspy/rhasspy-wake-raven) under the MIT license. It is mainly based 
on the Snips engine and allows for custom wake words. There are two people maintaining the repository, who are also 
responsible for the Rhasspy Assistant. Its also used by the first team as wake word engine. 

### Snips

Snipes is available on [github](https://github.com/snipsco/snips-record-personal-hotword) under the Apache 2.0 license. 
The last push was 14 months ago. It seems like it does not  get any support anymore. It is the base for Raven.

### Snowboy by Kitt-AI

Snowboy will be discontinued at Dec. 31st, 2020 as stated in the [readme.md on github](https://github.com/Kitt-AI/snowboy#readme)
On one hand it is widely used and might get good Community support, on the other hand the developers stated "The field 
of artificial intelligence is moving rapidly. As much as we like our products, we still see that they are getting 
outdated and are becoming difficult to maintain."

## Conclusion

Since all the above are open-source wake word engines and seem to run locally which also ensures privacy, we should
decide on the engine with the best support. Snowboy and Snips are EOL or don't get much support. Porcupine requires
a paid license for our use case. Raven and Pocketsphinx already get used by our other team, which only leaves us 
Precise.
