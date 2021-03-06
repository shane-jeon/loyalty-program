![headerimg](/static/img/glow_up.png)

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