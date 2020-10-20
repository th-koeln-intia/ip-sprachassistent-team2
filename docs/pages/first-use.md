---
# This top area is to give jekyll information about the page.
layout: default
---
# First Use
In this section we want to discuss different possibilities for the user to setup the rhasspy. However, it is important
 to keep in mind, that the range of our users skills and abilities might vastly differ.


### WLAN
- Do we need an internet connection?

Firstly there will probably be some clients, who should not use the Internet unattended and we should ship a Version
with no ability to connect to the internet or provide guidance to caretakers how to disable the internet connection on 
the pi or on the network level. 

Secondly the pi will already have cut capabilities, especially if the GUI is disabled. This way it will be more difficult
 to use the pi in an unintended or even harmful way.

Thirdly we are developing the assistant, because we want to encourage the user to explore, learn, tinker and engage with 
technology. Therefore we would like to keep node red and maybe some other services of the pi accessible to the user.

- How to configure/choose a Wi-Fi network?

https://davesteele.github.io/comitup/

- How to handle updates of the downloaded Wikipedia-Lib.? 

 Cronjob automated updates might break the device
Maybe it is possible to update the pi over git remotely.


### Adding new smart devices
- How to add a new smart device (e.g. a new lamp)?

Maybe we can use [Home Assistant](https://www.home-assistant.io/) to let the user add new devices to the assistant.
Home Assistants mobile app also offers an convinient way to controll the connected smart devices.

- How to add such a device to one or more groups?

Home Assistant supports rooms and groups. 

- Which kinds of device do we want to allow (lamps, thermometers, shutters, sockets)?  

### (Custom Wake-Word?)
- Do we allow modifying or changing the Wake-Word?
- What are the pros and cons?
- How could someone change it? 

### New Commands
- How to define new Commands for specific tasks (e.g. groups of lamps)?
- Do we pre-set a bunch of groups (e.g. living room, kitchen, bedroom)?
- Which functions should be implemented? (Reading data from thermometers, or just switching lights and sockets?)  
