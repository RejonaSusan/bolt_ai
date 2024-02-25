from fastapi import FastAPI
from transcript import getTranscript
from summarize import summariseTranscript

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@app.post("/video/summary")
async def video_summary(link):
    try:
        video_id = link[30:41]
        transcript = getTranscript(video_id)
        print(transcript)
        summary = summariseTranscript(transcript)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, debug=True)
