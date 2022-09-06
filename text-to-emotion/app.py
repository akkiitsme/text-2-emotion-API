from flask import Flask
from flask import Flask, jsonify, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import nltk

app = Flask(__name__)

@app.route("/api")
def queryApi():
    query = request.args.get('query')
    list=[]
    lower_case=query.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '',string.punctuation))
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if len(query)==0:
        result={
        "content": query,
        "result": "Empty",
        "status": False
        }
    else:
        if neg > pos:
            result={
            "content": query,
            "result": "negative",
            "status": True
            }
        elif pos> neg:
            result={
            "content": query,
            "result": "positive",
            "status": True
            }
        elif neu>pos and neu>neg:
            result={
            "content": query,
            "result": "neutral",
            "status": True
            } 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)