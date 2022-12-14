import requests
from api_code import API_KEY_ASSEMBLYAI
from api_comms import *
from record_mic import*
from translate import*
import sys

def main():
    uinput = input("Record Audio? y/n: ")
    if uinput.lower() == 'y':
        record()

    file_name = input('Enter file name to translate: ')
    audio_url = upload(file_name)
    save_transcript(audio_url, file_name)

    translate()

    
main()
