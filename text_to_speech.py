import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Volume = 50

def say(text_to_speak):
    speak.Speak(text_to_speak)