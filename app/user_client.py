import requests
import os

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8000")

def get_user(user_id: str):
    try:
        res = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        if res.status_code == 200:
            return res.json()
        return None
    except:
        return None