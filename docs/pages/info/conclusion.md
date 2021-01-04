---
# This top area is to give jekyll information about the page.
layout: page
permalink: /info/conclusion/
title: Conclusion
hero_height: is-low
subtitle: A conclusion of the project and the Tech-Stack
---


| Technology 	| Documentation 	| Installation 	| Usability 	| Accuracy/Usefulness 	| Recommendation   	|
|------------	|---------------	|--------------	|-----------	|---------------------	|------------------	|
| Precise    	| good          	| easy         	| good      	| ok                  	| yes (restricted) 	|
| Kaldi      	| good          	| tricky       	| good      	| good                	| yes (restricted) 	|
| FuzzyWuzzy 	| -             	| very easy    	| good      	| bad                 	| no               	|
| MaryTTS    	| good          	| ok           	| ok        	| understandable      	| yes              	|
| HermesMQTT 	| good          	| -            	| good      	| full control        	| yes              	|


## MyCroft-Precise

Mycroft-Precise is well [documented](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/precise) and easy to install.  
You should not install it on your Raspberry Pi, but on a more powerful computer due to its performance and storage size.  
The training is easy and the model is easy to use, but you have to invest some time to find a good wake-word.  
You should install a tool to filter background sounds to increase the accuracy.  
It is not possible to activate our voice assistant, while music is playing.  
  
**Yes**, we would **recommend** it under these **restrictions**!

## Kaldi

The [documentation](https://kaldi-asr.org/doc/) of Kaldi is not very appealing, but extensive.  
It is a bit tricky to install, but doable if you attentively and patiently follow the instructions.  
After you installed it, it is very precise and fast.  
It comes with a pretty well pre-trained base-directory, which is easy to extend.   
In our case it was not possible to detect words, that are not stored in the `sentences.ini` of Rhasspy.  
So it is not possible to add a "searching"-functionality to use sites like "[Wikipedia](https://www.wikipedia.de/)".

**Yes**, we would **recommend** it under these **restrictions**!

## FuzzyWuzzy

FuzzyWuzzy is a pretty simple tool.  
You do not really have to install anything, you can simply select it in Rhasspy.  
It is very limited in the amount of intents and sentences it can process and the spoken Sentences should match these.  
Even if there is not a big amount of sentences it had some issues to recognise the right intents.  

**No**, we would **not recommend** it!

## MaryTTS

The installation of MaryTTS was a bit confusing due to the multiple tools you can install (e.g. the  ["GUI"-version](https://github.com/marytts/marytts) or the ["Installer"-version](https://github.com/marytts/marytts-installer)).  
To understand, which version is the best for your purposes, you should read the well written [documentation](http://mary.dfki.de/).  
The voice we have chosen was understandable, but had some words with misspelling and some problems with negative numbers.  
These problems are preventable and not really a counterargument.  

**Yes**, we would **recommend** it!

## HermesMQTT

HermesMQTT is easy to use if you know how to work with MQTT and (in our case) Node-Red.  
You do not have to install something, just select it in Rhasspy and use the HermesMQTT-topics to set up your dialogue-manager.  
We used the documentation of [Snips](https://docs.snips.ai/reference/hermes) to learn how to use the topics and it was easy to implement.  
You should use HermesMQTT, if you want to have full control over you voice assistant.  

**Yes**, we would **recommend** it!

## What's next?

[Here](./user-experience.md) you can read how we imagined the user-experience at the beginning.