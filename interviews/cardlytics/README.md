## Directory Structure ##

- cardlytics
    - app
        - __init__.py
        - __pycache__
        - amazing_string.py
        - cavity_map.py
        - degree_of_array.py
        - maximize_profit.py
    - tests
        - __init__.py
        - __pycache__
        - test_amazing_string.py
        - test_cavity_map.py
        - test_degree_of_array.py
        - test_maximize_profit.py

## Each test is run with py.test and each test file coordinates to the same file name in 'app'
## Tests are run in in the same directory as 'app' and 'tests'
- py.test
- app
    - file
    - file
    - file
- tests
    - test_file
    - test_file
    - test_file

## To run the tests you will run $ py.test
## To run an individual test run $ py.test tests/test_file_name
## Another example for individual test $ py.test tests/test_degree_of_array.py
## You can edit the test file if you would like to change test data
