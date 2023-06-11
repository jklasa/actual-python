import requests
import json
from typing import Dict, Optional


class ActualAPI:
    def __init__(self, base_url: str = "http://localhost", port: int = 3000):
        self.api_endpoint = f"{base_url}:{port}/api"
        self.open = True

    def set_config(self, server_url: str, password: str, budget_id: str, save: bool = True) -> int:
        url = f"{self.api_endpoint}/config"
        data = {
            "serverURL": server_url,
            "password": password,
            "budgetID": budget_id
        }

        response = requests.post(url, json=data)
        if response.status_code == 201:
            config_id = response.json().get('id')

            if save:
                self.config_id = config_id
            return config_id
        else:
            raise Exception("Failed to save configuration")

    def get_config(self, config_id: int) -> Dict[str, str]:
        url = f"{self.api_endpoint}/config/{config_id}"
        
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise Exception("Configuration not found")
        else:
            raise Exception("Failed to retrieve configuration")

    def openRemote(self, server_url: str, password: str, budget_id: str) -> None:
        data = {
            "serverURL": server_url,
            "password": password,
            "budgetId": budget_id,
        }

        response = requests.post(url=f"{self.api_endpoint}/open", json=data)
        if response.status_code != 200:
            raise Exception("Failed to open Actual Budget API on backend")
        self.open = True

    def closeRemote(self) -> None:
        response = requests.post(url=f"{self.api_endpoint}/close")
        if response.status_code != 200:
            raise Exception("Failed to close Actual Budget API on backend")
        self.open = False

    def get_accounts(self):
        assert self.open
        response = requests.get(url=f"{self.api_endpoint}/accounts")
        if response.status_code == 412:
            raise Exception("Remote is uninitialized.")
        if response.status_code != 200:
            raise Exception("Failed to get accounts.")
        return json.loads(response.content.decode('utf-8'))

