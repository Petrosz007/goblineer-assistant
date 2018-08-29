from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='hey', kws_threshold=100)
for phrase in speech:
    print(phrase)