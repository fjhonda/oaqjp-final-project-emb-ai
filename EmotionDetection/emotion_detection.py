import requests
import json

def empty_response():
    return {
        "anger" : None,
        "disgust" : None,
        "fear" : None,
        "joy" : None,
        "sadness" : None,
        "dominant_emotion": None
    }

def emotion_detector(text_to_analyze):

    if text_to_analyze == None or len(text_to_analyze)==0:
        return empty_response

    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, headers = headers, json = json_data)

    #formatting the response to json
    response_json = json.loads(response.text)
    
    emotions_json = {
        "anger" : response_json["emotionPredictions"][0]["emotion"]["anger"],
        "disgust" : response_json["emotionPredictions"][0]["emotion"]["disgust"],
        "fear" : response_json["emotionPredictions"][0]["emotion"]["fear"],
        "joy" : response_json["emotionPredictions"][0]["emotion"]["joy"],
        "sadness" : response_json["emotionPredictions"][0]["emotion"]["sadness"]
    }

    dominant_emotion = max(emotions_json, key=emotions_json.get)
    emotions_json["dominant_emotion"]=dominant_emotion
    
    return emotions_json

