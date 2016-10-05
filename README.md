# Samsung's Good Lock Hex to Color
This python program takes in a hex value and then uses Android's ADB interface to pick the correct color from Samsung's Good Lock color picker.

The first and only argument needed is the hex value of the color you want.

Please view the footnotes before you get started.

## Requirements

### Windows  
1. [Samsung's Universal USB Driver for Mobile Phones](http://downloadcenter.samsung.com/content/DR/201602/20160219075034805/SAMSUNG_USB_Driver_for_Mobile_Phones_v1.5.45.00.exe)  
2. [ADB](https://www.androidfilehost.com/?fid=24521665358595410)
3. [Python 3](https://www.python.org/)

### Mac/Linux
1. ADB
2. [Python 3](https://www.python.org/)

## Examples
Your phone should be connected to your computer with a USB cable and USB Debugging should be turned on. Good Lock should be open and opened up to the custom color picker screen with the tile you want to change set as the selected tile.   
You should run this command for each tile you want to change.

`python hex2goodlock.py '#253f3f'`  
`python hex2goodlock.py '#253237'`


## Footnotes
1. The ADB installer for Windows comes from [this thread](http://forum.xda-developers.com/showthread.php?t=2317790)
2. ADB for Mac is included in this repo and the python script with check to see if you have ADB already installed. If not it'll use the included ADB
3. The ADB binary for Mac can also be downloaded using [this guide](http://forum.xda-developers.com/showthread.php?t=1917237)
4. Linux people should install ADB from their package manager. I trust that if you're running linux you know what you're doing and don't want me mucking up your OS
5. Mac and Linux should come with Python and you should not need to install it. To determine if you have python please open Terminal and type `python -V`. If you have Python this should return which python version you have. If you get anything else you don't have python.

### Tested on
* Galaxy S7 Edge from T-Mobile in the condensed display mode using macOS.
* Galaxy S7 from T-Mobile in the condensed display mode using Windows 10.

### Beta Testers
