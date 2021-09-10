Introduction to SQLModel
===============

Here, a study has been made on how to write data to the database in a simple way with FastAPI, and SQLModel

### SQLModel

SQLModel is a library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.

        $ pip install sqlmodel
        
### SQL Table

First, I create a table called a train. This table will contain the following columns.

* `id`
* `fullname`
* `age`
* `gender`

and it contains sample data as below.

| id | fullname | age | gender |
-----|------|-------------|------|
| 1  | Deadpond | 24 | Male |
| 2  | Spider-Boy | 36 | Male |
| 3  | Rusty-Man | 27 | Male |
