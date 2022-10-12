# Pharmacy-Management-System-Python-tkinter-MSSQL-DBMS
This project uses tkinter (a library of python) for the GUI and MySQL for storing data.

-------Tools---------
Following tools are required to run this code:
1) Python Interpretor such as pycharm
2) Microsoft SQL Server Management Studio

-------Libraries---------
Make sure following libraries are installed on python Interpretor:
- tkinter
- pypyobdc / pyobdc

-------Database Setup---------
Before Running the code :

- create a database named as 'Pharmacy Management System' in MS SQL:

- create table inside this database using the following code:

create table pharma(
ref_no INT PRIMARY KEY NOT NULL,
comp_name varchar(60),
typ varchar(60),
med_name varchar(60),
lot_no varchar(60),
issue varchar(60),
expire varchar(60),
uses varchar(60),
side_eff varchar(60),
price varchar(60),
)

-------Server Name---------
Make sure you assign sever name from MS SQL (which is usually name of your pc/laptop)
to a string self.server_name (line:252) inside function named 'connect_database'
