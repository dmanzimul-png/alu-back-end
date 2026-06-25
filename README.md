PI

## Description

This project demonstrates how to interact with a REST API using Python. The scripts retrieve employee TODO list information from the JSONPlaceholder API and export the data into different formats such as CSV and JSON.

## Learning Objectives

By completing this project, I learned:

* What an API is
* What a REST API is
* What microservices are
* How to consume APIs using Python
* How to work with JSON and CSV data formats
* How to use the `requests` module
* How to organize and export data in Python
* Python coding standards following PEP 8

## Requirements

* Ubuntu 14.04 LTS
* Python 3.4.3
* requests module
* PEP 8 compliant code

## Files

| File                                    | Description                                             |
| --------------------------------------- | ------------------------------------------------------- |
| 0-gather_data_from_an_API.py            | Retrieves and displays an employee's TODO list progress |
| 1-export_to_CSV.py                      | Exports an employee's TODO list to CSV format           |
| 2-export_to_JSON.py                     | Exports an employee's TODO list to JSON format          |
| 3-dictionary_of_list_of_dictionaries.py | Exports all employees' TODO lists to a single JSON file |

## API Endpoints Used

### Users

https://jsonplaceholder.typicode.com/users

### Todos

https://jsonplaceholder.typicode.com/todos

## Usage

### Task 0

```bash
python3 0-gather_data_from_an_API.py 2
```

### Task 1

```bash
python3 1-export_to_CSV.py 2
```

### Task 2

```bash
python3 2-export_to_JSON.py 2
```

### Task 3

```bash
python3 3-dictionary_of_list_of_dictionaries.py
```

## Author

Manzi Elvis

