# Library

Here is Library Project. It is built on Django Framework and MySQL. This project is my first in Django and MySQL. I was using MV Code to code and XAMPP in order to connect to 
database. I was managing database via phpMyAdmin. Due to problem with installing MySQL Client in my project, I had to install it via .whl file. 
In my project, you can register your on profile and, of course, you can log to it using email and password which you used during registration process. Library project also includes
CRUD. It is possible to create your own order (of book), read, update and, of course, delete it. After creation, there is 30 days to "return" book. That is date_end of Order.
There is also option of reset password. There is few conditions to achieve that. First of all, you must use gmail during registration with app password enabled on your gmail account. 
Second condition is enviromental variables. There must be two enviromental variables, email host username and password (names are provided at the end of settings.py file,
in get() method). 

To sum up, Library Project is my first project with Django and MySQL. It is full responsive web site (Bootstrap 4) with functionalities like registration, logging, CRUD and
password reset. This project is not finished yet. I still think of extensions like initial data, new tables in database, new layout or design. More informations soon.

Cheers!
