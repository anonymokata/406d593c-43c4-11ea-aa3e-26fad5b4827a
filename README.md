## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is my attempt at learning Test-Driven Development(TDD) by implementing the Pencil Durability Kata from Pillar Technology.
The primary goal of the project is to simulate a graphite pencil.
A description of the kata can be found [here](https://github.com/PillarTechnology/kata-pencil-durability)

## Technologies
This project is implemented in Python3

## Run the Project Tests
To run the project, open a cmd prompt or terminal and clone it locally using the link provided on GitHub:
```
git clone https://github.com/meggert9/PencilDurabilityKata.git
```
Once you have the project on your local machine, navigate to it in the terminal.
From there, you can run use the command line to run tests.
Use the command below to run tests for a specific test file (in this case 'test_paper.py')

```
python -m unittest test.test_paper
```
You can enter the command below to run all the tests from the test folder

```
python -m unittest discover .
```
