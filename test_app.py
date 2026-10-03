from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_healthz():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200


def test_notes():
    client = app.test_client()
    response = client.get("/notes")
    assert response.status_code == 200