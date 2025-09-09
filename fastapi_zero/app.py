from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Olá mundo!')


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello():
    return """
    <html>
        <title>Hello World!</title>
        <body>
            <h1>Hello Worldsss</h1>
        </body>
    </html>
"""
