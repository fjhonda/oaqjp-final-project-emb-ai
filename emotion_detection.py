import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, headers = headers, json = json)


    #formatting the response to json
    response_json = json.loads(response.text)
    
    emotions_json = {
        "anger" : response_json["emotionPredictions"]["emotion"]["anger"]
        "disgust" : response_json["emotionPredictions"]["emotion"]["disgust"]
        "fear" : response_json["emotionPredictions"]["emotion"]["fear"]
        "joy" : response_json["emotionPredictions"]["emotion"]["joy"]
        "sadness" : response_json["emotionPredictions"]["emotion"]["sadness"]
        "dominant_emotion" : 
    }

