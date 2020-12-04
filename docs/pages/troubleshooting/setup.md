---
# This top area is to give jekyll information about the page.
layout: page
permalink: /troubleshooting/setup/
title: Setup
---

# What was the main problem at the setup?

When using an image to set up a raspberry pi it can happen, that not all the space on the sd card is allocated.  
This can result in to little hard drive space for all technologies to be installed.  

# What was the solution?

We used the command Line to expand the filesystem:  

With the command `df -h` we can list the filesystem (fs).

![Filesystem after using an image for setup](../../assets/PI-df-h-after-using-image-for-setup.png)

In the first row we can see that the `/dev/root` only takes up 15 GB of space.  
With `sudo raspi-config --expand-rootfs` we expanded the filesystem.  

![Expanding fs](../../assets/Pi-expand-rootfs.png)


![Expanded fs](../../assets/Pi-expanded-file-system.png)

Here we can see that `/dev/root` uses almost all the 32 GB of the SD-Card.

<!--- 
# Solutions that did not work

We used rufus to put an image of a 16 GB SD card on a 32 GB one which resulted in 14,98 GB unformatted space. Now we are 
trying the same with the Raspberry Pi Imager v1.4.  


https://www.easeus.com/partition-master/expand-windows-7-partition.html
https://stackoverflow.com/questions/19355036/how-to-create-an-img-image-of-a-disc-sd-card-without-including-free-space

reformatted the volume on Raspberry Pi SD card with Windows Volumemanager.

Raspberry py boot error:
```bash
Kernel panic-not syncing: VFS: unable to mount root fs on unknown-block(179,6)
```

Following [these instructions](https://raspberrypi.stackexchange.com/questions/40854/kernel-panic-not-syncing-vfs-unable-to-mount-root-fs-on-unknown-block179-6)
--->