![headerimg](/static/img/glow_up.png)

#### [GlowUp 2021 Initial ReadMe.md](#last-updated-2021)
The following updates to my HB capstone project's ReadMe file come after returning to my project after a little more than a year.

## Revisitation thoughts and comments:
I took great pride in completing my capstone project as a part of Hackbright Academy's software engineering program. However, upon revisiting my project's GitHub repository, I realized taht I could have approached it with a greater sense of professionalism. I kindly request that you keep this in mind while reviewing my Git commit messages.

### Personal Objective: Addressing Password Vulnerabilities
As a tech enthusiast, I was motivated to enhance the security of the user login experirence for my capstone project. To mitigate the risk of storing plain text passwords in the database, I employed bCrypt to hash passwords during the registration process

The password hashing process utilizes bCrypt's `hashpw` method. The original password is converted ot bytes using `encode` and then hashed with a generated salt. The resulting hash is then decoded and stored in the database.

The `login_form` function, provided by Flask, handles the POST request for the login form. After validating the LoginForm object, the business user with the given username is retrieved. If the business user exists, bCrypt's `check_password_hash` method is used to compare the stored hashed password with the provided password. If the passwords match, the user is able to login. 

### From Backend to Frontend
#### `model.py`
This code is a part of a loyalty program project built using Python and Flask. It defines the database schema using SQLAlchemy, the ORM used for interacting with the database. The code defines a table business_users which stores information about business users such as email, username, password, name, business, and a picture path. The code also defines the class BusinessUser as a model for the table.
#### `crud.py`
Contains functions to manage the business user and client data for the rewards program application.

The functions use the SQLAlchemy ORM to interact with the database and manipulate the objects of the BusinessUser, Client, Transaction, ClientReward, and Reward models.

Some of the functions include:

- `create_business_user`: to create a new business user with given information (email, username, password, name, business, and profile picture path). **The ***password is hashed using bcrypt*** before being stored in the database.**
- `show_all_business_user`, `get_business_user_by_id`, `get_business_user_by_username`, `get_business_user_by_email`: functions to retrieve information about business users from the database
- `create_client`: to create a new client for a business user with given information (name, email, and associated business user).
- `show_all_client`, `get_client_by_id`, `get_client_by_email`: functions to retrieve information about clients from the database
- `adjust_client_points`: to adjust the reward points for a client with a given client ID by the specified reward points.

#### `seed_database.py`
Script for populating PostgreSQL database for the loyalty rewards program. It does the following steps:

- Drops and creates a new database called "loyalty" using the os.system function.

- Connects to the database using the model module and creates the necessary tables using `model.db.create_all()`.

- From file `data/bu_dummydata.json`, using json module and crud module to add to database:
    - Loads business user data and creates business users

    - Loads client data and creates clients, with each client randomly assigned to a business user.

    - Loads transaction data and creates transactions, with each transaction randomly assigned to a client.

    - Loads reward data and creates rewards, with each reward randomly assigned to a business user.

    - Creates client-reward associations by randomly assigning rewards to clients.

#### `server.py`
A Python Flask web application that provides a web interface for users to register, login and logout of the application. The application uses the Flask framework, the Flask-Login library for handling user authentication, the Flask-WTF library for form handling, and the Flask-Bcrypt library for password hashing. The application also uses a database (via the model.py file and the crud module) to store information about registered business users. The code implements forms for user registration and login, and also sets up login manager for handling user authentication.


# Last updated 2021
# GlowUp - customer loyalty app
Glow Up is a web application inspired by my sister's dream, of expanding her 
business as an aesthetician. In her particular instance, my sister wanted to offer
a free service after a customer's 10th visit. She had been tallying them down in
a notebook. So I thought, why not automate that?

This points based loyalty program is geared towards the small business owners
in the spa, aesthetician, & beauty industry.

## Introduction 
GlowUp reflects the culmination of knowledge and experience gained from my time
at Hackbright Academy. This project was completed in a 4 week time frame, in which
I was able to implement the features in my MVP as well as further development with 
my 2.0. 

After experiencing "coding bootcamp burnout" post Hackbright,
I had left this project unattended. As of February 28th, 2022, this is an ongoing 
fullstack project I hope to deploy by April 2022.

## Table of Contents
* [Technologies Used](#technologiesused)
* [How to locally run GlowUp](#localrun)
* [How to use There and Back Again](#use)
* [Project Status](#projectstatus)
* [Data Model](#datamodel)
* [About Me](#aboutme)

## General Info 
This project is a customer loyalty rewards programs, tallying up customer points
to redeem later a service chosen by the business owner.

Web app is very user friendly and self-explanatory. 

    - Register as user (or alternatively, login with a sample username and password 
    available in data file--bu_dummydata.json)
    - Add client profiles
    - In a client's profile, 
        - adjust client reward points (adding and "redeeming" need to be entered manually)
        - add client transactions
    - Add/delete rewards (enter reward name and number of points required)
    


## <a name="technologiesused"></a>Technologies Used 
- Python 
- JavaScript
- AJAX
- JSON
- HTML
- CSS
- Flask
- jQuery
- Bootstrap
- Jinja2
- bcrypt
- WTForms
- PostgreSQL
- SQLAlchemy


## <a name="localrun"></a>How to locally run GlowUp
* Create a virtual environment, activate it, and install GlowUp's dependences from requirements.txt
    * `virtualenv env`
    * `source env/bin/activate`
    * `pip install -r requirements.txt`

* Create PostgreSQL database
    * `createdb loyalty`

* Create tables in your database
    * `python -i model.py`
    * In interative mode, create tables: `db.create_all()`

* Run CRUD file and seed database
    * `python3 crud.py`
    * Seed database with dummy data (fake business users, clients, rewards, transactions): 
        *`python3 seed_database.py`

* Enter localhost:5000 in browser to see web app
   

## <a name="datamodel"></a>Data Model 

![data_model_loyalty](/static/img/data_model.png)

# <a name="projectstatus"></a>Project Status 
As of February 28th, 2022, the project is undergoing revisions for cleaner and
more concise code. I plan to implement new features I did not have the time
or knowledge to execute before the hard code freeze for my cohort's demo night.

## <a name="aboutme"></a>About me
Shane Jeon, a software engineer from a non-traditional background with a strong
resolve to demonstrate how an individual can overcome past struggles and start
carving a new path through tech.