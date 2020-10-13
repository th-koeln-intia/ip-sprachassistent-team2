# Setup

## Setup with iso image

## Setup fresh

### Download raspberry image and install on SD card

You will probably need a 32 GB SD card if you want to train your own [wake word model](./pages/mycroft.md) in precise.

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

### Uninstall Python 2.7

We want to uninstall the preinstalled Python to prevent future version interference. You can copy text from your clip
board into Putty by right clicking in the Putty window.

Check your Python version: 

```
Python --version
```

Now you can remove your Python. If 2.7 is not your version you need to type your version in the command line.

```
sudo apt-get remove python2.7
```

### Install Pip and Git 

First we want to run these commands and reboot:

```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

After rebooting you can install pip and git:

```
sudo apt install python3-pip
sudo apt install git
```

### Install Respeaker Microphone Array

To install the Microphone array you can follow the guide on [seeedstudio.com](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/)
Installing the LED drivers is optional.
