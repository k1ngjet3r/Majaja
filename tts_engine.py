import pyttsx3, os, time


def activate_ga():
    os.system('adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity')

def tts(query):
    engine = pyttsx3.init()
    engine.setProperty('rate', 105)
    # activate Google Assistant via adb
    activate_ga()
    # wait for 0.8 sec
    time.sleep(0.8)
    # giving the command via speaker
    engine.say(query)
    
    engine.runAndWait()


