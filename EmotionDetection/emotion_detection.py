import requests

def emotion_detector(text_to_analyse):
        url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        Headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        input_json= { "raw_document": { "text": text_to_analyse } }
        res = requests.post(url,json=input_json, headers=Headers)
        dict_res = res.json()
        if(res.status_code == 400):
            emotions = {
        'anger': "", 'disgust': "",
        'fear':"",'joy':"", 'sadness': "" }
            for key in emotions:
                emotions[key]= "None"
            emotions['dominant_emotion'] = "None"
            return emotions
        anger_score = dict_res["emotionPredictions"][0]['emotion']['anger'] 
        disgust_score = dict_res["emotionPredictions"][0]['emotion']['disgust']
        fear_score= dict_res["emotionPredictions"][0]['emotion']['fear']
        joy_score = dict_res["emotionPredictions"][0]['emotion']['joy']
        sadness_score = dict_res["emotionPredictions"][0]['emotion']['sadness']
        emotions = {
        'anger': anger_score, 'disgust': disgust_score,
        'fear': fear_score,'joy': joy_score, 'sadness': sadness_score}
        

        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions