from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_null_predictio():
    response = client.post('/v1/prediction', json={
        "production_budget": 0,
        "title_year": 0,
        "aspect_ratio": 0,
        "duration": 0,
        "budget": 0,
        "imdb_score": 0,
        "opening_gross": 0,
        "screens": 0
    })
    assert response.status_code == 200
    assert response.json()['worldwidegross'] == 0


def tets_random_predictio():
    response = client.post('/v1/prediction', json={
        "production_budget": 1000000,
        "title_year": 2000,
        "aspect_ratio": 2,
        "duration": 100,
        "budget": 1000000,
        "imdb_score": 7,
        "opening_gross": 1000000,
        "screens": 100
    })
    assert response.status_code == 200
    assert response.json()['worldwidegross'] > 0
