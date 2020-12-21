class All:
    def __init__(self, updated, cases, today_cases, deaths, today_deaths, recovered, today_recovered, active, critical,
                 cases_per_one_million, deaths_per_one_million, tests, tests_per_one_million, population,
                 one_case_per_people, one_death_per_people, one_test_per_people, active_per_one_million,
                 recovered_per_one_million, critical_per_one_million, affected_countries):
        self.updated = updated
        self.cases = cases
        self.today_cases = today_cases
        self.deaths = deaths
        self.today_deaths = today_deaths
        self.recovered = recovered
        self.today_recovered = today_recovered
        self.active = active
        self.critical = critical
        self.cases_per_one_million = cases_per_one_million
        self.deaths_per_one_million = deaths_per_one_million
        self.tests_per_one_million = tests_per_one_million
        self.tests = tests
        self.population = population
        self.one_case_per_people = one_case_per_people
        self.one_death_per_people = one_death_per_people
        self.one_test_per_people = one_test_per_people
        self.active_per_one_million = active_per_one_million
        self.recovered_per_one_million = recovered_per_one_million
        self.critical_per_one_million = critical_per_one_million
        self.affected_countries = affected_countries
