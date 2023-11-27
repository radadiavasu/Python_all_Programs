import pyttsx3
 
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# say method on the engine that passing input text to be spoken
engine.say('swagat he, me apki kya madad kar sakta hu?. pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. Engine instance. it is a very easy to use tool which converts the entered text into speech. The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows. It supports three TTS engines like (1)sapi5 – SAPI5 on Windows, (2)nsss – NSSpeechSynthesizer on Mac OS X, (3)espeak – eSpeak on every other platform')
 
# run and wait method, it processes the voice commands.
engine.runAndWait()
engine.stop()

##########################################################################################################
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[17].id)
# engine.say('Hello, World!')
# engine.runAndWait()

##########################################################################################################
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('Here we go round the mulberry bush.')
# engine.runAndWait()