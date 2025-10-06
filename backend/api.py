from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

@app.get("/time", response_class=PlainTextResponse)
def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# Vercel looks for a top-level `app` variable (ASGI)
handler = app
