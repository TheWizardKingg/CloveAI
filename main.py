import speech_recognition as sr
from faster_whisper import WhisperModel
from ollama import chat
from playsound import playsound
import requests
import time
import os
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="float32"
)

conversation = [
    {
        "role": "system",
        "content": """
You are Clove, an AI desktop companion.
You are playful, witty, energetic, and intelligent.
You speak naturally like a real person.
You never use emojis.
You never use markdown.
You never sound like customer support.
Keep most responses under 2 sentences.
Do not overexplain.
Talk casually and naturally.
Occasionally use light teasing or sarcasm.
You are talking through voice, so responses should sound natural when spoken aloud.
"""
    }
]
start_time = time.time()
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)

        with open("audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

    

    segments, info = model.transcribe(
        "audio.wav",
        language="en",
        beam_size=10
    )

    print("Transcription Time:", time.time() - start_time)

    query = ""

    for segment in segments:
        query += segment.text

    return query.strip()

CLOVE_API_URL = "https://operation-chosen-closable.ngrok-free.dev/synthesize"

AUDIO_OUTPUT_PATH = "clove_spoken_response.wav"

def generate_clove_voice(text_input):

    payload = {
        "text": text_input
    }

    try:

        voice_response = requests.post(
            CLOVE_API_URL,
            json=payload,
            timeout=45
        )

        if voice_response.status_code == 200:

            with open(AUDIO_OUTPUT_PATH, "wb") as f:
                f.write(voice_response.content)

            print(
                f"🎉 Success! Audio saved to:\n{os.path.abspath(AUDIO_OUTPUT_PATH)}"
            )
            print("Total latency: ",time.time() - start_time)

            return True

        else:
            print(
                f" Cloud Server Error ({voice_response.status_code}):"
            )
            print(voice_response.text)
            return False
    except requests.exceptions.RequestException as e:
        print(
            f" Failed to connect to Google Colab pipeline:\n{e}"
        )
        return False

if __name__ == "__main__":
    running=True
    while (running==True):
        text = listen()
        print("You said:", text)
        if any(word in text.lower() for word in ["bye","goodbye","exit","quit","stop clove"]):
            print("Goodbye! Shutting down CloveAI.")
            running = False
            break
        conversation.append(
            {
                "role": "user",
                "content": text
            }
        )
        LLM_response = chat(
            model="gemma3:1b",
            messages=conversation
        )
        text_response = LLM_response["message"]["content"]
        conversation.append(
            {
                "role": "assistant",
                "content": text_response
            }
        )
        print("\nClove:", text_response)
        success = generate_clove_voice(text_response)

        if success:
            print("Audio latency: ",time.time() - start_time)
            playsound(AUDIO_OUTPUT_PATH)