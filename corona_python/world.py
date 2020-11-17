import requests
import json
import datetime

request = requests.get("https://disease.sh/v2/all")
corona = json.loads(request.content)


class World:

    @staticmethod
    def last_updated():
        """
        :returns: (int) The time when the API was last updated
        """

        if request.status_code != 200:
            return None
        else:
            s = corona["updated"] / 1000.0
            updated = datetime.datetime.fromtimestamp(s).strftime("%d-%m-%Y %I:%M:%S UTC")
            return updated

    @staticmethod
    def total_cases():
        """
        :returns: (int) Number of total cases
        """

        if request.status_code != 200:
            return None
        else:
            return corona['cases']

    @staticmethod
    def today_cases():
        """
        :returns: (int) Number of the cases today
        """

        if request.status_code != 200:
            return None
        else:
            return corona['todayCases']

    @staticmethod
    def total_deaths():
        """
        :returns: (int) Number of the total deaths
        """

        if request.status_code != 200:
            return None
        else:
            return corona['deaths']

    @staticmethod
    def today_deaths():
        """
        :returns: (int) Number of the deaths today
        """

        if request.status_code != 200:
            return None
        else:
            return corona['todayDeaths']

    @staticmethod
    def recovered():
        """
        :returns: (int) Number of total recovered
        """

        if request.status_code != 200:
            return None
        else:
            return corona['recovered']

    @staticmethod
    def today_recovered():
        """
        :returns: (int) Number of the recoveries today
        """

        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def active_cases():
        """
        :returns: Number of active cases
        """

        if request.status_code != 200:
            return None
        else:
            return corona['active']

    @staticmethod
    def critical_cases():
        """
        :returns: (int) Number of critical cases
        """

        if request.status_code != 200:
            return None
        else:
            return corona['todayRecovered']

    @staticmethod
    def cases_per_one_million():
        """
        :returns: (int) Number of cases per one million
        """

        if request.status_code != 200:
            return None
        else:
            return corona['casesPerOneMillion']

    @staticmethod
    def deaths_per_one_million():
        """
        :returns: (int) Number of deaths per one million
        """

        if request.status_code != 200:
            return None
        else:
            return corona['deathsPerOneMillion']

    @staticmethod
    def total_tests():
        """
        :returns: (int) Number of total tests
        """

        if request.status_code != 200:
            return None
        else:
            return corona['tests']

    @staticmethod
    def population():
        """
        :returns: (int) Population of the world
        """

        if request.status_code != 200:
            return None
        else:
            return corona['population']

    @staticmethod
    def affected_countries():
        """
        :returns: (int) Number of affected countries
        """

        if request.status_code != 200:
            return None
        else:
            return corona['affectedCountries']

    @staticmethod
    def tests_per_one_million():
        """
        :returns: (int) Number of tests per one million people
        """

        if request.status_code != 200:
            return None
        else:
            return corona['testsPerOneMillion']

    @staticmethod
    def one_case_per_people():
        """
        :returns: (int) Number of tests per one million people
        """

        if request.status_code != 200:
            return None
        else:
            return corona['oneCasePerPeople']

    @staticmethod
    def one_deaths_per_people():
        """
        :returns: (int) Number of tests per one million people
        """

        if request.status_code != 200:
            return None
        else:
            return corona['oneCasePerPeople']