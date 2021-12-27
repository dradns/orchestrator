import requests
import os

orchestrator_domain = os.environ.get("ORCHESTRATOR_DOMAIN","orchestrator")

def test_main_request():
    for i in range(1):
        response = requests.get(f'http://{orchestrator_domain}/mainRequest/id1')
        assert response.status_code == 200
        assert response.json() == {
            "myKey": [
                0,
                1,
                2,
                4,
                5,
                7,
                9
            ]
        }


