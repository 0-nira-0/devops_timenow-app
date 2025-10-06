from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/task/unchecked")
def get_unchecked_task():
    return JSONResponse({
        "checked": False,
        "text": "run 100 miles"
    })

@app.get("/task/checked")
def get_checked_task():
    return JSONResponse({
        "checked": True,
        "text": "run 100 miles"
    })

# Vercel will use this
handler = app
