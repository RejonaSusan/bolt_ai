from flask import Flask
from transcript import getTranscript
from summarize import summariseTranscript

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/video/summary")
def videoSummary():
    try:
        link = "https://www.youtube.com/embed/6OQAHcB72dg"
        video_id = link[30:41]
        transcript =  getTranscript(video_id)
        print(transcript)
        s = summariseTranscript(transcript)
        return s
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == '__main__':
    app.run(debug=True, port=8001)