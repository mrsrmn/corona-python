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

    def today_deaths(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["todayDeaths"]

    def recovered(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["recovered"]

    def today_recovered(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["todayRecovered"]

    def active(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["active"]

    def critical(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["deaths"]

    def cases_per_one_million(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["casesPerOneMillion"]

    def deaths_per_one_million(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["deathsPerOneMillion"]

    def total_tests(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["tests"]

    def tests_per_one_million(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["testsPerOneMillion"]

    def population(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["population"]

    def continent(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["continent"]

    def one_case_per_people(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["oneCasePerPeople"]

    def one_death_per_people(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["oneDeathPerPeople"]

    def one_test_per_people(self):
        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            return None
        else:
            return corona["oneTestPerPeople"]
