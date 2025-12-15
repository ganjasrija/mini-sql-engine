# mini-sql-engine
## Overview
This is a small SQL engine I built using Python.  
It can load data from CSV files and run basic SQL queries from the command line.  
The goal of this project was to understand how databases work behind the scenes, like selecting columns, filtering rows, and counting values, without using an actual database.  
---

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone this repository:
```bash
git clone https://github.com/ganjasrija/mini-sql-engine.git 
```
3.Go into the project folder:
```bash
cd mini-sql-engine
```
4.Run the program with a CSV file:
```bash
python cli.py data/people.csv
```
4.You will see this prompt:
```bash
Mini SQL Engine (type 'exit' to quit)
mini-sql>
```

6.Now you can type SQL commands and press Enter.

7.To close the program, type:
```bash
exit
```
---
## Supported SQL Commands

These are the queries my engine can handle:

1. **Select all columns**
 ```sql
SELECT * FROM table_name;
```
## Example
 ```sql
mini-sql> SELECT * FROM people;
{'id': '1', 'name': 'Alice', 'age': '30', 'country': 'USA'}
{'id': '2', 'name': 'Bob', 'age': '25', 'country': 'India'}
{'id': '3', 'name': 'Charlie', 'age': '35', 'country': 'USA'}
{'id': '4', 'name': 'David', 'age': '', 'country': 'UK'}
(4 rows)
```
2. **Select specific columns**
 ```sql
SELECT column1, column2 FROM table_name;
```
## Example
``` sql
mini-sql> SELECT name, age FROM people;
{'name': 'Alice', 'age': '30'}
{'name': 'Bob', 'age': '25'}
{'name': 'Charlie', 'age': '35'}
{'name': 'David', 'age': ''}
(4 rows)
```

3. **Filter rows with WHERE (single condition only)**
 ```sql
SELECT * FROM table_name WHERE column_name > 25;
SELECT column1, column2 FROM table_name WHERE column_name = 'USA';

```
## Example1
``` sql
mini-sql> SELECT * FROM people WHERE age > 25;
{'id': '1', 'name': 'Alice', 'age': '30', 'country': 'USA'}
{'id': '3', 'name': 'Charlie', 'age': '35', 'country': 'USA'}
(2 rows)

```
## Example2
``` sql
mini-sql> SELECT name, country FROM people WHERE country = 'USA';
{'name': 'Alice', 'country': 'USA'}
{'name': 'Charlie', 'country': 'USA'}
(2 rows)

```
4. **COUNT() function**
 ```sql
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name;
```
## Example1
``` sql 
mini-sql> SELECT COUNT(*) FROM people;
COUNT = 4

```
## Example2
``` sql
mini-sql> SELECT COUNT(age) FROM people;
COUNT = 3

```
**Notes:**

- Only one condition is allowed in the WHERE clause.

- Supported operators: =, !=, >, <, >=, <=.

- COUNT(column_name) counts only non-empty values.
---



## Project Structure

- mini-sql-engine/
  - cli.py         Runs the command-line interface
  - parser.py      Handles parsing of SQL queries
  - engine.py      Executes queries and aggregation
  - loader.py      Loads CSV data into memory
  - data/          Folder containing CSV files
    - people.csv   Example CSV file
  - README.md      This file
  - .gitignore     Git ignore file


---

## Error Handling

The engine gives clear messages for errors, for example:

- **If the SQL syntax is wrong:**
    ```sql
    mini-sql> SELECT FROM people;
    Error: Invalid SQL syntax
    ```

- **If a column does not exist:**
    ```sql
    mini-sql> SELECT abc FROM people;
    Error: Column 'abc' does not exist
    ```

- **If you filter on a column that does not exist:**
    ```sql
    mini-sql> SELECT * FROM people WHERE salary > 50000;
    Error: Column 'salary' does not exist
    ```
