import json
from locust import HttpUser, task, between

#Define a class to stimulate a real user for benchmarking
class APIUsers(HttpUser):
    wait_time = between(1, 2)

    @task
    def call_predict(self):
        payload = {
            'feature1': 1.0,
            'feature2': 2.0
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post('/predict', data = json.dumps(payload), headers = headers)

    @task(1)
    def call_root(self):
        self.client.get('/')