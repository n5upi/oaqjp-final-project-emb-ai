from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    blank = response['dominant_emotion']

    # Extract the label and score from the response
    anger = "'anger': {}, ".format(response['anger'])
    disgust = "'disgust': {}, ".format(response['disgust'])
    fear =  "'fear': {}, ".format(response['fear'])
    joy = "'joy': {}, ".format(response['joy'])
    sadness = " and 'sadness': {}. ".format(response['sadness'])
    dominant = "The dominant emotion is {}.".format(response['dominant_emotion'])

    if blank is "None":
        return "Invalid text! Please try again!"
    else:
        return "For the given statement, the system response is " + anger + disgust + fear + joy + sadness + dominant

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
