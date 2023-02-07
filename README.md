![headerimg](/static/img/glow_up.png)

# [GlowUp 2021 Initial ReadMe.md](#last-updated-2021)
The following updates to my HB capstone project's ReadMe file come after returning to my project after a little more than a year.

## Revisitation thoughts and comments:
I took great pride in completing my capstone project as a part of Hackbright Academy's software engineering program. However, upon revisiting my project's GitHub repository, I realized taht I could have approached it with a greater sense of professionalism. I kindly request that you keep this in mind while reviewing my Git commit messages.

### Personal Objective: Addressing Password Vulnerabilities
As a tech enthusiast, I was motivated to enhance the security of the user login experirence for my capstone project. To mitigate the risk of storing plain text passwords in the database, I employed bCrypt to hash passwords during the registration process

The password hashing process utilizes bCrypt's `hashpw` method. The original password is converted ot bytes using `encode` and then hashed with a generated salt. The resulting hash is then decoded and stored in the database.

The `login_form` function, provided by Flask, handles the POST request for the login form. After validating the LoginForm object, the business user with the given username is retrieved. If the business user exists, bCrypt's `check_password_hash` method is used to compare the stored hashed password with the provided password. If the passwords match, the user is able to login. 


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