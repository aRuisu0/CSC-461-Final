import requests
from api_comms import *
from record_mic import*
from translate import*
from sentiment_analysis import*
import sys

    
        
def main():
    
    uinput = input("Record Audio? y/n: ")
    if uinput.lower() == 'y':
        record()
    
    tsinput = input("Transcribe Audio? y/n: ")
    if tsinput.lower() == 'y':
        file_name = input('Enter .wav file to transcribe: ') + '.wav'
        audio_url = upload(file_name)
        
        save_transcript(audio_url, file_name, sentiment_analysis= True)
        
        json_name = input('Enter name of JSON file: ') + '.json'
        analysis(json_name)
        
    
    # tinput = input("Would you like to translate a transcript? y/n:")
    # if tinput.lower() == 'y':
    #     translate()
     
if __name__ == "__main__":
    main()
