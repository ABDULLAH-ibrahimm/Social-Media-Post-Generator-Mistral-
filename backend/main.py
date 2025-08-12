from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/generate/")
def generate_posts(topic: str = Form(...), tone: str = Form(...), platform: str = Form(...)):
    prompt = f"""
    Create 3 social media post drafts for the platform: {platform}.
    Topic: {topic}
    Tone: {tone}

    Each post should have:
    1. A catchy opening line
    2. Main content
    3. A call-to-action

    Format clearly with "Post 1", "Post 2", "Post 3".
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    result = response.json()
    return {"posts": result["response"].strip()}
