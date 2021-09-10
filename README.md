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

Using a form written in HTML, we write the data we receive from the user to the database with a very short code. The data entered in the form will be written to our database via FastAPI.

To access the codes of the html form: <a href="https://github.com/ahmtcnbs/IntroSQLModel/blob/master/index.html">Click Here</a>

For database write operation and api: <a href="https://github.com/ahmtcnbs/IntroSQLModel/blob/master/main.py">Click Here</a>

For an introduction to databases, SQL, and everything else, see the <a href="https://sqlmodel.tiangolo.com" target="_blank">SQLModel documentation</a>.

