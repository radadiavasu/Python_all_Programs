# import tkinter as tk
# from tkinter import ttk
# import speech_recognition as sr
# from googletrans import Translator
# import pyttsx3
# from pydub import AudioSegment

# import httpcore
# httpcore.SyncHTTPTransport = httpcore.SyncHTTPTransport

# class VoiceTranslatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Translator")

#         self.speaker_language_var = tk.StringVar()
#         self.listener_language_var = tk.StringVar()

#         self.speaker_language_var.set("en")
#         self.listener_language_var.set("en")

#         languages = ["en", "es", "fr", "de", "zh", "ja"]

#         ttk.Label(root, text="Speaker's Language:").pack(pady=5)
#         self.speaker_language_combobox = ttk.Combobox(root, values=languages, textvariable=self.speaker_language_var)
#         self.speaker_language_combobox.pack(pady=5)

#         ttk.Label(root, text="Listener's Language:").pack(pady=5)
#         self.listener_language_combobox = ttk.Combobox(root, values=languages, textvariable=self.listener_language_var)
#         self.listener_language_combobox.pack(pady=5)

#         self.speaker_language_var.trace("w", self.update_listener_language)

#         ttk.Button(root, text="Start Translation", command=self.start_translation).pack(pady=10)

#     def update_listener_language(self, *args):
#         pass

#     def start_translation(self):
#         speaker_language = self.speaker_language_var.get().lower()
#         listener_language = self.listener_language_var.get().lower()

#         recognizer = sr.Recognizer()

#         with sr.Microphone() as source:
#             print("Say something:")
#             audio = recognizer.listen(source)

#         try:
#             spoken_text = recognizer.recognize_google(audio, language=speaker_language)
#             print("You said:", spoken_text)

#             translator = Translator()
#             translated_text = translator.translate(spoken_text, src=speaker_language, dest=listener_language).text

#             print("Translated Text:", translated_text)

#             # Initialize TTS engine
#             engine = pyttsx3.init()

#             # Get the available voices
#             voices = engine.getProperty('voices')
#             if not voices:
#                 print("No voices available.")
#                 return

#             # Set the voice for the specified listener's language
#             for voice in voices:
#                 languages = voice.languages
#                 if languages and listener_language in languages[0].lower():
#                     engine.setProperty('voice', voice.id)
#                     break
#             else:
#                 print(f"No suitable voice found for {listener_language}")
#                 return

#             # Speak the translated text
#             engine.save_to_file(translated_text, "translated_audio.mp3")
#             engine.runAndWait()

#             # Convert original spoken audio to AudioSegment
#             original_audio = AudioSegment.from_file("translated_audio.mp3", format="mp3")

#             # Convert the translated text to AudioSegment
#             translated_audio = engine.save_to_file(translated_text, None)
#             translated_audio = AudioSegment.from_file(translated_audio, format="mp3")

#             # Combine original and translated audio
#             final_audio = original_audio + translated_audio

#             # Save the final combined audio
#             final_audio.export("final_combined_audio.mp3", format="mp3")

#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VoiceTranslatorApp(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS
# import os

# import httpcore
# httpcore.SyncHTTPTransport = httpcore.SyncHTTPTransport

# class VoiceTranslatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Translator")

#         self.speaker_language_var = tk.StringVar()
#         self.listener_language_var = tk.StringVar()

#         self.speaker_language_var.set("en")
#         self.listener_language_var.set("en")

#         languages = ["en", "es", "fr", "de", "zh", "ja"]

#         ttk.Label(root, text="Speaker's Language:").pack(pady=5)
#         self.speaker_language_combobox = ttk.Combobox(root, values=languages, textvariable=self.speaker_language_var)
#         self.speaker_language_combobox.pack(pady=5)

#         ttk.Label(root, text="Listener's Language:").pack(pady=5)
#         # Correct the variable to use for listener_language_var
#         self.listener_language_combobox = ttk.Combobox(root, values=languages, textvariable=self.listener_language_var)
#         self.listener_language_combobox.pack(pady=5)

#         self.speaker_language_var.trace("w", self.update_listener_language)

#         ttk.Button(root, text="Start Translation", command=self.start_translation).pack(pady=10)

#     def update_listener_language(self, *args):
#         # Set the listener's language to the speaker's language
#         # self.listener_language_var.set(self.speaker_language_var.get())
#         pass

#     def start_translation(self):
#         speaker_language = self.speaker_language_var.get().lower()
#         listener_language = self.listener_language_var.get().lower()

#         recognizer = sr.Recognizer()

#         with sr.Microphone() as source:
#             print("Say something:")
#             audio = recognizer.listen(source)
 
#         try:
#             spoken_text = recognizer.recognize_google(audio, language=speaker_language)
#             print("You said:", spoken_text)

#             translator = Translator()
#             translated_text = translator.translate(spoken_text, src=speaker_language, dest=listener_language).text

#             print("Translated Text:", translated_text)

#             tts = gTTS(translated_text, lang=listener_language)
#             tts.save("translated_audio.mp3")
#             os.system("start translated_audio.mp3")
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VoiceTranslatorApp(root)
#     root.mainloop()

################################## Working File ##################################
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS # google text to speech api
import os # to save the audio file
import pyttsx3  # conversion of text to speech
from langdetect import detect # to know what language was used
import pycountry

# A tuple containing all the language - codes of the language will be detected
all_languages = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be','bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)','zh-tw', 'corsican', 'co', 'croatian', 'hr','czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo','estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german','de', 'greek', 'el', 'gujarati', 'gu','haitian creole', 'ht', 'hausa', 'ha','hawaiian', 'haw', 'hebrew', 'he', 'hindi','hi', 'hmong', 'hmn', 'hungarian','hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian','id', 'irish', 'ga', 'italian','it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)','ku', 'kyrgyz', 'ky', 'lao', 'lo','latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb','macedonian', 'mk', 'malagasy', 'mg', 'malay','ms', 'malayalam', 'ml', 'maltese','mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian','mn', 'myanmar (burmese)', 'my','nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa','polish', 'pl', 'portuguese', 'pt', 'punjabi','pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd','serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl','somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish','sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu','te', 'thai', 'th', 'turkish','tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur','ug', 'uzbek', 'uz','vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getLangName(lang_code):
    language = pycountry.languages.get(alpha_2 = lang_code)
    return language.name

# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query


print ("Welcome to the translator! ")
speak ("Welcome to the translator! ")
print ("Say the sentence you want to translate once you see the word 'listening'")

# Input from user and make input to lowercase
query = takecommand()
while (query == "None"):
    query = takecommand()

from_lang = detect(query)
print ("The user's sentence is in ", getLangName(from_lang)) 

def destination_language():
    print("Enter the language in which you	want to convert : Ex. Hindi , English , Spanish, etc.")
    print()

    # Input destination language in
    # which the user wants to translate
    to_lang = takecommand()
    while to_lang == "None":
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang


to_lang = destination_language()

# Mapping it with the code
while (to_lang not in all_languages):
    print("Language in which you are trying	to convert is currently not available, please input some other language")
    print()
    to_lang = destination_language()

to_lang = all_languages[all_languages.index(to_lang) + 1]

# invoking Translator
translator = Translator()

# Translating from src to dest
text_to_translate = translator.translate(query, dest=to_lang)

text = text_to_translate.text

# Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because by default it speaks very slowly
speak = gTTS(text=text, lang=to_lang, slow=False)

# Using save() method to save the translated speech in capture_voice.mp3
speak.save("audioCap.mp3")

# Using OS module to run the translated voice.
playsound('audioCap.mp3')
os.remove('audioCap.mp3')

# Printing Output
print(text)

# from playsound import playsound
# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS
# import os
# import pyttsx3
# from langdetect import detect
# import pycountry
# from pydub import AudioSegment

# all_languages = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be','bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)','zh-tw', 'corsican', 'co', 'croatian', 'hr','czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo','estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german','de', 'greek', 'el', 'gujarati', 'gu','haitian creole', 'ht', 'hausa', 'ha','hawaiian', 'haw', 'hebrew', 'he', 'hindi','hi', 'hmong', 'hmn', 'hungarian','hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian','id', 'irish', 'ga', 'italian','it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)','ku', 'kyrgyz', 'ky', 'lao', 'lo','latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb','macedonian', 'mk', 'malagasy', 'mg', 'malay','ms', 'malayalam', 'ml', 'maltese','mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian','mn', 'myanmar (burmese)', 'my','nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa','polish', 'pl', 'portuguese', 'pt', 'punjabi','pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd','serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl','somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish','sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu','te', 'thai', 'th', 'turkish','tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur','ug', 'uzbek', 'uz','vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def getLangName(lang_code):
#     language = pycountry.languages.get(alpha_2=lang_code)
#     return language.name

# def extract_voice_from_file(file_path):
#     audio = AudioSegment.from_mp3(file_path)
    
#     # Assuming your voice is in the first 5 seconds, adjust the duration accordingly
#     voice_segment = audio[:5000]  
    
#     voice_segment.export("extracted_voice.wav", format="wav")

#     return "extracted_voice.wav"

# def destination_language():
#     to_lang = None
#     while True:
#         print("Enter the language in which you want to convert: Ex. Hindi, English, Spanish, etc.")
#         print()

#         r = sr.Recognizer()
#         with sr.AudioFile("extracted_voice.wav") as source:
#             try:
#                 print("Listening for language input...")
#                 audio_data = r.record(source, duration=10)  # Increase the duration if needed
#                 to_lang = r.recognize_google(audio_data, language='en-in')
#                 to_lang = to_lang.lower()
#                 print(f"You said: {to_lang}")
#             except sr.UnknownValueError:
#                 print("Sorry, couldn't recognize the language. Please try again.")
#             except sr.RequestError as e:
#                 print(f"Could not request results from Google Speech Recognition service; {e}")

#         if to_lang in all_languages:
#             to_lang = all_languages[all_languages.index(to_lang) + 1]
#             break
#         else:
#             print("Language in which you are trying to convert is currently not available, please input some other language")
#             print()

#     return to_lang

# print("Welcome to the translator! ")
# speak("Welcome to the translator! ")

# # Assuming the MP3 file is named "recorded_voice_adjusted.mp3"
# extracted_voice_file = extract_voice_from_file("recorded_voice_adjusted.mp3")

# # Input from user and make input to lowercase
# from_lang = "en"  # Replace with the correct language code if needed
# print("The user's sentence is in ", getLangName(from_lang))

# to_lang = destination_language()

# # Mapping it with the code
# while to_lang not in all_languages:
#     print("Language in which you are trying to convert is currently not available, please input some other language")
#     print()
#     to_lang = destination_language()

# to_lang = all_languages[all_languages.index(to_lang) + 1]

# # Invoking Translator
# translator = Translator()

# # Translating from src to dest
# query = "This is a sample sentence."  # Replace with the actual sentence
# text_to_translate = translator.translate(query, dest=to_lang)

# text = text_to_translate.text

# # Using Google-Text-to-Speech, i.e., gTTS() method to speak the translated text into the destination language which is stored in to_lang.
# # Also, we have given the 3rd argument as False because by default it speaks very slowly
# speak = gTTS(text=text, lang=to_lang, slow=False)

# # Using save() method to save the translated speech in capture_voice.mp3
# speak.save("audioCap.mp3")

# # Using OS module to run the translated voice.
# playsound('audioCap.mp3')
# os.remove('audioCap.mp3')

# # Printing Output
# print(text)

