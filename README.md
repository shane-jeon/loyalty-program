![headerimg](/static/img/glow_up.png)

# GlowUp - customer loyalty app
Glow Up is created with VScode

This project was inspired by my sister's dream, of expanding her business as an aesthetician. After her clients get 10 
facials, they get 1 for free. She had been tallying them down in a notebook. Why not automate that?

Thus, this points based loyalty program is geard towards the small business owner of the spa & aesthetician community.

## Introduction 
The GlowUp web app is the culmination of my bootcamp experience. My Hackbright capstone project, GlowUp reinforced all information that the bootcamp has stuffed into my brain within the bootcamp's limited time frame.

## Table of Contents
* [Technologies Used](#technologiesused)
* [How to locally run GlowUp](#localrun)
* [How to use There and Back Again](#use)
* [Project Status](#projectstatus)
* [Data Model](#datamodel)
* [About Me](#aboutme)

## General Info 
This project is a customer loyalty rewards programs, tallying up customer points to redeem later on for rewards promoted by the business user.

Web app is very user friendly and self-explanatory. 

    - Register as user (or alternatively, input username and password available in data file--bu_dummydata.json)
    - Add clients
    - In client profile, 
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

    Baby's first data model

![data_model_loyalty](/static/img/data_model.png)

# <a name="projectstatus"></a>Project Status 
Still a work in progress...

## <a name="aboutme"></a>About me
Shane Jeon is a budding software engineer in Oakland, CA.