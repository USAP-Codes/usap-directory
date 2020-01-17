# services/server/tests/test_app.py

import json


def test_app(test_app):
    client = test_app.test_client()
    response = client.get('/app')
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert 'success' in data['status']
