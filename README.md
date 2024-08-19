 # Byte 2 Eat
![image](https://github.com/user-attachments/assets/a7fc73bf-10f8-4ffa-af78-daa3be85604e)

## Contents
1. [Introduction](#introduction)
2. [The Team](#the-team)
3. [Planning](#planning)
4. [Design](#design)
5. [Repository, Project Board and Deployment](#project-base)
6. [Wireframes](#Wireframes)
7. [Features](#Features)
8. [Deployment](#Deployment)
9. [Technology](#Technology)
10. [Future Features](#Future-Features)
11. [Testing](#Testing)
12. [Validator Testing](#Validator-Testing)
13. [Credits](#Credits)
14. [Content Credit](#Content-Credit)
15. [Further Thoughts](#Further-Thoughts)

# Introduction

Welcome to Byte 2 Eat, a website designed to allow private users to review takeaways without having to make any public declaration. This offers a chance for highly personal reviews to be left of any standard without concerns for how it may look, legal consequences or controversy.

This website was created during Hackathon 3 of the "16-Week High-Performance Full Stack Skills Bootcamp" which ranged from 15/08/2024 (from 9am) to 19/08/2024 (up to 1.30pm) covering a weekend period. There were no planning or preparation conducted before the start day.

The goal of this Hackathon was to demonstrate the construction of a full-stack web development project using HTML, CSS, JavaScript, Python and Django in a team environment. 

<a id="the-team"></a>
## The Team

Together, we are Snack Overflow!

In alphabetical (by surname) order, here are the members of the team:-

The full-time developers: 

* Christina Hughes - (https://github.com/CHughes13)
* Barrie Millar - (https://github.com/CyberArchitect777)
* Samuel Parker - (https://github.com/SamuelParkerTech)

Additional development only (due to other course / personal committments):

* Leander Otis - (https://github.com/LO-CI24)
* Jamie Pudsey - (https://github.com/JPudsey-11)
* Aeryx Rose - (https://github.com/SubjugatorofCSS)

<a id="planning"></a>
## Planning Methodology 

Using Agile ideals, the project was designed with the principle of minimum viable product in mind. Therefore, it was decided that a very simple product would be constructed before any additional features were added. It was determined early on that the following features would be applicable to our project. 

Must-do:

- A login and registration system for our users to sign in to their private review areas
- A review screen where comments could be added, edited or deleted.
- Additional pages for form additions to achieve this as needed.
- A site that was effortless to use in order to allow users to quickly check in and out to submit their own ideas.

Should-do: 

- A wishlist of takeaways that people might like to try.

Won't do: 

- A public facing area showing all reviewed takeaways as this is not applicable to our project idea.
- Email / reset password login as the development of this feature requires an email server and is beyond the scope of this project.

A Google document was set up to share and discuss ideas (https://docs.google.com/document/d/1tP5J2UAh9JbXni9sQfab1tEwxLOkr21A9vTms7MyAY4). A Miro Board (https://miro.com/app/board/uXjVKpKknpw=/) was also established for the same reason. A screenshot of this board can be seen below. 

![image](https://github.com/user-attachments/assets/e97bbda1-9818-4b91-af25-67fdccdd7ed0)

## Repository, Project Board and Deployment

Our project details can be found in the following places. 

Project Board - (https://github.com/users/CyberArchitect777/projects/11)

GitHub Repository - (https://github.com/CyberArchitect777/hackathon3-byte-to-eat-project)

Heroku Live Deployment - (https://hackathon3-byte-to-eat-project-25fab4e92590.herokuapp.com)

## Design

### Colour scheme

Site: Purple: (#5058A8) \ White (#FFFFFF)

Logo: Purple (#5058A8) \ Fork grey (#BCBEC0) \ Circle grey (#F0F2F1)

### Wireframes

To design the project, we used Balsalmiq to create a number of wireframes. Our design concepts are shown below:-

Main Page \
![byte_2_eat_-_home_720](https://github.com/user-attachments/assets/95ec1821-43f2-4433-8273-8c70df7a7a80)

Register / Login \
![byte_2_eat_-_register_720](https://github.com/user-attachments/assets/19187be5-03c2-4fa9-af80-d575988784de)

Register Food / Review \
![byte_2_eat_-_user_food_form_720](https://github.com/user-attachments/assets/d0114c95-fd52-415e-b4d1-9a1ded14e572)


## Features

The main features of the site are a login management system, a user dashboard to view, create, edit and delete takeaway reviews and an about page. The screenshots below show the site as seen on desktop and mobile.

Once entering the website, the user is greeted with the following page on desktop and on mobile. Note the different ways that the logged in status is shown on desktop and mobile to provide clarity to users on both platforms.

![Desktop image of the index page when logged out](docs/images/desktop-index-loggedout.png)
![Mobile image of the index page when logged out](docs/images/mobile-index-loggedout.png) 

From here, you can register for the site as shown below.

![alt text](docs/images/desktop-register.png)
![alt text](docs/images/mobile-signup.png)

If you are already signed up, you can log in from this page instead.

![alt text](docs/images/desktop-login.png) 
![alt text](docs/images/mobile-login.png) 

Once logged in via the register page or log in page, the following index page is shown.

![alt text](docs/images/desktop-index-loggedin.png)
![alt text](docs/images/mobile-index-loggedin.png) 

When the user wants to sign out, they can do it here.

![alt text](docs/images/desktop-logout.png) 
![alt text](docs/images/mobile.logout.png)

## Deployment Via Heroku

First make sure the Debug is set to false \
In our project Debug was set via env.py so was active locally but disabled on Heroku automatically. \
![image](https://github.com/user-attachments/assets/e367bb35-3372-4c39-8672-5544cad9e9d8)

Connect your Github to your Heroku \
![image](https://github.com/user-attachments/assets/d8a7aed2-8c8e-4df5-92ce-286396be909f)

Make sure VARS are set correctly. \
![image](https://github.com/user-attachments/assets/cd552e8e-2fc9-4929-8f65-912860ec5c69)

In the deploy tab, scroll down and deploy MAIN Branch \
![image](https://github.com/user-attachments/assets/20234481-4a8a-44b7-9070-69b5bb1dd0c4)

## Technology

* Github - Version Control & Project Kanban / Issues
* Gitpod - Code Editor
* Django - Python Framework
* BootStrap - CSS Framework
* Google Fonts - Open Sans Font https://fonts.google.com
* Miro - Project Ideas Board & ERD Creation https://miro.com/
* Coolors.co - Colour pallette/tone helper https://coolors.co/
* Google Docs - Sharing and hosting files
* AllAuth
* Am I Responsive https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.de

### Django Requirements

* asgiref==3.8.1
* cloudinary==1.40.0
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.14
* django-allauth==0.57.2
* django-summernote==0.8.20.0
* gunicorn==20.1.0
* oauthlib==3.2.2
* psycopg==3.2.1
* PyJWT==2.9.0
* python3-openid==3.2.0
* requests-oauthlib==2.0.0
* sqlparse==0.5.1
* urllib3==1.26.19
* whitenoise==5.3.0

## Future Features

## Testing

Testing was done both manually and using Validators (see next section).

## Validator Testing

## HTML
Tested the HTML using W3 Validator using the URL checker function. https://validator.w3.org/
No issues - ![image](https://github.com/user-attachments/assets/a5bce627-5103-4a8d-b5bf-19001b6b2a57)

## CSS
CSS Validator testing used the jigsaw validator: https://jigsaw.w3.org/css-validator/ and posted no issues. 
![image](https://github.com/user-attachments/assets/4353bcf2-ec95-466d-a20e-ab277c556564)


## Javascript
Javascript was testing using JS Hint: https://jshint.com/

## Python PEP 8 CI Checker - https://pep8ci.herokuapp.com/

### User Profile Pages
urls.py \
![image](https://github.com/user-attachments/assets/5eef4c00-f015-44b8-b6da-4d51daba7ea4)
views.py \
![image](https://github.com/user-attachments/assets/ccf7eb2f-52dd-4f48-b7a6-d0ede8c32b4c)


## Credits

## Content Credit
Images from Unsplash.com & Freepik.com

## Further Thoughts

### 
### 
