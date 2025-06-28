import speech_recognition as sr
import pyttsx3
from modules.veda_core import ask_veda
from modules.logger import log_interaction

# 🎤 Text-to-Speech Setup (Natural Voice)
engine = pyttsx3.init()
engine.setProperty('rate', 185)  # Faster, human-like speech
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():  # Windows users: Microsoft Zira
        engine.setProperty('voice', voice.id)
        break


# 🗣 Speak Function
def speak(text):
    clean_text = text.replace("📘", "").replace("👨‍🏫", "Professor").replace("📂", "").replace("⚠️", "").replace("🔍",
                                                                                                              "").replace(
        "❌", "").replace("🧠", "")
    print("VEDA >", clean_text)
    engine.say(clean_text)
    engine.runAndWait()


# 🎧 Listen Function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Listening... (say 'exit' to stop)")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print("You >", query)
            return query
        except sr.WaitTimeoutError:
            return "Listening timed out, please speak again."
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is down."


# 🚀 Main Loop
def main():
    speak("Hello Anwar. I am VEDA, your voice assistant. How can I help you?")
    exit_phrases = ["exit", "quit", "shutdown", "bye veda", "veda exit", "stop now"]

    while True:
        query = listen()

        if any(phrase in query.lower() for phrase in exit_phrases):
            speak("Logging off. Study well, rise high!")
            break

        response = ask_veda(query)
        log_interaction("VOICE", query, response)
        speak(response)


if __name__ == "__main__":
    main()
