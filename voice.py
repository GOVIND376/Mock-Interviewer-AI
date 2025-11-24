"""
voice.py

JarvisVoice:
- Text-to-speech using pyttsx3
- Speech-to-text using sounddevice + Vosk (no PyAudio needed)
"""

import os
import json
import pyttsx3
import sounddevice as sd
from vosk import Model, KaldiRecognizer

from config import TTS_RATE, TTS_VOLUME


MODEL_DIR_NAME = "models/vosk-model-small-en-us"  # adjust if your folder name is different


class JarvisVoice:
    def __init__(self) -> None:
        # --- TTS setup ---
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", TTS_RATE)
        self.engine.setProperty("volume", TTS_VOLUME)

        # --- STT (speech-to-text) setup ---
        self.sample_rate = 16000  # Vosk default
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, MODEL_DIR_NAME)

        if not os.path.isdir(model_path):
            raise RuntimeError(
                f"Vosk model directory not found at: {model_path}\n"
                "Make sure you downloaded a Vosk model and placed it there."
            )

        self.model = Model(model_path)

    def speak(self, text: str) -> None:
        """Speak text aloud and also print it."""
        print(f"Jarvis: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as exc:
            print(f"[TTS Error] {exc}")

    def listen(self, duration: float = 8.0) -> str:
        """
        Record from microphone for a fixed duration (in seconds)
        and return recognized text using Vosk.
        """
        self.speak("Listening...")

        try:
            # Record audio
            audio = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype="int16",
            )
            sd.wait()  # Wait until recording is finished
        except Exception as exc:
            print(f"[Audio Input Error] {exc}")
            self.speak("I could not access your microphone. Please check your audio settings.")
            return ""

        # Convert to bytes for Vosk
        data = audio.tobytes()

        # Recognize with Vosk
        try:
            recognizer = KaldiRecognizer(self.model, self.sample_rate)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
            else:
                result = recognizer.FinalResult()

            result_json = json.loads(result)
            text = result_json.get("text", "").strip()
            print(f"[Recognized] {text}")
            return text
        except Exception as exc:
            print(f"[STT Error] {exc}")
            self.speak("I had trouble understanding your voice.")
            return ""
