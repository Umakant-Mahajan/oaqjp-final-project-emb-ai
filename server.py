import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detector")

@app.route("/",methods=["GET"])
def acces():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])  # Fixed typo in methods
def emotion_analysis():  # Fixed typo in function definition
    text_to_analyse = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyse)

    return (
        "For the given statement, the system response is 'anger': " + str(res["anger"]) +
        ", 'disgust': " + str(res["disgust"]) +
        ", 'fear': " + str(res["fear"]) +
        ", 'joy': " + str(res["joy"]) +
        " and 'sadness': " + str(res["sadness"]) +
        ". The dominant emotion is " + res["dominant_emotion"] + "."
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)
