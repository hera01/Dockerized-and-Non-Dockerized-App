from locust import HTTPUser, task, between
import json

class BreastCancer(HTTPUser):
    wait_time = between(1,2)

    @task
    def get_valueclass(self):
        payload = {"text": ""}
        header = {'Content-Type': 'application/json', 'Accept':'application/json' }
        self.client.post("/score", data=json.dumps(payload),headers=header, catch_response=False)
