# 1
# import googletrans
# import speech_recognition

# recognizer = speech_recognition.Recognizer()
# with speech_recognition.Microphone() as source:
#     print("Speak Now")
#     voice = recognizer.listen(source)
#     text = recognizer.recognize_google(voice, language="fr")
#     print(text)


# translator = googletrans.Translator()
# translation = translator.translate(text, dest="fr")
# print(translation)
# #print(googletrans.LANGUAGES)


# 2
# import googletrans
# import speech_recognition

# recognizer = speech_recognition.Recognizer()

# with speech_recognition.Microphone() as source:
#     print("Speak Now")
#     voice = recognizer.listen(source)

# try:
#     text = recognizer.recognize_google(voice, language="fr")
#     print("Recognized Text:", text)

#     translator = googletrans.Translator()
#     translation = translator.translate(text, dest="fr")
#     print("Translation:", translation.text)
    
# except speech_recognition.UnknownValueError:
#     print("Could not recognize speech.")
# except googletrans.exceptions.GoogleTranslateError as e:
#     print("Translation Error:", e)


# 3
# import googletrans
# import speech_recognition

# recognizer = speech_recognition.Recognizer()

# with speech_recognition.Microphone() as source:
#     print("Speak Now")
#     voice = recognizer.listen(source)

# try:
#     text = recognizer.recognize_google(voice, language="fr")
#     print("Recognized Text:", text)

#     translator = googletrans.Translator()
#     translation = translator.translate(text, dest="fr")
#     print("Translation:", translation.text)

# except speech_recognition.UnknownValueError:
#     print("Could not recognize speech.")
# except Exception as e:
#     print("Translation Error:", e)


# 4
# import speech_recognition
# import googletrans

# recognizer = speech_recognition.Recognizer()

# with speech_recognition.Microphone() as source:
#     print("Speak Now")
#     voice = recognizer.listen(source)

# try:
#     text = recognizer.recognize_google(voice, language="en")
#     print("Recognized Text:", text)

#     translator = googletrans.Translator()
#     translation = translator.translate(text, dest="fr")  # Change dest to your desired language code
#     print("Translation:", translation.text)

# except speech_recognition.UnknownValueError:
#     print("Could not recognize speech.")
# except Exception as e:
#     print("Error:", e)
    
# import re

# pattern = r'\b\w+\b'
# text = 'hello my name is Vasu'

# match = re.search(pattern, text)
# print(match)
# if match:
#     match_text = match.group()
# else:
#     print("No match found")

p1 = [1,2,3,4,5]

print(p1[3:])
# x = slice(2)