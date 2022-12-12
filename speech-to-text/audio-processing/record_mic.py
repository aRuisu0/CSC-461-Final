import pyaudio
import wave

# Setting parameters for .wav audio file
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Create Object With PyAudio to play and record audio
rec = pyaudio.PyAudio()

# Recording Begins
stream = rec.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)
print("Start Recording...")

frames = []
seconds = 5
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    # Read each chunk of data
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

print("Recording Stopped")

stream.stop_stream()
stream.close()
rec.terminate()

# Output .wav file with audio format
wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(rec.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()