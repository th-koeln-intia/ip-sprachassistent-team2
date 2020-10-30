---
# This top area is to give jekyll information about the page.
layout: default
---
# Documentation

## Introduction

This projekt is part of [INTIA](https://dites.web.th-koeln.de/forschung/projekte/research-projects-intia/).

The aim of project is to improve possibilities of digital participation for clients of social work organisations and other
institutions.   

To achieve this goal we want to develop a private and local Voice Assistant. The user should be able to control lights and 
other Internet of Things (IoT) devices locally without internet access, as well as search for information on wikipedia.
On top of this the user should be able to ask for the time and set alarms. If there are use cases which require internet 
access e.g. playing music or getting a weather report, we want no personal information to be send to external servers.

For our voice assistant we want to use the Raspberry Pi and multiple open source software packages.


## How to get started
### Used hardware
- Raspberry Pi 3 B or better
- Power supply according to your Raspberry Pi
- 32 GB SD card or bigger
- Microphone (USB or compatible with the 40 Pin Header of the Pi)

### Used software
- Wake word engine: [MyCroft-Precise](./pages/mycroft.md)
- Speech to Text: [Kaldi](./pages/kaldi.md)
- Intent Recognition: [Rasa NLU](pages/rasanlu.md)
- Text to Speech: [MaryTTS](./pages/marytts.md) 
- Dialogue Management: [Hermes MQTT](./pages/hermesmqtt.md)

### Other important technologies 
- Protocol for massage management: [MQTT](./pages/mqtt.md) 
- Graphical development engine: [Node-Red](./pages/node-red.md)

### First use
- To see what to do at the first use and what we decided to go with, please look [here](./pages/first-use.md).

## Epics
- These are the use cases which we want to implement:
- As user, I want to give the voice assistant commands in natural language (Speech-To-Text)
- [As user, I want to control lighting bulbs with the command "Licht an"/"Licht aus" (Intent recognition)](pages/epics/lights.md)
- As user, I want to set an alarm
- As user, I want to set a timer
- As user, I want to ask for information on wikipedia
- As user, I want to play music over Spotify

## Other

[Wake word engine comparison](pages/wake-word-engine-comparrison.md)

## Sources
- You can find a list of our sources [here](./pages/source-links.md)

