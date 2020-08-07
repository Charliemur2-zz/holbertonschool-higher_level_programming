<img src="https://www.fullstackpython.com/img/visuals/orms-bridge.png">

# 0x0F. Python - Object-relational mapping

n this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

### TASKS ###
0. Get all states mandatory
Write a script that lists all states from the database hbtn_0e_0_usa
1. Filter states mandatory
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
2. Filter states by user input mandatory
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
3. SQL Injection... mandatory
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
4. Cities by states mandatory
Write a script that lists all cities from the database hbtn_0e_4_usa
5. All cities by state mandatory
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
6. First state model mandatory
Write a python file that contains the class definition of a State and an instance Base = declarative_base():




---

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)


---


## Installation

Copy the code, compile (if is necessary), and execute it.

---

### Setup

---

## Features
## Usage 

See the codes of different functions and programs.

## Documentation 

<a href="https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA">`Object-relational mappers`</a><br>
<a href="https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw">`mysqlclient/MySQLdb documentation `</a><br>
<a href="https://intranet.hbtn.io/rltoken/KskI6xMlQCYJyE0UVPJfKQ">`MySQLdb tutorial`</a><br>
<a href="https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ">`SQLAlchemy tutorial`</a><br>
<a href="https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA">`SQLAlchemy`</a><br>
<a href="https://intranet.hbtn.io/rltoken/SSoBE3ckyGFi3NexCH3nuw">`mysqlclient/MySQLdb`</a><br>
<a href="https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg">`Introduction to SQLAlchemy`</a><br>
<a href="https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A">`Flask SQLAlchemy`</a><br>
<a href="https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw">`10 common stumbling blocks for SQLAlchemy newbies`</a><br>
<a href="https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw">`Python SQLAlchemy Cheatsheet`</a><br>
<a href="https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw">`SQLAlchemy ORM Tutorial for Python Developers`</a><br>

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using 

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using. 
---

## Team

https://github.com/Charliemur2
---

## Support

Feel free to contact me!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Insert more social links here.

---

## License

Free Source Code
