import openai
import speech_recognition as sr
from gtts import gTTS
import playsound

openai.api_key = "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"

recognizer = sr.Recognizer()

def recognizer_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = sr.listen(source)
        print("Recognizing...")

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

        def text_to_speech(text):
            tts = gTTS(text)
            tts.save("response.mp3")
            playsound.playsound("response.mp3")

        while True:
            user_input = input("You: ")
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"You said: {user_input} \nAI:",
                max_tokens=150
            )
            ai_response = response.choice[0].text.strip()
            print(f"AI: {ai_response}")

            if "exit" in user_input.lower():
                break
            if "speak" in user_input.lower():
                speech = recognizer_speech()
                print(f"You said: {speech}")

            text_to_speech(ai_response)

        print("Conversation ended.")



    __init__.py

