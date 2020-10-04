# Welcome to RuleOf72



# What is RuleOf72?
RuleOf72 is a finance education website for anyone to create a topic that they are knowledgeable about. Users are also able to have discussions on any topic that they are enthusiatic about.
Please visit the live site [here](https://ruleof72zx.herokuapp.com/) 

### For test users, please use the following account:
- User: **customerb**
- Password: **12345678!**
### or
- User: **LZX**
- Password: **seehorse1993!**
### Image
##### - This website uses Cloudinary for image uploading.
### Video
##### - To Embed a video for a topic, please go to youtube, select a video to embed, click on "Share" and copy the embeded link. This is due to the constrains of cloudinary as they have a set 100mb storage capability. 
##### - For testing, please paste <https://www.youtube.com/embed/v6j8ewrcxd8> this link into the video field.
##### - Lesson "stocks 202" has 3 sub topics.


# UI/UX


## Strategy
### Owner stories:

- As the owner, I want to build an ecosystem so that users can learn about any financial topic there is.
- As the owner, I want to build up a reputation to be the website with the highest quantity and quality educational content pertaining finance.
- As the owner, I want people to embrace finance and take control of their own finances as I believe the best investment anyone can make is their own education.

### User-Teacher:

- As the teacher of a financial topic, I want my students to have the best experience and useablity when it comes to UIUX as this will encourage my students to stay on the site longer.
- As the teacher, I want to be able to present my knowledge in a structured manner so that students will no be overwhelmed by information.
- As the teacher, I want to teach on a website that has alot of visitors as that will boost my earnings.

### User-Student:

- As a student, I want to study on a website that is easy to use so that I can retain my attention span for a longer period of time.
- As a student, I want to be on a website that provides a wide array of lessons to choose from.
- As a student, I want to be able to engage in meaningful discussions after a topic so that I can retain the most information and also helps to cement my understanding on the topic.


## Scope

### Current Features

#### Accounts:
- Register
- Login
- Logout
#### Lessons:
- Create Lessons
- Update Lessons
- Delete Lessons
- View all created Lessons
- View all purchased Lessons
- Search for a Lesson by title
- Create sub topics
- Update sub topics
- Delete sub topics
#### Forum:
- Create a discussion
- Update a discussion
- Delete a discussion
- Search for a discussion by title
- Create a comment
- Update a comment
- Delete a comment

### Features to be implemented

- Login/Register with social media sites
- Filter search results and sort by price or date listed
- Wishlist for users to add in sortlisted listings
- Annotations of video lectures 
- Sending confirmation emails
- Voting system for Lessons and Forum comments

## Skeleton

Wireframes can be found [here](https://github.com/liuzhenxin2/RuleOf72/tree/master/wireframes)

## Surface

As this is a finance related website, I chose darker colors to represent professionalism and I chose a lighter shade of blue to give users a slightly casual and less pressured feeling. There is no fancy font as I want to present a readable website.
The logo used is 72/? because the rule of 72 is a known equation that helps to calculate the number of years required to double your investment. So for example, if your returns is 6%, 72/6 would be 12. Which means that it would take you 12 years to double your investment.

# Technologies used

- HTML
- CSS
- Javascript
- [JQuery](https://jquery.com/) to simplify DOM manipulation
- [Bootstrap version 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) for flex boxes, color schemes and navbar
- [GitHub](https://github.com/) for version control
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) for template displaying
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) for more aesthetically pleasing forms
- [Stripe](https://stripe.com/en-sg) for payment handling
- [Heroku](https://dashboard.heroku.com/apps) for website hosting
- [Cloudinary](https://cloudinary.com/) for image uploading
- [Django](https://www.djangoproject.com/) for the key essential features such as routing, validation of forms and implementing key functions of the webpage.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) to provide basic security and privacy features and to enable an account login system.
- [Python-dotenv](https://pypi.org/project/python-dotenv/) to prevents senstive information from being uploaded to github
- [SQLite3](https://www.sqlite.org/index.html) for test development
- [dj_database_url](https://pypi.org/project/dj-database-url/) for heroku development and deployment


# Database design

ER diagram can be found [here](https://github.com/liuzhenxin2/RuleOf72/blob/master/ERD72.png)
Logic Schema can be found [here](https://github.com/liuzhenxin2/RuleOf72/blob/master/LogicS72.png)

# Bugs

### Stripe webhooks not working.

# Testing

A detailed testing file can be found [here](https://github.com/liuzhenxin2/RuleOf72/blob/master/ruleof72%20test.pdf)

# Deployment

#### This website is deployed on Heroku. The URL for the deployed website is https://ruleof72zx.herokuapp.com/

#### To deploy on Heroku:

1. Download or Clone the master branch from github
2. To list all the requirements in requirements.txt, run the following command in terminal:
```pip3 freeze --local > requirements.txt```
3. Set Debug to False in settings.py of main project app.
4. Procfile need to be created to run gunicorn upon deployment
5. Git push to Heroku Master after all the documents are properly set up
6. All public keys and private keys for the following need to be added to in Heroku Config Vars settings:
- Cloudinary API key
- Cloudinary API Secret
- Cloudinary Cloud Name
- Database URL
- Stripe Endpoint Secret
- Stripe Publishable Key
- Stripe Secret Key
- Secret Key
# Credits

- Google and Unsplash for images
- [LogoMakr](https://logomakr.com/) for logo
- [Favicon.io](https://favicon.io/) for favicon conversion

