## Project Proposal

### Overview


app for small business owners to create simple loyalty program
(much like a cafe punch card--buy 10 drinks, get 1 on the house)

### Technologies required (besides typical Hackbright tech stack)
 ``


-Acuity API -https://developers.acuityscheduling.com/reference#quick-start
-Mockaroo API https://www.mockaroo.com/ (to generate fake customer data)


### Data


-user business name, password, and email
-brief summarization of business 
-number of transactions
-client names


### Roadmap

#### MVP

-Users login & create account
-user can manipulate numbers (max up to ten, minimum 0)
-add graphic of star when num gets to 10
-add & store client name
-add & store reward name



#### 2.0

-button clicking feature (changes colors)
-profile pictures?

#### 3.0

haven't thought this far



##########10/18 (Monday after end of 1st sprint)###############
### data
user:
    name, email, password, business name, business profile picture
client:
    name, email, reward point count
transactions:
    appointment type, transaction date, total cost
rewards:
    reward type
    reward cost

### MVP 
-user login & create account
-created directory for user
-(used hashed pw)
-create a client
-add transactions
-add reward types
-created tests for tables
-started point adjustment option for adding reward points


### 2.0
-finish point adjustment function
    -get points to database
    -create redeem
-change login to flask login
-amp security
    -strong password policy in place
    -use 2FA (two-factor authentication)
    -prevent sql injections
        -DON'T WRITE DYNAMIC QUERIES
        -prevent user supplied input which contains malicious SQL
        from affecting logic of executed query
    -use patchstack
-change url links to queries


### 3.0
-edge cases (?)
-ability to undo redeems...
-more security
    -check out cross site scripting
    -insecure deserialization
    -broken authentication
    -cross site request forgery attacks
    -sensitive data exposure
    -create way to have security check scans
