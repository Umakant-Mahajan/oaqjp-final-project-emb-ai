'''This is the server module and handles requests to return the detected emotion '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detector")


@app.route("/", methods=["GET"])
def access():
    '''This is the entry point that renders the main HTML'''
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    '''This performs the emotion analysis on the provided text'''
    text_to_analyse = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyse)

    
    if res["dominant_emotion"] == "None":
        return "Invalid text! Please try again!"

    
    return (
        f"For the given statement, the system response is 'anger': {res['anger']}, "
        f"'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']}, "
        f"and 'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}."
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True)
