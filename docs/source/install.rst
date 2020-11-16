Getting Started
=========================================

Install
-----------------

To install corona-python, do:

.. code-block:: python
  :linenos:

  pip install corona_python

or

.. code-block:: python
  :linenos:

  python -m pip install corona_python


Examples
-----------------

.. code-block:: python
  :linenos:

  from corona_python import Country
  country = Country("USA")

  print(country.total_cases())


More examples are provided in the `examples folder <https://github.com/MakufonSkifto/corona-python/tree/main/examples>`_

Function List
-----------------

Country:

.. code-block:: python
  :linenos:

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


World:

.. code-block:: python
  :linenos:

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


More detailed explanations of the functions can be found in `Functions <https://corona-python.readthedocs.io>`_

Errors
-----------------

The module will release ``KeyError`` if the given country is invalid

If the module doesn't return anything, there might be a problem with the API