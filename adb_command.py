import os
import time

'''
    This is mainly designed for 10" screen only
    There is currently no program for 13"
'''
def adb_root():
    os.system('adb root')

def online():
    os.system('adb shell "svc wifi enable"')


def offline():
    os.system('adb shell "svc wifi disable"')


def sign_in():
    adb_root()
    # tap Google Maps
    os.system('adb shell input tap 65 420')
    # tap account icon
    os.system('adb shell input tap 1692 144')
    # tap sign in to Google
    os.system('adb shell input tap 920 360')
    time.sleep(6)
    # tap sign in on car
    os.system('adb shell input tap 590 500')
    time.sleep(6)
    # tap username input
    os.system('adb shell input tap 420 400')
    time.sleep(3)
    # enter username
    os.system('adb shell input text "gm.testing.phone"')
    # tap next
    os.system('adb shell input tap 1640 130')
    time.sleep(6)
    # enter password
    os.system('adb shell input text "2019Go1101"')
    # tap next 
    os.system('adb shell input tap 1640 130')
    time.sleep(6)
    # rap done
    os.system('adb shell input tap 1850 200')


def sign_out():
    adb_root()
    os.system('adb shell input tap 0 600')
    os.system('adb shell input tap 1850 200')
    os.system('adb shell input tap 600 700')

def pin_lock():
    adb_root()
    os.system('adb shell locksetting set-pin 0000')

def pw_lock():
    adb_root()
    os.system('adb shell locksetting set-password 0000')

def pattern_lock():
    adb_root()
    os.system('adb shell locksetting set-pattern 14789')
