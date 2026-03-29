import requests
from flask import g

class ServiceClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        if hasattr(g, 'token') and g.token:
            headers["Authorization"] = f"Bearer {g.token}"
        return headers

    def get(self, endpoint, params=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=self._get_headers(), params=params, timeout=10)
            if response.status_code == 200:
                return response.json()["data"]
            else:
                return None
        except Exception as e:
            # Log error or handle exception as needed
            return None

    def post(self, endpoint, data=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, headers=self._get_headers(), json=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            # Log error or handle exception as needed
            return None

    def put(self, endpoint, data=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.put(url, headers=self._get_headers(), json=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            # Log error or handle exception as needed
            return None

    def delete(self, endpoint):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.delete(url, headers=self._get_headers(), timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            # Log error or handle exception as needed
            return None
