import pyaudio
import wave
import keyboard
import time

def record_audio(output_filename):
    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Press 'space' to speak...")

    frames = []

    while True:
        if keyboard.is_pressed("space"):
            time.sleep(0.2)  # 避免误触发，增加短暂延时
            break

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            if keyboard.is_pressed("space"):
                time.sleep(0.2)  # 避免误触发，增加短暂延时
                break
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return output_filename