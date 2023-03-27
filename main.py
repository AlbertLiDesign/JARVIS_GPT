import os
import openai
import Recording as RC
import VoiceSynthesis as VS

if __name__ == "__main__":
    out_file = 'demo.wav'
    rec_time = 3 # Recording time
    speed = 180 # speeking speed

    openai.api_key = "Your API key"
    openai.organization = os.getenv("OPENAI_ORGANIZATION")

    conversation = []

    while(True):
        # Recording
        RC.record_audio(out_file)

        # Voice recognizition
        audio_file = open(out_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        user_input = transcript['text']
        print(user_input)

        conversation.append({"role": "user", "content":user_input})
        # ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        output_text = response['choices'][0]['message']['content'];
        conversation.append({"role": "assistant", "content": output_text})
        print('\n'+output_text)

        #Voice synthesis
        VS.TextToVoice(output_text, speed)
