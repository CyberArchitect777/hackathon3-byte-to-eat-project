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

## Repository, Project Board and Deployment

Our project details can be found in the following places. 

Project Board - (https://github.com/users/CyberArchitect777/projects/11)
GitHub Repository - (https://github.com/CyberArchitect777/hackathon3-byte-to-eat-project)
Heroku Live Deployment - (https://hackathon3-byte-to-eat-project-25fab4e92590.herokuapp.com)

Miro Board
https://miro.com/app/board/uXjVKpKknpw=/

## Design

Purple: #5058A8 \
Fork grey: #BCBEC0 \
Circle grey: #F0F2F1 

## Wireframes 
Website Wireframes were created in Balsalmiq.
Main Page \
![byte_2_eat_-_home_720](https://github.com/user-attachments/assets/95ec1821-43f2-4433-8273-8c70df7a7a80)

Register / Login \
![byte_2_eat_-_register_720](https://github.com/user-attachments/assets/19187be5-03c2-4fa9-af80-d575988784de)

Register Food / Review \
![byte_2_eat_-_user_food_form_720](https://github.com/user-attachments/assets/d0114c95-fd52-415e-b4d1-9a1ded14e572)


## Features

The main features are a login page, a user dashboard with the ability to post new reviews of takeaways and view those takeaways. 

### Main Page (Not logged in)
![image](https://github.com/user-attachments/assets/4efc420f-3485-4d9a-b725-bdc8ec6deb63)

### Sign in Page
![image](https://github.com/user-attachments/assets/1e7c2cb1-1c4c-4fb9-9720-3b56daefff14)

### Main Page (logged in)
![image](https://github.com/user-attachments/assets/add01b10-2872-4b2e-94c4-72f8f26e8fa7)
We are likely to add more functionality to this page, or have it redirect to the user dashboard. 

### 'My Reviews' / User Dashboard
![image](https://github.com/user-attachments/assets/1abb16c8-ee12-4a8a-ae63-a1eda4a8e653)

### Add Review Page
![image](https://github.com/user-attachments/assets/7e90d289-449a-4e41-8020-24a507842543)

### Edit/Delete a Review Page
![image](https://github.com/user-attachments/assets/3ace9008-d151-400b-98ba-c4eeee62b422)

### About Page
![image](https://github.com/user-attachments/assets/389e8acf-1487-41e4-a514-69b01fb7891c)

### Logout Page
![image](https://github.com/user-attachments/assets/9c455384-7546-400a-8eee-a0c04c9b61fa)

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
* Google Fonts - Oswald Font https://fonts.google.com/specimen/Oswald
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


## Credits

## Content Credit
Images from Unsplash.com & Freepik.com

## Further Thoughts

### 
### 
