[![Documentation Status](https://readthedocs.org/projects/corona-python/badge/?version=latest)](https://corona-python.readthedocs.io/en/latest/?badge=latest) [![License](https://img.shields.io/github/license/MakufonSkifto/corona-python)](LICENSE.md) [![GitHub stars](https://img.shields.io/github/stars/MakufonSkifto/corona-python)](https://github.com/ExpDev07/coronavirus-tracker-api/stargazers) [![PyPI version](https://badge.fury.io/py/corona-python.svg)](https://badge.fury.io/py/corona-python)

 

# corona_python
A Python API Wrapper for coronavirus stats

## Installation

To install corona-python, do:

`pip install corona-python`

or 

`python -m pip install corona-python`

## Usage
```python
from corona_python import Country
country = Country("USA")

print(country.total_cases())
```

More examples are provided in the [examples folder](https://github.com/MakufonSkifto/corona-python/tree/main/examples)

## Documentation

Documentation can be found [here](https://corona-python.readthedocs.io)

## Functions

Country:
```
last_updated()
flag()
total_cases()
today_cases()
total_deaths()
today_deaths()
recovered()
today_recovered()
active()
critical()
cases_per_one_million()
deaths_per_one_million()
total_tests()
tests_per_one_million()
population()
continent()
one_case_per_people()
one_death_per_people()
one_test_per_people()
```

World:
```
last_updated()
total_cases()
today_cases()
total_deaths()
today_deaths()
recovered()
today_recovered()
active_cases()
critical_cases()
cases_per_one_million()
deaths_per_one_million()
total_tests()
population()
affected_countries()
tests_per_one_million()
one_case_per_people()
one_death_per_people()
one_test_per_people()
active_per_million()
recovered_per_million()
critical_per_million()
```

More detailed explanations of the functions can be found in [the docs](https://corona-python.readthedocs.io)

## Errors

The module will raise ``KeyError`` if the given country is invalid

If the module doesn't return anything, there might be a problem with the API. To report the problem, contact me, the developer or create an issue.
