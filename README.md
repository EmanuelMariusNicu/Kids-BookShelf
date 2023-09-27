# KIDS'BOOKSHELF

This a Django based(fictional) e-commerce application of 5 required portfolio projects.
Kids'BookShelf is an online store business based in the UK, specialising in used books for children. The store offers a variety of sensorial, fairytale/fiction, non-fiction and large-prints books. Currently the business offers orders only.
On their site, Chirpy Chooks also host a forum about all things poultry. Articles published by the business itself are posted on a regular basis, offering helpful advice about children education, interesting facts about different books or the latest recommendations on book challenges, child health etc.

## Table of Contents

- [UI/UX](#uiux)
    - [Agile](#agile)
    - [Site Goals](#site-goals)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [Database Design](#database-design)
    - [Custom Model](#custom-model)
    - [CRUD](#crud)

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [Payment processing](#payment-processing)
    - [Emails/Newsletter](#emailsnewsletter)
    - [SEO/Marketing](#seomarketing)

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    - [Media and Styling](#media-and-styling)
    - [Content/Data](#contentdata)
 
      ## UI/UX

The overall design of the site follows a cosmic style and a color palette that makes you think of the world of children and creativity. 
The website is very easy to navigate, very intuitive and very user-friendly. The site includes 4 categories of books at the moment, which makes it very practical and not crowded at all.


### Agile

This project was designed and built using the agile approach. Right from the initial planning through to final development. To help visualise the process I created a [GitHub project](https://github.com/users/EmanuelMariusNicu/projects/3/views/1) and utilised the provided Kanban board method to split project elements into user stories and manageable tasks.
To view all user stories refer to the project linked to above.
Each story also has been tagged with a label to signify how crucial a particular feature is to the overall workings and acceptability of the site.


### Site Goals

This site is the online shop of the fictional supplier of used children books Kids'BookShelf. This business is based in UK, and is aiming a consumer requirement for the early education of children from any social category, the books having ridiculous prices for all pockets.

On the site, customers can view different categories of books that the business owns and sells.Books can be ordered and paid for via an intuitive, straight forward process. This business can offer shipping.

"Kids'BookShelf" is very keen as a business to provide for past and future customers with useful advise and support about education. As well as general contact details, the shop's site also features a forum maintained by the business itself, where all visitors of the site can find helpful articles on various subjects related to education, children and books.

### 5 Planes of UX

#### Strategy

The website is addressed to parents, educators and children. The main objective is to reach the largest possible market of people and possibly their children with our used books but in a very good condition and for all pockets.
We rely a lot on children's early education,promoting reading among kids, building a community of readers, and providing educational resources and when is the best time to start? Exactly from the first months of the child's life.
In the future, we are thinking of offering everyone the opportunity to sell their used books so that as many children as possible can benefit.


#### Scope

Addresses what functions and features are within the scope of the project and not least a mobile-first approach for the business.
Basic and essential e-commerce functionality was key to this project. This means that most features included are a basic requirement. Features like user sign up and login, user profile creation, checkout functionality and secure online payment had to be implemented, as well as basic CRUD funtionality for authorised users. For detailed explanation of all existing features see [Existing Features](#existing-features).
To meet the site owners basic needs, each product can be easily updated or deleted via the front-end interface. New products can also be added via the front-end. Forum posts are handled the same way. All these features are only accessible to authorised users.

#### Structure

Defines how users can navigate the site and utilise all existing features.
The structure of the site is modelled on a basic e-commerce application with an additional forum page.
The structure allows users to browse products and make purchases as well as visit the forum to find information about children health, education and books. Authenticated users can store their personal information in a user profile for the purpose of faster order handling.
All CRUD functionality is placed intuitively with the relevant features of the site (individual products, forum posts). A super-user can avail of the same navigation options as any authenticated users. However, these include additional features limited to authorised users.

#### Skeleton

Puts features defined in structure into navigational elements.
To guarantee intuitive navigation of the site, both the navbar and the main content follow a standard layout pattern that should be familiar to most users.
The navbar provides links to the main features and functions of the site, varying based on whether a user is authenticated or not. On small to medium screen sizes a drop-down burger menu takes the place of the full navbar.
The shopping basket link in the navbar is being updated everytime a user adds an item (of a differnt type!) to the basket.
Products and categories, as well as forum posts are listed in a card-style display.
All forms are cleary labelled an inform the user of invalid fields. User feedback is represented throughout the whole site via alert pop-ups.
Buttons and links are appropriately named.
A footer with social media links completes the footer of the website.

#### Surface

Addresses visual design and how to convey desired emotions and achieve desired effects.
For more detail on the planning of the surface plane, see [Visual Design Choices](#visual-design-choices).

### Visual Design Choices

**Colour Scheme:**

The site utilises one accent colour (``primary-color: #e3dada``)r its warm, earthy quality. It also offer high enough colour in contrast with hero image and the navbar color.
 and a darker gradient of the same pallete (``primary-color-dark: #ceb4cf``) for the purpose of creating a visual contrast between header and hero image color pallete. The chosen colors are: 
 
![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/e896334b-4284-4c2c-b70e-386b5c19d68c)

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/6e0a9fa3-a048-4714-a06d-05544f228284)

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/b02947aa-4d28-478c-83d9-61e73ac29b16)

**Fonts:**

One extravagant font ("Orbitron") was chosen for the entire website.


**Images and Icons:**

All images of this site are purely related to the products offered in the store or relevant to the individual forum post. Apart from the hero image on the home page and about us page, the site refrains from using too many decorative elements.
Logo image is custom made especially for the website relevance.
Icons used for the purpose of navigation are standards symbols which should be familiar to most users.
For full despcription of all images and their sources see [Media and Styling](#media-and-styling).

## Features

### Existing Features

#### Global and Home

**Navigation**

- Responsive navbar with burger dropdown menu
- Shop logo as default home link
- Navigation options dependant of user authentication/authorisation

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/c4e44e5d-912e-4050-a850-2ed067481770)

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/337e1f51-9e57-4a23-968b-5fed546ddce2)



**Footer**

- Footer element with social media links
- Contains link to privacy policy
- Newsletter sign up option

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/8414ba4b-425f-49c7-9f9e-66a4b980d0b0)

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/be11cc3e-309f-4c3d-a5c8-4500a0997fc2)


**Home page**

- Home page with banner image and introduction
- Shop Now button ("Go To Library")

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/3bc24399-623d-4b7e-b318-a554d3e5c286)


**About page**

- General info about store operations
- Contact info incl. address, phone number and email
- Shop opening hours

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/9941cda9-2a4d-49b6-ae7f-fc0e97e3b03e)
![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/d6d7fa6a-67a8-4d8a-8eea-64ec5f395c8f)


**Privacy policy**

- Standard GDPR compliant privacy policy page 
- Linked to in footer

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/8153b550-4539-45d8-a20a-81e995c07b10)


Image does not contain entire policy document. Visit site to view full policy.

**404 Error page**
- Informs user of invalid URL
- Back button redirects user back to home page



**User feedback**

- Alert messages inform user of:

    - Actions about to be performed
    - Actions successfully completed
    - Actions failed to complete


#### Authentication

**Sign Up**

- Allows new users to create account
- Sign up process includes confirmation email with confirmation link

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/9bba9236-9cf6-42b8-997e-957464daabbb)

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/2d8c9f34-13ef-4d8c-863f-6db3adc097e6)


**Login**

- Allows existing users to log into their account
- Includes Remember me checkbox and forgot Password option

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/f2953f9a-bfb8-439c-906c-d779ebf0d184)


**Logout**

- Allows authenticated users to securely log out of their account

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/b9290cdc-a111-43a2-968a-56b432a62ea3)

#### Products

**All Products page**

- Lists all categories of products
- Links to forum and contact info

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/811d0212-9bd3-4add-b2af-c62518bc53c8)


**Products page (of same category)**

- Lists all products of the same category
- Quick link to All Products page

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/e3f3be11-308b-4c54-8e14-891c1d248265)


**Product details page**

- Product image, description and price
- Quick link to respective category
- Quantity input
- Continue Shopping button ("Browse more")
- Add to basket button
- Edit and delete option for authorised users for each product

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/49438ac3-e9c6-40ac-abd2-4a725a12a7c7)

**Add Product page**

- Authorised admin users only!
- Complete product form with image upload option
- Cancel button
- Add product button to add product to database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/58deb5bc-8bff-4861-ac13-f1ca3c7f3ca3)


**Edit Product page**

- Authorised admin users only!
- Complete product form with image upload option
- Form is pre-populated with existing product's details
- Cancel button
- Update product button to update existing product in database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/b6325053-1f62-493c-9fba-03d92d70c815)


**Delete Product option**

- Authorised admin users only!
- Option on product details page
- Request for user confirmation before deleting product
- Cancel button
- Delete button to delete existing product from database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/f4f99558-9968-4129-8b08-93b37c003668)

#### Forum

**Forum page**

- Lists all forum entries in tile format
- Tiles show title, excerpt, image, create-date and category
- Category button filters all entries by respective category

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/67919069-c663-4e66-b52e-195e23c2531d)


**Filter option**

- Category tag in each entry tile acts as filter button
- When clicked, Clear Filter button is displayed above fitler result

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/926f1294-e68c-4025-8815-1c5ac9d52e8a)


**Entry detail**

- Shows complete content of forum post
- Edit and delete option for authorised users for each entry

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/dc4182b3-96b6-438e-a67e-828a1cfdd5b6)


**Add Entry**

- Authorised admin users only!
- Complete forum entry form with image upload option
- Cancel button
- Add entry button to add entry to database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/ad253b6b-7657-494f-8e9f-645947b74666)


**Edit Entry page**

- Authorised admin users only!
- Complete forum entry form with image upload option
- Form is pre-populated with existing entry's details
- Cancel button
- Update entry button to update existing entry in database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/83b90a55-31a1-4d51-9499-1d377b165e8d)

**Delete Entry option**

- Authorised admin users only!
- Option on forum entry page
- Request for user confirmation before deleting entry
- Cancel button
- Delete button to delete existing entry from database

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/01750e3a-57e2-4d4d-83cc-481e71f89f3a)


**Response form and display**

- Post response: authenticated users only!
- Response form under entry content
- All submitted responses need admin approval (user alert after form submit about wait for approval)
- Approved responses listed below response form, including author, post-date and content

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/394ce3d4-f182-4ab1-ac25-0402467be62b)

#### Shopping Basket

**Basket items in nav**

- Live update of basket status in navbar
- Counter in nav element displays only the number of different products, not the total of all products.
![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/56e19e8c-1162-4e83-a8dd-08287cab41ac)


**Shopping Basket**

- Tabular view of currently selected products and their quantity
- Quantity adjustment option
- Product removal option
- Display of subtotal, delivery cost (currently always 0) and grand total
- Continue shopping button
- Proceed to checkout option

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/a7d13b2e-bf24-4a87-8540-64203ad23780)



#### Checkout

**Checkout page**

- Checkout form, including sections for personal info, contact details and card details
- Option to save details to profile for authenticated users
- Current order summery
- Edit Basket button
- Pay now button

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/156efd17-dfcc-4151-a35a-ecc0e32470bb)
![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/f456a47f-7644-4ba4-92a3-e8808759651c)


**Checkout Success page**

- Confirms successfull order and informs user that email was sent to the address specified
- Displays order details, contact and billing info
- Continue Shopping button ("Back to products")

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/d086bf3b-e920-48a0-9c26-003ec81aa31e)


#### Profile

**User Profile page**

- Contact address form (pre-populated if user has previously saved his info)
- Update Info button
- Listing of past orders in order history

![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/4926662b-3334-42fc-afe7-01e92743fef9)


### Possible Future Features

**Extended product range**

The shop has the potential to extend its product range to different products or services about education.
For the purpose of this project however, it was unnecessary to implement such a broad product database.

**Search option**

A search bar could be included in the header or be accessible throughout all products related pages of the site. Currently the product selection is so small that a search bar was deemed unnecessary but would make sense to implement along with an extended product range.


**Forum response approval via front-end**

Currently the approval of user responses to forum entries by admin users is happening solely via the Django admin dashboard. 


### Custom Model

As required by the assessment criteria for this project, three custom models were added which were not covered by the Code Institute tutorial this project is based on. These models are ``EntryType``, ``Entry`` and ``Response``, all of the forum app (forum/models.py).
I have also customised models covered the Boutique Ado walkthrough project (see [References](#referencesdocumentationtutorials)) by adding or removing fields.

### CRUD

Full CRUD functionality via the front-end UI is implemented for admin users in the Forum app and the Products app. 

**Create:**

*Forum:* Create new forum entry. 
*Products:* Add new product. 

**Read:**

*Forum:* Read all existing forum entries. 
*Products:* View all existing products. 

**Update:**

*Forum:* Edit existing forum entries. 
*Products:* Edit existing products. 

**Delete:**

*Forum:* Delete existing forum entries. 
*Products:* Delete existing products. 

For a detailed description of all CRUD features see [Features](#features)

## Technologies Used

### Work Environments and Hosting
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [AWS - Amazon Web servises (S3)](https://aws.amazon.com/) (Hosting static and media files)

### Python Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (integrates python libraries with AWS services)
- [django-storages](https://django-storages.readthedocs.io/en/latest/) (collection of custom storage backends for Django)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Python linter used for python code validation)

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)
- [Bootstrap5 template pack for django-crispy-forms](https://pypi.org/project/crispy-bootstrap5/)
- [django-summernote](https://github.com/summernote/django-summernote) (WYSIWYG HTML editor)

### Payment processing

- [Stripe](https://stripe.com/) (Online payment platform)

### Emails/Newsletter

- [Gmail](https://mail.google.com/) (Real email sending)
- [Mailchimp](https://mailchimp.com/) (Automated newsletter subscription service)


### SEO/Marketing

- [XML Sitemaps](https://www.xml-sitemaps.com/) (Sitemap generator)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

## Testing
For extensive instructions on how to manually test this site and it's user stories, please refer to these [Manual Testing Instructions](TESTING.md)
### Test Guide

### Validator Testing

####  HTML [W3C Markup Validation](https://validator.w3.org/)  is a service provided by the W3C that allows you to validate your HTML code against the official specifications. It checks for syntax errors, improper tag usage, and other issues that may affect the structure and semantics of your web pages. Validating your HTML code with W3C Markup Validation helps ensure that your pages are well-formed and adhere to web standards.
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/base.png)</details>| :white_check_mark:
|index| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/index.png)</details>| :white_check_mark:
|add_| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/add_trip.png)</details>| :white_check_mark:
|edit_| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/edit_trip.png)</details>| :white_check_mark:
|browse| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/browse.png)</details>| :white_check_mark:
|post_detail| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/post_detail.png)</details>| :white_check_mark:
|search_card| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/search_card)</details>| :white_check_mark:
|search_results| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/search_results.png)</details>| :white_check_mark:



#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No errors found.

#### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

**Desktop results**
![image](https://github.com/EmanuelMariusNicu/kids-bookShelf/assets/108750655/fd206bfd-39b4-47c9-b089-9b6200eceea3)



**Mobile results**

### Browser Testing

**Layout:** 

Testing layout and appearance of site for consistency across browsers.

**Functionality:** 

Testing complete functionality of the site as specified in the [Manual Testing Instructions](TESTING.md) accross browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |

### Fixed bugs




### Unfixed bugs

- Lighthouse Chrome DevTools performance needs to be adjusted.

## Deployment

This project was deployed using [Heroku](https://heroku.com/), [ElephantSQL](https://www.elephantsql.com/) and [AWS](https://aws.amazon.com/). For a full list of libraries refer to [Technologies Used](#technologies-used).

#### Installing libraries

The following steps outline all libraries needed for successful deployment on Heroku. All necessary requirements and settings updates will not be discussed in this section as they are assumed as logical follow-up steps to installments. For full explanation on how to install these libraries, refer to the links provided in [Technologies Used](#technologies-used).

- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Create PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Data center
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but be more inventive about the key string!)

#### Update Settings

- Add the following code at the top of ``settings.py`` to connect Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove insecure secret key provide by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to new database, replace provided **DATABASE** variable with 
    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made and load in fixtures

#### Preparing for Heroku

- Create Procfile (tells Heroku to create web dyno which will run gunicorn and serve Django app)

- Temporarily disable collectstatic (prevent Heroku from collecting static files when deploying)

- Allow Heroku as host:

    In ``settings.py`` add
        ````
        ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
        ````
#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add three new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")


#### Deyploying with Heroku

- In Heroku dashboard, go to **Deploy** tab
- Select "GitHub" as Deployment method and choose correct repo
- Enable Automatic Deploys
- Click "Deploy Branch" button

#### Hosting images and static file with AWS

- Create AWS account and go to AWS Management Console in the My Account dropdown
- Find and access S3 as a service and create a new bucket:

    Under Object Ownership, check "ACLs enabled"

    Uncheck "Block all public access" and acknowledge (required for public access to static files)

- Configur bucket settings:

    Under **Properties**, enable Static Website Hosting

    Under **Permissions**, copy the following code into CORS section:

    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    This is required to set up the access between the Heroku app and the S3 bucket.

    Under **Bucket policy**, go to Policy generator.

    Bucket Type = S3 Bucket Policy

    Principal = * (allows all principles)

    Actions = GetObject

    Paste in ARN from bucket settings tab.

    Click Add Statement, then Generate Policy.

    Copy policy in paste into bucket policy editor. Also add ``/*`` onto the end of the resource key.

    Click Save.

    Under **Access control list (ACL)**, check "List" checkbox for "Everyone (public access)"

- Create user to access bucket with IAM (Identity and Access Management)

    In IAM, got to User Groups (sidebar left).

    There create a group for a user, create an access policy giving the group access to the S3 bucket and assign the user to the group so it can use the policy to access all files. 

- Connect Django to S3

    Install packages "boto3" and "django-storages" and add ``'storages'`` to INSTALLED_APPS  in settings.py

    Configure settings.py accordingly, including necessary AWS variables.

    Add new config vars in Heroku app settings, including user credentials from AWS.

    Create ``custom_storages.py`` file.

- Upload static files and media files to S3

  #### Add Stripe keys to Heroku

From Stripe account, under Developers > API keys copy Public Key and Secret Key and set as config vars in Heroku app settings.

Create new Webhook endpoint for deployed site and enable all events. Then add Signing Secret to Heroku app config vars.


## Development

The following options are available to work with this code or run in a local environment.

### Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on repository to download 
- Click the **Fork** buttonin the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed

### Clone

Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repostitory (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change current directory to target location for cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

### Download as ZIP

- Log into GitHub and click on repository to download 
- Select **Code** and click "Download Zip" file
- Once download is completed, extract ZIP file and use in your local environment

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/ie/) tutorial ["Boutique Ado"](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546).

**Basket tools**:

[Django Docs on creating custom template tags](https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/)

**Basket items count display in navbar**:

The syntax for displaying the amount of items currently in the shopping basket was taken from this [FeelFreeToCode tutorial](https://www.youtube.com/watch?v=3xQRJqxdgK4&ab_channel=FeelFreeToCode)

**User alerts (toasts/messages)**:

The live feedback messages to alert user actions were implemented using the [Django message framework](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) and the respective [message levels](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/).

The alert pop-up frames were rendered using [Bootstrap 5 toasts](https://getbootstrap.com/docs/5.0/components/toasts/).

### Media and Styling
**Images:**
All images are my own but hero image from google.
**Fonts:**
All fonts were taken from [Google Fonts](https://fonts.google.com/).

**Icons:**

All icons were taken from [Iconify](https://icon-sets.iconify.design/). Included in this is the animated loading spinner icon of the checkout page.

### Content/Data

#### Products

All fixtures for the products app were manually compiled with data gathered from various online resources.
