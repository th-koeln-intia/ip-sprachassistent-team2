---
# This top area is to give jekyll information about the page.
layout: page
permalink: /tech-stack/marytts/
title: MaryTTS  
hero_height: is-low  
subtitle: Text to Speech
---

## Introduction

MaryTTS is a java-based open-source text to speech system.  
It was developed by the [German Research Center for Artificial Intelligence](https://www.dfki.de/web/) and the [University of Saarland](https://www.uni-saarland.de/start.html).  
In our case we use the [MaryTTS-Installer](https://github.com/marytts/marytts-installer) to both install new languages **and** run the server,  
because we were unable to install new languages with the [Installer-GUI](https://github.com/marytts/marytts#downloading-and-installing-voices) due to our missing video output.  

## Install MaryTTS
### Download
Download the [MaryTTS-Installer](https://github.com/marytts/marytts-installer/releases) and unzip it.  
Go to the directory, where you downloaded it and install a language:  

```bash
    cd marytts-installer-5.2/
    ./marytts install voice-bits3-hsmm
```

*`bits3-hsmm` is a german male voice, you can try any voices [here](http://mary.dfki.de:59125/).*  

To run your server you just need to type `./marytts` in the same directory.  
The server will be available at `http://localhost:59125/`.  

### Run MaryTTS as a service
We created a service to start the MaryTTS server at boot up.  
To do so, type `sudo nano /etc/systemd/system/marytts.service` in the console and copy the following lines:  

```
    # Make sure to change ExecStart, WorkingDirectory
    # and Environment to the path, where you installed marytts

    [Unit]
    Description=MaryTTS
    
    [Service]
    WorkingDirectory=/home/pi/marytts-installer-5.2/
    ExecStart=/home/pi/marytts-installer-5.2/marytts
    Environment=GOPATH=/home/pi/marytts-installer-5.2
    Restart=always
    RestartSec=5
    TimeoutSec=10
    
    [Install]
    WantedBy=multi-user.target
```

Save and close the file.  
Enable and start the service by typing:  

```
    sudo systemctl enable marytts.service
    sudo systemctl start marytts.service
```
  
  

## Use MaryTTS in Rhasspy

For MaryTTS you need to have `OPENSSL_1_1_1` installed.  
To see how to do this, look at our troubleshooting-section for [OpenSSL](../info/openssl.md).  

### Update your profile

Go to your Rhasspy-profile or the webinterface and add the following lines:

```json
{
  "text_to_speech": {
      "marytts": {
          "locale": "de",
          "voice": "bits3-hsmm"
      },
      "system": "marytts"
  }
}
```

*Make sure to change `"locale"` and `"voice"` to any voice you installed.*

### Test MaryTTS

Now you should be able to test MaryTTS by typing any word or sentence in the input-field of the webinterface.  
By pressing the "Speak"-button you should be able to hear the spoken text through your selected "Audio Playing"-service, in our case `aplay` (3.5mm-headphonejack).  
  
![MaryTTS-Test](../../assets/MaryTTS-Test.png)

### Call TTS from Node-Red

To see how we use Node-Red to interact with MaryTTS, click [here](./hermesmqtt.md#tts).

## Sources
[MaryTTS-Documentation](http://mary.dfki.de/)  
[DFKI](https://www.dfki.de/web/)  
[Universität des Saarlands](https://www.uni-saarland.de/start.html)

## What's next?

If you do not want to use Rhasspy's own dialogue manager you can use [HermesMQTT](./hermesmqtt.md).