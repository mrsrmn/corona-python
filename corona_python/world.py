import requests
import json
import datetime
from .all import All

request = requests.get("https://disease.sh/v2/all")
corona = json.loads(request.content)


class World:

    @staticmethod
    def last_updated():
        """
        :returns: (int) The time when the API was last updated
        """

        if request.status_code != 200:
            pass
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
            pass
        else:
            return corona['cases']

    @staticmethod
    def today_cases():
        """
        :returns: (int) Number of the cases today
        """

        if request.status_code != 200:
            pass
        else:
            return corona['todayCases']

    @staticmethod
    def total_deaths():
        """
        :returns: (int) Number of the total deaths
        """

        if request.status_code != 200:
            pass
        else:
            return corona['deaths']

    @staticmethod
    def today_deaths():
        """
        :returns: (int) Number of the deaths today
        """

        if request.status_code != 200:
            pass
        else:
            return corona['todayDeaths']

    @staticmethod
    def recovered():
        """
        :returns: (int) Number of total recovered
        """

        if request.status_code != 200:
            pass
        else:
            return corona['recovered']

    @staticmethod
    def today_recovered():
        """
        :returns: (int) Number of the recoveries today
        """

        if request.status_code != 200:
            pass
        else:
            return corona['todayRecovered']

    @staticmethod
    def active_cases():
        """
        :returns: Number of active cases
        """

        if request.status_code != 200:
            pass
        else:
            return corona['active']

    @staticmethod
    def critical_cases():
        """
        :returns: (int) Number of critical cases
        """

        if request.status_code != 200:
            pass
        else:
            return corona['todayRecovered']

    @staticmethod
    def cases_per_one_million():
        """
        :returns: (int) Number of cases per one million
        """

        if request.status_code != 200:
            pass
        else:
            return corona['casesPerOneMillion']

    @staticmethod
    def deaths_per_one_million():
        """
        :returns: (int) Number of deaths per one million
        """

        if request.status_code != 200:
            pass
        else:
            return corona['deathsPerOneMillion']

    @staticmethod
    def total_tests():
        """
        :returns: (int) Number of total tests
        """

        if request.status_code != 200:
            pass
        else:
            return corona['tests']

    @staticmethod
    def population():
        """
        :returns: (int) Population of the world
        """

        if request.status_code != 200:
            pass
        else:
            return corona['population']

    @staticmethod
    def affected_countries():
        """
        :returns: (int) Number of affected countries
        """

        if request.status_code != 200:
            pass
        else:
            return corona['affectedCountries']

    @staticmethod
    def tests_per_one_million():
        """
        :returns: (int) Number of tests per one million people
        """

        if request.status_code != 200:
            pass
        else:
            return corona['testsPerOneMillion']

    @staticmethod
    def one_case_per_people():
        """
        :returns: (int) Number of cases per one person
        """

        if request.status_code != 200:
            pass
        else:
            return corona['oneCasePerPeople']

    @staticmethod
    def one_death_per_people():
        """
        :returns: (int) Number of deaths per one person
        """

        if request.status_code != 200:
            pass
        else:
            return corona['oneDeathPerPeople']

    @staticmethod
    def one_test_per_people():
        """
        :returns: (int) Number of one tests per one person
        """

        if request.status_code != 200:
            pass
        else:
            return corona['oneTestPerPeople']

    @staticmethod
    def active_per_million():
        """
        :returns: (int) Number of active cases per one million people
        """

        if request.status_code != 200:
            pass
        else:
            return corona['activePerOneMillion']

    @staticmethod
    def recovered_per_million():
        """
        :returns: (int) Number of recovered cases per one million people
        """

        if request.status_code != 200:
            pass
        else:
            return corona['recoveredPerOneMillion']

    @staticmethod
    def critical_per_million():
        """
        :returns: (int) Number of critical cases per one million people
        """

        if request.status_code != 200:
            pass
        else:
            return corona['criticalPerOneMillion']

    @staticmethod
    def get_all():
        """
        :returns: (str) Returns the full data in JSON format
        """

        if request.status_code != 200:
            pass
        else:
            return All(

            )
