import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
 
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    
    # Determine the dominant emotion
    emotions = {
        'joy': joy_score,
        'anger': anger_score,
        'disgust': disgust_score,
        'sadness': sadness_score,
        'fear': fear_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Create the desired output format
    output = {
        'joy': joy_score,
        'anger': anger_score,
        'disgust': disgust_score,
        'sadness': sadness_score,
        'fear': fear_score,
        'dominant_emotion': dominant_emotion
    }

    return output
