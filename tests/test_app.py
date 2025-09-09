from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def hello_test():
    client = TestClient(app)

    response = client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert (
        """
    <html>
        <title>Hello World!</title>
        <body>
            <h1>Hello Wor</h1>
        </body>
    </html>
      """
        in response.text
    )
