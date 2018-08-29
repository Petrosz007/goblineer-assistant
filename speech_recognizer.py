import speech_recognition as sr
import text_to_speech as tts
import assistant
import sys
from pocketsphinx import LiveSpeech
import winsound



r = sr.Recognizer()
mic = sr.Microphone()

def get_command(fail_counter):
    with mic as source:
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        print("Ready...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("Command: " + command)

    #Try until it gets a recognisabe command
    except sr.UnknownValueError:
        print("Unable to recognise command.")
        # if fail_counter < 2:
        #     command = get_command(fail_counter + 1)
        # else:
        return "no command"

    return command

def listen(keyword):
    speech = LiveSpeech(lm=False, keyphrase=keyword, kws_threshold=100)
    for phrase in speech:
        return get_command(0)
