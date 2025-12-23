import numpy as np
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

#Test case
def test_predict_with_mock():
    with patch('model.model.predict') as mock_predict:
        mock_predict.return_value = [99] #hardcoding return value
        response = client.post(
            '/predict',
            json = {
                'SepalLengthCm': 5.5,
                'SepalWidthCm': 2.1,
                'PetalLengthCm': 4.3,
                'PetalWidthCm': 1.25
            }
        )
        assert response.status_code == 200
        assert response.json() == {'prediction': 99}