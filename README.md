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

- [SEO and Marketing](#seo-and-marketing)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)

- [Database Design](#database-design)
    - [Database Model](#database-model)
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

## SEO and Marketing

For an extensive overview of the marketing research for this project, please refer to this [SEO and Marketing documentation](MARKETING.md)


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




