---
# This top area is to give jekyll informations about the page.
layout: default
---

# MyCroft-Precise

We decided to go with MyCroft-Precise for the given [reasons](./wake word engine comparison.md) and started to train our Wake-Word: ["WakeWord"](./wake-word.md).
Hereinafter we explain, how we made it and what the difficulties were.

## Basics

MyCroft-Precise uses `.wav` files to train a model, which then can be used by Rhasspy to set up the wake-word.  


## How to Train your own Wake-Word?

First off all search for a word that ...  
This is a shorted version of the original [Documentation](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word).  
After you installed Precise by following [this](https://github.com/MycroftAI/mycroft-precise#source-install) step-by-step instruction, you are able to use `source .venv/bin/activate` to activate the virtual console and the following commands:  
- `precise-collect` to record own `.wav` files
- `precise-train` to train a model with given sound-files initially
- `precise-train-incremental` to reduce false activations at trained model
- `precise-test` to test your model with prerecorded soundfiles
- `precise-listen` to test your model live with a connected microphone (in our case the [ReSpeaker 4-Mic Array](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/))
- `precise-convert` to convert your `.net`-Keras model to a `.pd`-TensorFlow model

#### Recording and training

We recorded some audio samples using the `precise-collect`-command and moved most of these `.wav`-files into the `mycroft-precise/heimdall/wake-word/`-directory and a few into the `mycroft-precise/heimdall/test/wake-word/`-directory.  
We collected some files recorded by our friends and family, too.  
After we sorted all recorded samples into the right directories, we started the training using the `precise-train`-command.  
```bash
    precise-collect
    precise-train -e 60 heimdall.net heimdall/
```

#### Testing and improving

After the first training we tested our model using the `precise-listen`-command and noticed, that there are many false detections.
```bash
    precise-listen heimdall.net
```
To reduce these false reactions we downloaded the [Public Domain Sounds Backup](http://pdsounds.tuxfamily.org/) as recommended in the original Precise [documentation](https://github.com/MycroftAI/mycroft-precise/wiki/Training-your-own-wake-word#Method-2).
To do this, we downloaded the package to the `data/random`-directory and unzipped it.
```bash
    cd data/random
    wget http://downloads.tuxfamily.org/pdsounds/pdsounds_march2009.7z
    7z x pdsounds_march2009.7z
    cd ../..
```
To convert all these downloaded `.mp3`-files to the needed `.wav`-format we used the following script:
```bash
    SOURCE_DIR=data/random/mp3
    DEST_DIR=data/random
    
    for i in $SOURCE_DIR/*.mp3; do echo "Converting $i..."; fn=${i##*/}; ffmpeg -i "$i" -acodec pcm_s16le -ar 16000 -ac 1 -f wav "$DEST_DIR/${fn%.*}.wav"; done
```
Now we had the all files in the right format and were able to train the model again.
To do so, we used the `precise-train-incremental`-command, which takes clips from the `data/random`-directory copied these to the `heimdall/not-wake-word`-directory and retrained the model.
This process lasts a few hours on the raspberry pi 3B+.
```bash
    precise-train-incremental heimdall.net heimdall/ -r data/random/
```
(directories can be different to your setup)

You can repeat this whole process until you are happy with the result of the wake-word-detection

#### Use your model in Rhasspy

Before you can use your model with Rhasspy you need to convert it from the Keras `.net`-format to the TensorFlow `.pb`-format.
We have used the `precise-convert`-command to do so.
```bash
    precise-convert heimdall.net
```
We have got three new files:

- `heimdall.pb`
- `heimdall.pb.params`
- `heimdall.pbtxt`

After we copied all these files to the `rhasspy/profiles/de/precise`-directory, we were able to select and use them in the Rhasspy-GUI on `http://<hostname>:12101`.
