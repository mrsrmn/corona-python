import requests
import json
import datetime

request = requests.get("https://disease.sh/v2/all")
corona = json.loads(request.content)


class World:

    @staticmethod
    def last_updated():
        if request.status_code != 200:
            return None
        else:
            s = corona["updated"] / 1000.0
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")
            return updated

    @staticmethod
    def total_cases():
        if request.status_code != 200:
            return None
        else:
            return corona['cases']

    @staticmethod
    def today_cases():
        if request.status_code != 200:
            return None
        else:
            return corona['todayCases']

    @staticmethod
    def total_deaths():
        if request.status_code != 200:
            return None
        else:
            return corona['deaths']

    @staticmethod
    def today_deaths():
        if request.status_code != 200:
            return None
        else:
            return corona['todayDeaths']

    @staticmethod
    def recovered():
        if request.status_code != 200:
            return None
        else:
            return corona['recovered']

    @staticmethod
    def today_recovered():
        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def active_cases():
        if request.status_code != 200:
            return None
        else:
            return corona['active']

    @staticmethod
    def critical_cases():
        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def cases_per_one_million():
        if request.status_code != 200:
            return None
        else:
            return corona['casesPerOneMillion']

