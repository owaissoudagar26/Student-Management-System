# Student-Management-System
A simple Student Management System built with Python + MySQL. It supports adding, displaying student records with subject-wise marks (English, Maths, Science, SST, Hindi).
Project Title

Student Management System (Python + MySQL)

Description

This is a Command Line Interface (CLI) project that manages student records using Python and MySQL.
It demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on a database.

Features

Add a new student (Roll No, Name, Department, Marks for 5 subjects)

Display all students with subject-wise marks


Technologies Used

Python 3

MySQL (database)

mysql-connector-python library

How to Run

Clone this repo or download the code.

Install required package:

pip install mysql-connector-python

Create database and table in MySQL:

CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    English INT,
    Maths INT,
    Science INT,
    SST INT,
    Hindi INT
);


Run the program:

python student_db.py

Screenshots:

<img width="1061" height="942" alt="image" src="https://github.com/user-attachments/assets/98f5cec6-d06a-4930-b977-fe4b2a86e63d" />

What I Learned

How to connect Python with MySQL using mysql-connector-python

Writing SQL queries inside Python

Implementing CRUD operations

Structuring a menu-based CLI project
