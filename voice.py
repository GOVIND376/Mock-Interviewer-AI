'''
JarvisVoice:
 * Text-to-Speech using pyttsx3
 * Speech-to-text using SpeechRecognition (Google API)
 '''
 
import pyttsx3
import speech_recognition as sr
from config import TTS_RATE,TTS_VOLUME


class JarvisVoice:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate",TTS_RATE)
        self.engine.setProperty("volume",TTS_VOLUME)
        self.recognizer = sr.Recognizer()
    
    def speak(self,text:str) ->None:
        
        #Speak text aloud using and also print it.
        
        print(f"Jarvis:{text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as exc:
            print(f"[TTS Error]{exc}")
            
    def listen(self) ->str:
            
            '''
            Listen through the microphone and return the recognized text.
            Returns an empty string if recognition fails.
            '''
        try:
            with sr.Microphone() as  source:
                self.speak("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio= self.recognizer.listen(source)
            return self.recognizer.recognize_google(audio)
        except Exception as exc: 
            print(f"[Speech Recognition Error]{exc}:")
            return""    
            
    
        