import requests
from api_code import API_KEY_ASSEMBLYAI
from api_comms import *
import sys

filename = sys.argv[1]
audio_url = upload(filename)

save_transcript(audio_url, filename)