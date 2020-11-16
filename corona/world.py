import requests
import json
import datetime

request = requests.get("https://disease.sh/v2/all")
corona = json.loads(request.content)


class World:

    @staticmethod
    def last_updated():
        """The time when the API was last updated"""

        if request.status_code != 200:
            return None
        else:
            s = corona["updated"] / 1000.0
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")
            return updated

    @staticmethod
    def total_cases():
        """Number of total cases"""

        if request.status_code != 200:
            return None
        else:
            return corona['cases']

    @staticmethod
    def today_cases():
        """Number of the cases today"""

        if request.status_code != 200:
            return None
        else:
            return corona['todayCases']

    @staticmethod
    def total_deaths():
        """Number of the total deaths"""

        if request.status_code != 200:
            return None
        else:
            return corona['deaths']

    @staticmethod
    def today_deaths():
        """Number of the deaths today"""

        if request.status_code != 200:
            return None
        else:
            return corona['todayDeaths']

    @staticmethod
    def recovered():
        """Number of total recovered"""

        if request.status_code != 200:
            return None
        else:
            return corona['recovered']

    @staticmethod
    def today_recovered():
        """Number of the recoveries today"""

        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def active_cases():
        """Number of active cases"""

        if request.status_code != 200:
            return None
        else:
            return corona['active']

    @staticmethod
    def critical_cases():
        """Number of critical cases"""

        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def cases_per_one_million():
        """Number of cases per one million"""

        if request.status_code != 200:
            return None
        else:
            return corona['casesPerOneMillion']

    @staticmethod
    def deaths_per_one_million():
        """Number of deaths per one million"""

        if request.status_code != 200:
            return None
        else:
            return corona['deathsPerOneMillion']

    @staticmethod
    def total_tests():
        """Number of total tests"""

        if request.status_code != 200:
            return None
        else:
            return corona['tests']

    @staticmethod
    def population():
        """Population of the world"""

        if request.status_code != 200:
            return None
        else:
            return corona['population']

    @staticmethod
    def affected_countries():
        """Number of affected countries"""

        if request.status_code != 200:
            return None
        else:
            return corona['affectedCountries']

    @staticmethod
    def __version__():
        return "0.1.1"
