
from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client["SIH_DB"]



@app.route('/')
def index():
    news_data = []
    alltitles = db.Processed_News.find()

    for objects in alltitles:
        news_data.append({'title':objects['title'],'Sentiment':objects['Sentiment']})
    
    return render_template('index.html',news_data = news_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))



