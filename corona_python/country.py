import requests
import json
import datetime


class Country:
    def __init__(self, country):
        self.country = country

    @staticmethod
    def last_updated():
        """
        :returns: (int) The time when the API was last updated
        """

        request = requests.get("https://disease.sh/v2/all")
        corona = json.loads(request.content)
        if request.status_code != 200:
            pass
        else:
            s = corona["updated"] / 1000.0
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")
            return updated

    def flag(self):
        """
        :returns: (str) The image link to the flag of the country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["countryInfo"]["flag"]

    def total_cases(self):
        """
        :returns: (int) Number of the total cases in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["cases"]

    def today_cases(self):
        """
        :returns: (int) Number of the total cases today in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["todayCases"]

    def total_deaths(self):
        """
        :returns: (int) Number of the total deaths in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["deaths"]

    def today_deaths(self):
        """
        :returns: (int) Number of the total deaths today in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["todayDeaths"]

    def recovered(self):
        """
        :return: (int) Number of the total recoveries in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["recovered"]

    def today_recovered(self):
        """
        :return: (int) Number of the total recoveries today in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["todayRecovered"]

    def active(self):
        """
        :return: (int) Number of the active cases in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["active"]

    def critical(self):
        """
        :return: (int) Number of the critical cases in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["deaths"]

    def cases_per_one_million(self):
        """
        :return: (int) Number of the cases per one million in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["casesPerOneMillion"]

    def deaths_per_one_million(self):
        """
        :return: (int) Number of the deaths per one million in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["deathsPerOneMillion"]

    def total_tests(self):
        """
        :return: (int) Number of the total tests in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["tests"]

    def tests_per_one_million(self):
        """
        :return: (int) Number of the tests per one million in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["testsPerOneMillion"]

    def population(self):
        """
        :return: (int) Number residents in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["population"]

    def continent(self):
        """
        :return: (str) The continent of the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["continent"]

    def one_case_per_people(self):
        """
        :return: (int) Number of the one cases per people in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["oneCasePerPeople"]

    def one_death_per_people(self):
        """
        :return: (int) Number of the one deaths per people in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["oneDeathPerPeople"]

    def one_test_per_people(self):
        """
        :return: (int) Number of the one tests per people in the specified country
        """

        request = requests.get(f"https://disease.sh/v2/countries/{self.country.replace(' ', '%20')}")
        corona = json.loads(request.content)

        if request.status_code != 200 and request.status_code != 404:
            pass
        else:
            return corona["oneTestPerPeople"]
