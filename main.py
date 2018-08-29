import assistant
import speech_recognizer as sp
import text_to_speech as tts

while True:
    assistant.assistant(sp.listen("hey"))
