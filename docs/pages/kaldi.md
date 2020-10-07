---
# This top area is to give jekyll informations about the page.
layout: default
---

# Kaldi

## Introduction
Kaldi is a C++ based speech recognition tool. It's licensed under Apache License v2.0.

## Install Kaldi
### Download
Clone the Kaldi repository and move into the folder.
```bash
    git clone https://github.com/kaldi-asr/kaldi.git kaldi --origin upstream
    cd kaldi
```
### Install
To install Kaldi follow the instructions in the INSTALL file.  
It will guide you to the INSTALL files in `kaldi/tools/` and `kaldi/src/`. 
After you followed all these instructions, you can move on with this guide.

## Train a model
### Record samples or ...
Kaldi uses `.wav` files to train a model.
### ... download Tuda
[Tuda](https://github.com/uhh-lt/kaldi-tuda-de)
### Train the model

## Use Kaldi in Rhasspy
#### Update your Rhasspy profile
You need to have Kaldi installed.
To use it in Rhasspy add the following to your profile.
```json
    {
      "speech_to_text": {
        "system": "kaldi",
        "kaldi": {
            "base_dictionary": "base_dictionary.txt",
            "compatible": true,
            "custom_words": "custom_words.txt",
            "dictionary": "dictionary.txt",
            "graph": "graph",
            "kaldi_dir": "/opt/kaldi",
            "language_model": "language_model.txt",
            "model_dir": "model",
            "unknown_words": "unknown_words.txt",
            "language_model_type": "arpa"
        }
      }
    }
```
Set `kaldi_dir` to the directory, where you installed Kaldi in our case `~/kaldi`.
