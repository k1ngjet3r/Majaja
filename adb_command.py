import os, time

def online():
    os.system('adb shell "svc wifi enable"')
def offline():
    os.system('adb shell "svc wifi disable"')

def sign_in():
    os.system('adb shell input tap 0 600')
    os.system('adb shell input tap 1850 200')
    os.system('adb shell input tap 700 500')
    time.sleep(6)
    os.system('adb shell input tap 700 700')
    time.sleep(6)
    os.system('adb shell input tap 700 550')
    time.sleep(3)
    os.system('adb shell input text "gm.testing.phone"')
    os.system('adb shell input tap 1850 200')
    time.sleep(6)
    os.system('adb shell input text "2019Go1101"')
    os.system('adb shell input tap 1850 200')
    time.sleep(6)
    os.system('adb shell input tap 1850 200')

def sign_out():
    os.system('adb shell input tap 0 600')
    os.system('adb shell input tap 1850 200')
    os.system('adb shell input tap 600 700')


