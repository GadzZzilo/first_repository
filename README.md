# Service site

---
## Contents
1. [Description](#description)
2. [Features](#features)
3. [How the site looks like?](#how-the-site-looks-like)
4. [How do I launch a website?](#how-do-i-launch-a-website)
---
## Description
<p> This multifunctional website is designed to provide services to students 
</p>

---
## Features
- A form is used for feedback on the passage of the captcha
- User registration and authorization is used, followed by entry into the database
- A confirmation email will be sent to complete the registration
- It is possible to log in via social networks
- Celery is used for the task queue (when registering, the user does not wait for the system to send an email)
- The PostgreSQL database is used
- Database queries were tracked and data caching was introduced using the debug_toolbar
---
## How the site looks like?
<p><b>Main page</b></p>
<p align="center"><img src="misc\images\main_page.png" alt="main_page" style="width: 80%; min-width: 100px;"></p>

<p><b>Captcha feedback form</b></p>
<p align="center"><img src="misc\images\feedback.png" alt="feedback" style="width: 80%; min-width: 100px;"></p>

<p><b>Registration/authorization form</b></p>
<p align="center"><img src="misc\images\auth_form.png" alt="registration/authorization form" style="width: 80%; min-width: 100px;"></p>

---
## How do I launch a website?
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver