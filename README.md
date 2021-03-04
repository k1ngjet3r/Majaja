# Majaja
## What is Majaja?
An Android-based devices testing aid, which has an ugly GUI and functions such as:
* Wifi control (online/offline)
* Google account sign-in or sign-out
* Create device's user
* Give Google Assistant command
And it also has a space for meme because why not

## Environment Requirment
1. Python 3.6+
2. Pillow module (pip install pillow)

## How Majaja Work?
Most of the functions were directly controlled by sending adb command, however, since we cannot find the direct control for login or out of the google account, adb was used for simulate the tap to login or out the Google account

## Supported Docs
### tk.Listbox()
https://www.tutorialspoint.com/python/tk_listbox.htm
