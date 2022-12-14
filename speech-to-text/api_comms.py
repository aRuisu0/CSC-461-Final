import textwrap
import requests
import json
import time
from translate  import*
from api_code import API_KEY_ASSEMBLYAI
import os

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}

headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB


def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
    return upload_response.json()['upload_url']


def transcribe(audio_url, sentiment_analysis):
    transcript_request = {
        'audio_url': audio_url, 
        'language_detection': True,
        "speaker_labels": True,
        "sentiment_analysis": sentiment_analysis
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']

        
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url, sentiment_analysis):
    transcribe_id = transcribe(url, sentiment_analysis)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
            
        print("waiting for 30 seconds")
        time.sleep(30)
        
        
def save_transcript(url, title, sentiment_analysis=False):
    data, error = get_transcription_result_url(url, sentiment_analysis)
    
    if data:
        title = title.strip().replace(".wav", ".txt")
        filename = title
        my_wrap = textwrap.TextWrapper(width = 60)
        input_file = os.path.join("transcripts", filename)
        with open(input_file, 'w') as f:
            f.write(my_wrap.fill(data['text']))
            
        tinput = input("Would you like to translate a transcript? y/n:")
        if tinput.lower() == 'y':
            filename = translate(filename)
             
        if sentiment_analysis:
            title = title.strip().replace(".txt", ".json")
            filename = title
            transc_file = os.path.join("sentiments", filename)
            with open(transc_file, 'w') as f:
                sentiments = data['sentiment_analysis_results']
                json.dump(sentiments, f, indent=4)
        print('Transcript saved')
        
    elif error:
        print("Error!!!", error)
        return False