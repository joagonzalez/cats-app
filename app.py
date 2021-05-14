from logging import DEBUG
import socket
import random
import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI(
    title='Cats API',
    description='A simple cat application',
    version='1.0.0',
    docs_url='/docs'
)

container_hostname = socket.gethostname()
templates = Jinja2Templates(directory="templates")

# list of cat images
images = [
    "https://media.giphy.com/media/7SfAXqgRgh0li/giphy.gif",
    "https://media.giphy.com/media/W8krmZSDxPIfm/giphy.gif",
    "https://media.giphy.com/media/W80Y9y1XwiL84/giphy.gif",
    "https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif",
    "https://media.giphy.com/media/l0Iy9Kry5yhBSwQSs/giphy.gif"
]


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    url = random.choice(images)
    return templates.TemplateResponse("index.html", {"request": request, "url": url, "hostname": container_hostname})


if __name__ == '__main__':
    uvicorn.run(    
        "app:app",
        host="0.0.0.0",
        port=5000,
        log_level=DEBUG,
        reload=True,
        workers=2 
    )