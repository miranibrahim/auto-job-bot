import json
import os
from datetime import datetime

class Storage:
    def __init__(self, path):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(path):
            self.save({
                "last_run_time": None,
                "countries": {}
            })

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def update_country(self, country, count):
        data = self.load()
        data["countries"][country] = count
        data["last_run_time"] = datetime.utcnow().isoformat()
        self.save(data)

    def get_previous_count(self, country):
        data = self.load()
        return data["countries"].get(country, 0)