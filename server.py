from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get('textToAnalyze')
    if textToAnalyze:
        json_emotions=emotion_detector(textToAnalyze)
        return f"For the given statement, the system response is 'anger': {json_emotions['anger']}, 'disgust': {json_emotions['disgust']}, 'fear': {json_emotions['fear']}, 'joy': {json_emotions['joy']}, and 'sadness': {json_emotions['sadness']}. The dominant emotion is {json_emotions['dominant_emotion']}", 200
    return render_template("index.html")

app.run(port=5000, debug=True)