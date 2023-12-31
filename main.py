import openai
from speech_recognition import Microphone, Recognizer, exceptions, RequestError
from gtts import gTTS
from playsound import playsound

# Set your OpenAI API key here
openai.api_key = "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"

recognizer = Recognizer()


def recognize_speech():
    with Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        print("Recognizing...")

        try:
            recognized_text = recognizer.recognize_google(audio)
            return recognized_text
        except exceptions:
            print("Google Speech Recognition could not understand audio")
            return ""
        except RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            return ""


def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    playsound("response.mp3")


while True:
    user_input = input("You: ")

    if "exit" in user_input.lower():
        break

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"You said: {user_input} \nAI:",
        max_tokens=150
    )
    ai_response = response.choices[0].text.strip()
    print(f"AI: {ai_response}")

    if "speak" in user_input.lower():
        speech = recognize_speech()
        print(f"You said: {speech}")
        text_to_speech(speech)

print("Conversation ended.")
