import openai
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


openai.api_key = "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"

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said:", recognized_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition; {e}")

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
