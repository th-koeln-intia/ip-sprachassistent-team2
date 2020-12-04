---
# This top area is to give jekyll information about the page.
layout: page
permalink: /dev/setup/
title: Setup for developers
---

## Setup with iso image

Please reference the [setup guide for users](../users/setup.md)

## Setup fresh

### Download raspberry image and install on SD card

You will probably need a 32 GB SD card if you want to train your own [wake word model](../tech-stack/mycroft.md) in precise.
We recommend to download and install the full verion with Graphical User Interface. Using the lightversion leeds to 
many compatibility issues and you might need to install a lot of software, which is already included in the full version.
https://www.raspberrypi.org/downloads/

### Enable SSH and WIFI

After you installing the image on your SD card you can enable `SSH` by creating a file with the name SSH and no fileextention.

You can make your pi connect to WIFI automaticly by creating a file named `wpa_supplicant.conf` in the `boot` directory.
It has to have the following content:

```
country=DE                              # You can change your countrycode here.
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="intia"                        # Enter your wifi network name here.
    psk="Bunteslicht10"                 # Enter your wifi password here.
    key_mgmt=WPA-PSK                    # It is recommended to use "" around your values to prevent erors with spaces.
}
```

### Connect to your Raspberry

After inserting the SD card and booting the Pi you can ssh after a little while. You will need your Pi's IP-Address to
connect with via a SSH tool like Putty. You can find it in your routers web-interface. 

Default user is `pi` and the password is `raspberry`.

First we want to run these commands and reboot:

```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

### Install Pip and Git if you have used the light version

After rebooting you can install pip and git:

```
sudo apt install python3-pip
sudo apt install git
```

### Install Respeaker Microphone Array

To install the Microphone array you can follow the guide on [seeedstudio.com](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/)
Installing the LED drivers is optional.

```
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh --compat-kernel
reboot
```

This can take more than 10 minutes.

`sudo nano /etc/asound.conf`

Comment out all of the "pcm.!default" and below ad :


```
pcm.!default {
type pulse
# If defaults.namehint.showall is set to off in alsa.conf, then this is
# necessary to make this pcm show up in the list returned by
# snd_device_name_hint or aplay -L
hint.description "Default Audio Device"
}
ctl.!default {
type pulse
}
```

Now change the audio output and activate the SPI.

```
sudo raspi-config
# Select 7 Advanced Options
# Select A4 Audio
# Select 1 Force 3.5mm ('headphone') jack
# Select 5 Interfacing Options
# Select P4 SPI
# <Yes>
# Select Finish
```

### Install Mosquitto and Node-Red

[Node-Red installaton](https://nodered.org/docs/getting-started/raspberrypi)

```
sudo apt-get install mosquitto mosquitto-clients -y
sudo apt install build-essential git  # This fixed a Problem running the script in the next line.
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-andnodered)
sudo systemctl enable nodered.service # This starts Node-Red when the pi is booting.
```

You can enter Node-Red under http://<hostname>:1880



























































