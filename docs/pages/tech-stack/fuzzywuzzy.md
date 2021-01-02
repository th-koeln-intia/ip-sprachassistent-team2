---
# This top area is to give jekyll information about the page.
layout: page
permalink: /tech-stack/fuzzywuzzy/
title: FuzzyWuzzy
hero_height: is-low
---

## Introduction

FuzzyWuzzy is an intent recognition system, that uses the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) to compare a given input to preset intent sentences.   
It works best with a small amount of sentences.  

## Levenshtein distance

The Levenshtein distance describes the minimal count of characters you have to change, to transform a word into another.  
In the following example the levenshtein distance is 3.  
You have to change 3 characters from "Apples" to "Maple":  

1. Ap**p**les -> Aples (erased **p**)  
2. Aples -> **M**aples (added **M**)  
3. Maple**s** -> Maple (erased **s**)  

## Using FuzzyWuzzy in Rhasspy

To use Rhasspy with FuzzyWuzzy, you just have to select it in the settings or add the following to your profile:
  
```json
{
  "intent": {
    "system": "fuzzywuzzy"
  }
}
```
After retraining Rhasspy you should be able to recognise the intents in your `sentences.ini`.

## Sources

[Rhasspy-Documentation](https://rhasspy.readthedocs.io/en/latest/intent-recognition/)

## What's next?

After [Node-Red](./node-red.md) handles the command, [MaryTTS](./marytts.md) will give an audio feedback.