import requests
import json
import datetime


class Country:
    def __init__(self, country):
        self.country = country

    @staticmethod
    def last_updated():
        """The time when the API was last updated"""

        request = requests.get("https://disease.sh/v2/all")
        corona = json.loads(request.content)
        if request.status_code != 200:
            return None
        else:
            s = corona["updated"] / 1000.0
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")
            return updated

    def flag(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["countryInfo"]["flag"]

    def total_cases(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["cases"]

    def today_cases(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["todayCases"]

    def total_deaths(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["deaths"]

