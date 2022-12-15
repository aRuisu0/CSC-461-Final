import requests
from api_comms import *
from record_mic import *
from translate import *
from sentiment_analysis import *
import sys


def main():

    while True:
        uinput = input("Record Audio? y/n: ")
        if uinput.lower() == 'y':
            record()

        tsinput = input("Transcribe Audio? y/n: ")
        if tsinput.lower() == 'y':
            file_name = input('Enter .wav file to transcribe: ') + '.wav'
            wav_file = os.path.join("wav", file_name)
            audio_url = upload(wav_file)

            save_transcript(audio_url, file_name, sentiment_analysis=True)

            json_name = input('Enter name of JSON file: ') + '.json'
            json_file = os.path.join("sentiments", json_name)
            analysis(json_file)

        # Prompt the user for their choice
        choice = input("Do you want to run the program (Y/N)? ")

        # If the user enters "Y" or "y", run the program
        if choice == "Y" or choice == "y":
            main()
        elif choice == "N" or choice == "n":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
