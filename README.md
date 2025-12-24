# Python Lab

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![APIs & HTTP](https://img.shields.io/badge/Tools-APIs_&_HTTP_Requests-2C3E50?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Notebooks-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Python_Fundamentals_&_Data_Workflows-0A66C2?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-8_Structured_Modules-8E44AD?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/danij4ne/python-lab?style=for-the-badge)
![Commit Activity](https://img.shields.io/github/commit-activity/m/danij4ne/python-lab?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2ECC71?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-1D8348?style=for-the-badge)

Python Lab is a structured repository designed to consolidate foundational and intermediate Python programming concepts, including control flow, functions, data collections, object-oriented programming, exception handling, file operations, numerical computing with NumPy, tabular data processing with pandas,  HTTP/API workflows and local database interaction with SQLite.
Each module contains standalone scripts and exercises that focus on a specific functional area of the Python programming ecosystem.

---

## Repository Structure

```
01_basics/
02_functions/
03_collections/
04_oop/
05_exceptions_and_files/
06_numpy/
07_pandas/
08_apis_scraping/
09_sql_and_databases/
README.md
```

---

## Tools and Dependencies

The repository contains modules that rely on both Python standard-library components and external packages.
The tools used across modules include:

### Standard Library

- os – file-path management and directory handling
- json – JSON serialization and deserialization
- xml.etree.ElementTree – parsing XML files
- glob – file pattern matching where applicable
- random – value generation for numerical workflows

### External Libraries

- NumPy – numerical arrays, vectorized operations, matrix structures
- pandas – tabular data processing, DataFrame structures, CSV/Excel operations
- requests – HTTP client for GET/POST requests and API interaction
- Pillow (PIL.Image) – image loading when handling downloaded files
- Jupyter (.ipynb notebooks) – interactive analysis and documented walkthroughs

Each module specifies its relevant imports within the scripts and notebooks.

---

# Module Overview

## 01 — Basics

This module focuses on the essential elements of Python execution flow.

### Purpose

To present core procedural constructs and foundational syntax.

### Concepts Addressed

- Basic input/output
- Arithmetic and logical operations
- Conditional structures
- Looping constructs

### Practical Use

Provides the fundamental blocks required for more advanced modules such as functions, collections, and file handling.

### Exercises

- Basics.py
- ex_conditions.py
- ex_loops_for_while.py
- loops_for_while.py

### Module Summary

The module establishes the procedural backbone used throughout the repository and serves as the entry point for Python's imperative programming style.

---

## 02 — Functions

This module covers user-defined functions and functional-style utilities.

### Purpose

To maintain a clear separation of behavior through reusable callable units.

### Concepts Addressed

- Function definitions
- Parameters and return values
- Scope rules
- Anonymous functions via lambda

### Practical Use

Useful for structuring script behavior, encapsulating logic, and supporting modular development.

### Exercises

- functions_def.py
- ex_functions_def.py
- lambda_exercises.py

### Module Summary

This module organizes function-level logic and establishes conventions for clean procedural abstraction.

---

## 03 — Collections

This module focuses on Python’s primary container types and comprehension forms.

### Purpose

To document structured data containers and their manipulation patterns.

### Concepts Addressed

- Lists, tuples, sets, dictionaries
- Collection methods and operations
- List/set/dict comprehensions
- Mutability rules and data access patterns

### Practical Use

Essential for dataset management, transformation steps, and core algorithmic operations.

### Exercises

- lists_tuples.py
- dictionaries.py
- sets.py
- comprehensions.py
- ex_lists_tuples.py
- ex_lists_tuples_sets_dict.py
- ex_comprehensions.py

### Module Summary

Provides complete coverage of Python’s primary data structures and supports transformation logic across the repository.

---

## 04 — Object-Oriented Programming

This module introduces Python’s class-based programming model.

### Purpose

To demonstrate structured modeling through classes and object instances.

### Concepts Addressed

- Class definitions
- Attributes and methods
- Object instantiation
- Encapsulation patterns

### Practical Use

Supports scalable program design and mirrors structures used in professional applications.

### Exercises

- classes_and_objects.py
- ex_classes_and_objects.py

### Module Summary

Defines object-structured logic that expands program organization beyond procedural code.

---

## 05 — Exceptions and Files

This module handles error management and file system interaction.

### Purpose

To formalize controlled error handling and consistent file I/O workflows.

### Concepts Addressed

- Exception classes and structured exception blocks
- Reading and writing text files
- File iteration patterns
- Working with multiple formats: CSV, JSON, XML
- Managing file pointers and resource control via with open

### Practical Use

Critical for safe data processing workflows, log handling, and text-based dataset operations.

### Exercises

- exception_handling.py
- ex_exception_handling.py
- file_open.py
- ex_file_open.py
- work_with_different_formats.py
- ex_work_with_different_formats.ipynb
- with_open.ipynb

### Module Summary

Combines structured exception management with practical file operations, forming the backbone of many data-processing tasks.

---

## 06 — NumPy

This module focuses on numerical computing and vectorized operations.

### Purpose

To document array-based computation patterns used in scientific and analytical workflows.

### Concepts Addressed

- One-dimensional and two-dimensional arrays
- Vectorized arithmetic
- Reductions and descriptive statistics
- Array reshaping and matrix operations

### Practical Use

Forms the computational layer for numerical tasks, matrix logic, and data transformation.

### Exercises

- numpy_basics.py
- numpy_basics.ipynb
- numpy_two_dimensional.ipynb
- ex_numpy.py

### Module Summary

Supports efficient numerical computation through structured array systems.

---

## 07 — Pandas

This module provides structured tabular data processing.

### Purpose

To organize and manipulate row-column data through DataFrame operations.

### Concepts Addressed

- CSV/Excel ingestion
- DataFrame indexing and selection
- Filtering, sorting, and grouping
- Descriptive statistics
- Export workflows

### Practical Use

Serves as the primary tool for structured data pipelines and file-driven analysis.

### Exercises

- pandas_basics.py
- training_with_pandas.ipynb
- ex_pandas.py
- pandas_numpy_open_cheatsheet.py

### Module Summary

Documents core DataFrame operations widely used in analytics and data-engineering workflows.

---

## 08 — APIs and Scraping

This module covers HTTP requests and introductory web scraping.

### Purpose

To interact with external data sources and APIs through HTTP operations.

### Concepts Addressed

- GET and POST requests
- Request headers and parameters
- JSON API consumption
- Basic scraping logic
- Local file handling for downloaded data

### Practical Use

Useful for acquiring external datasets and integrating API-based sources into broader workflows.

### Exercises

- apis/get_post_requests_and_scraping.ipynb
- apis/exploring_randomuser_fruityvice_openjoke_apis.ipynb
- apis/coingecko_basic_request.ipynb
- scraping/web_scraping.ipynb
- data/ sample text files
- roadmap/python_learning_roadmap_all_blocks.ipynb
- roadmap/python_learning_roadmap_all_blocks.py

### Module Summary

Encapsulates API-based extraction, preliminary scraping patterns, and auxiliary datasets used in interactive notebooks.

---



## 09 — SQL and Databases (SQLite + pandas + Jupyter)

This module covers the integration of Python with relational databases using SQLite, pandas, and Jupyter notebooks.  
It reflects real data-engineering and analytics workflows, from low-level database connections to SQL-driven analysis and real dataset exploration.

### Purpose

To provide a complete introduction to database programming from Python, including SQL execution, DataFrame-based querying, and lightweight data pipelines built on SQLite.

### Concepts Addressed

- SQLite database fundamentals (file-based relational storage)
- Database connections and cursor-based SQL execution
- Creating, reading, updating, and querying tables from Python
- Using pandas as a SQL interface (`read_sql`, `to_sql`)
- Jupyter SQL magic for interactive SQL analysis
- Real dataset ingestion and exploration using SQLite

### Practical Use

This module mirrors real-world Data Engineering and Analytics tasks such as:
- Loading structured datasets into relational databases
- Executing SQL queries from Python
- Validating transformations through record counts and filters
- Combining SQL, pandas, and notebooks for exploratory data workflows

### Module Structure

```
09_sql_and_databases/
│
├── 01_sqlite_basics/
│ ├── 00_sqlite_basics.py
│ ├── sqlite_connection_and_cursor.py
│ └── sql_magic.py
│
├── 02_sqlite_with_pandas/
│ └── sqlite_insert_update_select_pandas.ipynb
│
├── 03_sql_magic_notebooks/
│ └── sql_magic_sqlite_from_zero.ipynb
│
├── 04_real_projects/
│ └── chicago_sqlite_python_learning_guide.ipynb
│
└── staff_lab/
├── INSTRUCTOR.csv
└── lab_staff_database.py
```

### Module Summary

This module provides a full SQLite-based data workflow: from low-level SQL execution with cursors, to pandas-powered querying, to real-world notebook projects built on relational data — forming a strong foundation for Data Engineering and Analytics pipelines.

---

## Conventions and Standards

- English file naming is used throughout the repository.
- Each module organizes its scripts, exercises, and notes consistently.
- Notebook files (.ipynb) provide walkthroughs, while .py files contain script-based implementations.
- All modules avoid instructional guidelines and instead describe their internal structure and responsibilities.

---

## Author

Daniel Jane Garcia (danij4ne)
