# Solent Campers  
A full fledged Solent Campers implemented in Python using object oriented programming.

## Advisors can 

* See available vans and camping sites.
* Book vans on behalf of customers.
* Return vans on behalf of customers.
* Book camping sites on behalf of customers.
* Cancel camping sites booking on behalf of customers.

For simplicity we assume that there is only one customer at a given moment. However requested vans(small/medium/large) should be less than available stock and requested camping sites should be there in available camping sites list. The cancellation of camping sites will cancel all the camping sites booking made by the customer.

## Customers can

* See their booking deatils of vans and camping sites.
  
The booking summary can be seen in json or csv format.

## Administrator can 

* Add the vans and camping sites.
* Remove vans and camping sites.

By default, there will be -10 small vans, 10 medium vans, 10 large vans ; camping sites - ['London','Oxford','Glasgow','Manchester'] at the beginning of the application.

## Unit-Test

Test module is written alongside the main program to rigorously test the classes and methods for errors.
Most of them have been taken care of.

## Running the tests

To run the tests, 

- Python 3.8+: `pytest-3 UnitTests.py`

Alternatively, you can tell Python to run the pytest module:
`python3 -m pytest UnitTests.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

## How to run?
This code is written in python3.9.
The entry point to the application is main.py.

Simply run
``` 
python3 main.py
```