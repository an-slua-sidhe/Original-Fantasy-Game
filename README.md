# **ORIGINAL FANTASY GAME&trade;**

<!-- ![Original Fantasy Game Banner Logo](static/images/misc/banner_1.png "Original Fantasy Game Banner Logo") -->

## **Introduction**

This is the repository for the **ORIGINAL FANTASY GAME&trade;** website.

The deployed site can be visited by clicking [**here**](https://pq-original-fantasy-game.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/an-slua-sidhe/milestone-3).

My name is **Paul Quinn** and I designed and developed this site in its entirety as part of my [**Fullstack Web Development Diploma**](https://codeinstitut#e.net/courses) with the **Code Institute**, Ireland. For my Milestone 3 project, I designed a browser-based adventure game called the 'Original Fantasy Game™'. The inspiration for this came from the [**Fighting Fantasy**](https://www.fightingfantasy.com/) series of books by Games Workshop in the 1980s (among others). I imagined each page choice in the books as equivalent to a app route in HTML, with text on screen telling the player the story and offering them game choices. I also imagined a character creation section, where the player's statistics (effected by their race and class choices) would allow them to interact and fight with non-player characters they encountered.

This project contains the main menu and CRUD functionality of the game, along with a carousel of the game location art. The actual adventure and several other features will be added at a later date. The site is deployed dynamically on Heroku with template logic via Python3, Flask and JinJa. It has a connected MongoDB database allowing character, class and race creation CRUD functionality.

There is a full overview of the design/development process below, along with an extensive outline of the testing process, future features, user stories, responsivity and deployment.

## **Table of Contents**

1. [User Experience](#user-experience)
    * [User Stories](#user-stories)
        * [The Gamer](#the-gamer)
        * [The Gamebook Fan](#the-gamebook-fan)
        * [The Developer](#the-developer)
        * [The Critic](#the-critic)
    * [Design Documents](#design-documents)
        * [Basic Wireframes](#basic-wireframes)
        * [Full Asset Mockups](#full-asset-mockups)
        * [Database Schema](#database-schema)
    * [Design Choices](#design-choices)
        * [Images](#images)
        * [Colours](#colours)
        * [Fonts](#fonts)
        * [Icons](#icons)
        * [UI](#ui)
    * [Design Changes](#design-changes)
        * [General Changes](#general-changes)
        * [Mobile Changes](#mobile-changes)
        * [Tablet Changes](#tablet-changes)
        * [Desktop Changes](#desktop-changes)

2. [Features](#features)
    * [Existing Features](#existing-features)
        * [Base HTML](#base-html)
        * [Main Page](#main-page)
        * [List of Classes/Races](#list-of-classes/races)
        * [Create/Edit Classes/Races](#create/edit-classes/races)
        * [List of Characters](#list-of-characters)
        * [New Character/Edit Character](#new_character/edit_character)
        * [New Game Page](#new-game-page)
        * [Start Game Page](#start-game-page)
        * [Game Location 1](#game-location-1)
        * [Game Art Page](#game-art-page)
        * [Footer](#footer)
    * [Future Features](#future-features)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)
    * [Testing Devices](#testing-devices)
        * [Mobile Devices](#mobile-devices)
        * [Laptop Devices](#laptop-devices)
        * [Desktop Devices](#desktop-devices)
    * [Developer Tools](#developer-tools)
        * [Chrome](#chrome)
        * [Firefox](#firefox)
        * [Opera](#opera)
        * [Edge](#edge)
        * [Internet Explorer](#internet-explorer)
        * [Safari](#safari)
        * [Mobile Resolutions](#mobile-resolutions)
        * [Tablet Resolutions](#tablet-resolutions)
        * [Desktop Resolutions](#desktop-resolutions)
    * [Media Queries](#media-queries)
    * [Dashboard](#dashboard) ??
    * [Validation](#validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JavaScript](#javascript)
        * [Python](#python)
        * [ARIA](#aria)
    * [User Scenarios](#user-scenarios)
        * [Gamer looking for a new interactive experience](#gamer-looking-for-a-new-interactive-experience)
        * [Fantasy gamebook Fan seeking nostalgic entertainment](#fantasy-gamebook-fan-seeking-nostalgic-entertainment)
        * [Game reviewer looking for a product to review](#game-reviewer-looking-for-a-product-to-review)
    * [Outstanding Bugs](#outstanding-bugs)

5. [Deployment](#deployment)
    * [Local](#local)
    * [Remote](#remote)
    * [Heroku](#heroku)

6. [Credits](#credits)
    * [Code Used](#code-used)
    * [Images Used](#images-used)
    * [Acknowledgements](#acknowledgements)

___

## **User Experience**

**Original Fantasy Game™** was conceived as an atmospheric fantasy adventure, with corresponding art and design. It was designed with both mobile and desktop in mind, as opposed to mobile first, as it's appeal to users would be split between the two. The fantastic artwork would clearly suit larger resolutions better. I sought to create a smooth and atmospheric UX, where the fantasy atmosphere could be felt in the colours scheme, art and navigation. To achieve this, I chose a template from [**Start Bootstrap**](https://startbootstrap.com/) which I felt could embody this atmosphere, called [**Grayscale**](https://startbootstrap.com/themes/grayscale/). I then amended this template in several places to suit the site.

### **User Stories**

There are different types of user which may visit the site, each with different goals and motivations. I have listed their stories in three categories; The Gamer, The Gamebook Fan, The Developer, The Critic.

#### The Gamer

* As a Gamer, I can find the site online while looking for a new interactive experience.
* As a Gamer, I can start a new game from the [Main Page](#main-page).
* As a Gamer, I can create my character by selecting New Character form the Navbar, or by pressing the New Game button and choosing Create Character.
* As a Gamer, I can choose an already created character in the [List of Characters](#list-of-characters) screen.
* As a Gamer, I can begin a new game with either an previous or a newly created character in the [Start Game Page](#start-game-page).

#### The Gamebook Fan

* As a Gamebook Fan, I create a [Character](#new_character/edit_character) with various statistics in a similar way to the original gamebooks.
* As a Gamebook Fan, I can find the fantasy location art carousel on the [Game Art Page](#game-art-page) and browse a selection of fantasy landscapes.

#### The Developer

* As a Developer, I can find the site while looking for people to collaborate with on a new game project.
* As a Developer, I can read the future features listed on the [Game Location 1](#game-location-1) screen.

#### The Critic

* As a Games Reviewer, I can access the game from the Heroku link and try out the current UI, fantasy aesthetic and functional CRUD screens.
* As a Games Reviewer, I can return later to sample the full adventure and review the game for my publication.


### **Design Documents**

I used Adobe XD to design and create **Wireframes** and **Mock-ups** for this site. I decided to create a single page site and to follow the principal of **Mobile First**. I followed the usual method of keeping the basic wireframes extremely simple stylistically, mostly focusing on the form, location and interaction between the various elements of the site on each page. I then used the theme of culinary excellence to decide the colour palette and artistic direction of the site. The wireframes and mock-ups can be found as PDFs in this repository (see below for links).

#### Basic Wireframes

The basic **Wireframes** are available in three PNGs; one for [**Mobile**](assets/wireframes/mobile-wireframe.png), one for [**Tablet**](assets/wireframes/tablet-wireframe.png) and one for [**Desktop**](assets/wireframes/desktop-wireframe.png). Any colour used is for contrast only. Simple text headings were added to each element to denote its purpose. These overall [**Design Choices**](#design-choices) can be traced to the final deployed [**Website**](https://an-slua-sidhe.github.io/milestone-2), with some changes (see [**Design Changes**](#design-changes)).

#### Full Asset Mockups

PNGs of the full asset **Mockups** can also be found in this repository. The **Mobile** mockup can be found [here](assets/mockups/mobile-mockup.png), the **Tablet** version is [here](assets/mockups/tablet-mockup.png) and the **Desktop** version is [here](assets/mockups/desktop-mockup.png).

#### Database Schema

The database in this project was non-relational, and therefore the actual schema is very simlple. It can be found [here](static/design_docs/database_schema.pdf) and it shows how the Race and Class creation routes feed into the character creation section.

### **Design Choices**

Bootstrap Template:
    Source Site: https://startbootstrap.com/themes/grayscale/
    Live Site: https://startbootstrap.github.io/startbootstrap-grayscale/
The site was intended to have an aura of classy competence, a simplicity of design that didn't attempt to overwhelm the users senses. I have tried to use clear, simple and high quality images and textures when designing the site. I didn't want a site that contained too much clutter and text, but one that got across its message confidently, clearly and cleanly. Therefore, I decided to create a single-page site with a focused aesthetic. Mobile, tablet and desktop versions of the site are only very slightly different, basically involving **Bootstrap** responsive break-point changes (see the [**Restaurants Section**](#restaurants-section) below).

#### Images

I wanted a selection of high quality images for the site, which were uncluttered and depicted cooking scenes in an elegant way. Where these images would be used was already decided in the design **Wireframes** (see [above](#basic-wireframes)). I found the assets I sought on [**Pixabay**](https://pixabay.com/). The main **Jumbotron Background Image** was very important for the site. I chose one that was tasteful, with a palette of muted, yet organic colours, and it can be found [here](assets/images/jumbotron.jpg). I selected an ephemeral image of fine dining for the **README Banner Logo** which can be found [here](assets/images/banner.png). The **Booking Section Background** (click [here](assets/images/bookings-background.jpg)) introduces a dash of brighter colour to the overall palette. This is expanded with the **About Us Background**, which you can see [here](assets/images/about-us-background.jpg). Finally, each culinary venue has an image that was sourced from the restaurant's own web page; click on the restaurant name below to see the location of these files in this repository:

* [Ichigo Ichie](assets/images/ichigo-ichie-cork.jpg)
* [The Cliff House](assets/images/cliff-house-waterford.jpg)
* [L'Ecrivain](assets/images/lecrivain-dublin.jpg)
* [The Ox](assets/images/ox-belfast.jpg)
* [Kai Restaurant](assets/images/kai-restaurant-galway.jpg)
* [The Chart House](assets/images/chart-house-dingle.jpg)

To see where these images appear on their respective web pages, see the [**Credits**](#credits) section below. All images were resized with the  [**Jpeg Optimizer**](http://jpeg-optimizer.com/) so that the site would load more quickly. The original size of the images was massive and led to stuttering when the page was scrolled.

#### Colours

I used [**Canva**](https://www.canva.com) to create a palette from the **Jumbotron Background Image**. This understated and earthy palette suited the culinary nature of the site. I contrasted each section's use of colour, with large high-res background images for the **Jumbotron**, **Booking** and **About Us** sections, and a simple chocolate coloured backdrop to the sections in between. One more main colour from the palette was used for the backgrounds of separate elements within the **Services** and **Restaurants** sections, a moderate blue which could be contrasted with the chocolate background of the overall sections. Variations on these colours where then used for the **anchor links** throughout the site, with changes on **hover**, **scroll** and other actions. The main text colour was a white or off-white, so as to be legible on the dark backgrounds. Variations on the main text colour were used in the Navbar and in various elements throughout for legibility and contrast. An opaque background colour was used in various elements to make text visible.

The colours used for the site are:

* Main Text Colour - #FFF
* Navbar Text Colour - #E0DFDF
* Text Colour Variation - #F1E5E5
* Main Background Colour - #594C45
* Opaque Background Colour - rgba(0, 0, 0, 0.6)
* Contrasting Background Colour - #426A8C
* Link Colour - #F7D29C
* Link Hover Colour - #C29C64
* Google Maps Colour - #000
* Form Button Colour - #ECEAEA

#### Fonts

The fonts I used were selected from [**Google Font's**](https://fonts.google.com/) array of options.  [_**Gafata**_](https://fonts.google.com/specimen/Gafata) was chosen as the main font of the site, as it has a simple yet classy look, and is clearly legible. [_**Cinzel**_](https://fonts.google.com/specimen/Cinzel) was chosen as the main heading font, and for the **Logo**. This font has an elegant look to it which suits the site's overall theme. The back up font is _**Sans-serif**_.

#### Icons

A **Navicon** was created for the site using the font _**Cinzel**_ and [**Gimp**](https://www.gimp.org/) and can be viewed [here](assets/images/favicon.png) (PQ - To be completed). Social media link icons were supplied by [Font Awesome](https://fontawesome.com/).

#### UI

???

### **Design Changes**

#### General Changes

There were very little general changes from the original design. Some font colours were changed when it became apparent that they didn't work as expected; an example of this is in the **CTA**, where the '20% OFF' text was meant to be red, but was changed to a lighter brown colour as the red was too dark. One major change was the introduction of **Flipcards** into the **Restaurants Section** (see [**below**](#flipcards)). This allowed me to have the restaurant image on the front of the card and the information on the back, saving space and making for a better looking UI. In turn, this impacted on the original **Mobile** and **Tablet** design for this section, which tried to force the images and information into one card. The original design, and its **Desktop** variant, can still be seen in the [**Mock-ups**](#full-asset-mockups). The final general change was in the background colours for the elements in the **Services** and **Restaurants** sections. Initial there was supposed to be a contrast between elements, using a light brown (#C29C64) and a blue colour (#594C45) (see for example the contrasting backgrounds of the different Restaurants Section cards in the mockups). This didn't look well in practice, however, and it was decided to just use the blue colour, as it was more understated.

#### Mobile Changes

* **Google Maps API Section**  

    This element was initially supposed to appear above the **Services Section Text** element in the **Services Section**. This didn't really work in practice, however, as users would have been asked to browse the map without the context the **Services Text** provided. It was decided to use **Bootstrap's** inbuilt column ordering to make the Services Text appear before Google Maps on mobile, but to appear to the right of it on desktops and higher resolutions.

#### Tablet Changes

* **Google Maps API Section**  

    Originally meant to appear above **Services Section Text** element in the **Services Section**, it was decided to use the **Desktop** layout here instead, where these two elements are side by side with **Google Maps** to the left.

#### Desktop Changes

* **Logo**

    The **Logo** was initially supposed to swap corners with the **Navbar** on **Desktop** resolutions. It was believed that the Logo might clash with the lighter section of the **Landing Page** background image on higher resolutions. It did not clash, however, and so it was decided to use the same Landing Page layout for all platforms.

___

## **Features**

This is a single-page site with 6 main sections. The basic layout of the site was created using the [**Bootstrap 4**](https://getbootstrap.com) grid system (which is based on [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)), with alterations and additions. The core of this is the use of containers, rows and columns as classes for elements. All **anchor** links within text are fully navigable; they also change colour when hovered over (see [**Colours**](#colours)). On **Desktop**, the main sections alternate between ones with large and detailed fixed backgrounds (e.g. the **Landing Page Jumbotron**) and ones with the more muted dark brown (#594C45) background that scrolls (e.g. the **Services Section**). On **Mobile** devices these section's backgrounds still alternate, but their 'background-attached' value was changed from 'fixed' to 'scroll' via a **Media Query**, so that the whole page scrolls at the same time. This is because **iOS** does not support fixed backgrounds, as they take up too much system memory to run, which resulted in extremely focused-in and unappealing images.

### **Existing Features**

#### Base HTML

* **Base HTML**  

    This [image](assets/images/jumbotron.jpg) is a high quality file sourced on [**Pixabay**](https://pixabay.com/) which provides a striking backdrop to the **Landing Page**. It is presented via a **Jumbotron**, and scales across all platforms. On **Mobile** devices the 'background-attached' value was changed from 'fixed' to 'scroll' via a **Media Query**. This is because **iOS** does not support fixed backgrounds, as they take up too much system memory to run. 

* **Main Logo**  

    As the concept of **Elite Gourmet** is one I come up with myself, I have no proprietary icons or images to use as a banner logo for the site. Therefore, I simply used the chosen **Heading** font (_**Cinzel**_) for the landing page's main title. This element has an opaque background to keep it legible on the dark background of the **Hero Image**.

* **Navbar**  

    I modified the typical [**Bootstrap**](https://getbootstrap.com/docs/4.0/components/navbar) **Navbar** to suit the site. This included collapsing the Navbar into a **Burger Button** and fixing it to top left, so it would remain there while scrolling. I modified **Javascript** from [**JS Fiddle**](https://jsfiddle.net/wamosjk/ufhp9s15) to make an opaque Navbar background (rgba: 0, 0, 0, 0.6) for when the page scrolled. I also changed some of the styling to suit the site, selecting Bootstrap's 'navbar-dark' option so it could be seen over the muted colour palette, and changing the 'text-color' (#E0DFDF) for the same reason (along with colour changes for 'hover': #C29C64). On all platforms the Navbar goes to the top left of the screen, with the logo to the top right. It was initially planned that they would swap places for the **Desktop** version, but this was not deemed necessary (see [**Desktop Changes**](#desktop-changes) above).

* **Call to Action (CTA)**  

    There is a **CTA** at the bottom of the **Landing Page** envelope. This tells users that there is 20% off all services at the moment, and provides a link for them to click to get more information, bringing them to the **Services Section** of the page. The anchor for this link is the '20% off!' text, which was styled in light brown (#F7D29C, 'hover': #C29C64) to distinguish it from the main text (#FFF). The CTA element has an opaque background (rgba: 0, 0, 0, 0.6) to keep it legible over the darker colours of the **Hero Image**.

#### Main Page

????

#### List of Classes/Races

????

#### Create/Edit Classes/Races

???

#### List of Characters

???

#### New Character/Edit Character

???

#### New Game Page

???

#### Start Game Page

???

#### Game Location 1

????

#### Game Art Page

????

#### **Footer**

    The **Copyright Text** is a simple part of the **Bootstrap** grid, occupying the left-hand side of the **Footer** on small device sizes and up. It is a basic text element and does not display on XS resolutions. This de-clutters the screen on mobile devices.

### **Future Features**

* **Music and Sound Effect**  

    As this site ???

* **Full Game Adventure**  

    Selected Character in MongoDB stores info for game, feeds into the game GUI HUD, including Character profile and stats.

* **Character Basic Stat Roll**  

    As this site ???

* **Game Fighting Modal**  

    As this site ???

___

## **Technologies Used**

All the technologies used to create this project are listed below, along with their usage. Simply click on the title for a link to the main site. When there were separate instances where a technology was used, I have listed each link below.

[**HTML**](https://en.wikipedia.org/wiki/HTML5) - This project's structure is based on **HTML 5**.

[**CSS**](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This project's style was created using **CSS 3**.

[**Javascript**](https://en.wikipedia.org/wiki/JavaScript) -   A number of elements on the site have **Javascript** functionality (**JS 1.8.5**).

* There were [three plugins](https://getbootstrap.com/docs/4.5/getting-started/introduction) required so that **Bootstrap** would function; **jQuery**, **Popper.js** and **Bootstrap's** own **min.js**.
* I copied and modified **Javascript** code from [**Js Fiddle**](https://jsfiddle.net/wamosjk/ufhp9s15) to create transitions while scrolling.
* I copied **Javascript** code from [**Stack Overflow**](https://stackoverflow.com/questions/42401606/how-to-hide-collapsible-bootstrap-4-navbar-on-click) to make the Navbar collapse after an option was selected.
* I  used **Javascript** to get the [**Google Maps API**](https://developers.google.com/maps/documentation/javascript/tutorial) to function in the **Services Section**.
* I also used **Javascript** to give [**EmailJS**](https://www.emailjs.com/docs/sdk/installation/) functionality to my **Bookings Section**.

[**Python 3**](https://www.python.org/download/releases/3.0/) - This project's app routing was created using **Python 3**.

[**Flask**](https://flask.palletsprojects.com/en/1.1.x/) - This project's template logic was created using **Flask**.

[**MongoDB**](https://www.mongodb.com/) - This project's non-relational database is hosted by **MongoDB**.


<!-- [**SweetAlert**](https://sweetalert.js.org/guides/) - I found a dynamic alert for the **Contact Form** on SweetAlert's website. -->

<!-- Maybe delete SWeet ALert ref?? -->

[**Adobe XD**](https://www.adobe.com/ie/products/xd.html) - The wireframes and mockups for this site were designed in **Adobe XD**.

[**DBDiagram**](https://dbdiagram.io/) - The database schema for this site was designed with **DBDiagram**.

[**VSCode**](https://code.visualstudio.com) - All code for this site (including this README file), and all **Github** versioning of this code, was done with **VSCode**.

[**Git**](https://git-scm.com/) - I used **Git** to create this project's local repository and to maintain version control.

[**Github**](https://github.com) - The remote repository was done through **Github**.

[**Heroku**](https://www.heroku.com/) - The site was deployed live on **Heroku**.

[**Bootstrap**](https://getbootstrap.com) - The site was built using **Bootstrap's** grid system (**Bootstrap 4.5.0**).

* I also modified several **Bootstrap** components with my own targeted styles (e.g. **Navbar**).

<!-- Mention Grayscale here! PQ -->

[**Photoshop**](httpshttps://en.wikipedia.org/wiki/Adobe_Photoshopwww.gimp.org/) - I used **Photoshop** to edit all art and the **Favicon**.

[**HTML Code Checker**](https://validator.w3.org) - My HTML validator.

[**CSS Code Checker**](https://jigsaw.w3.org/css-validator) - My CSS validator.

[**CSS Auto-prefixer**](https://autoprefixer.github.io) - My selected auto-prefix checker.

[**Javascript Code Checker**](https://jshint.com/) - My JavaScript validator.

[**ARIA Checker**](http://wave.webaim.org/) - Selected ARIA validator.

[**BrowserStack**](https://www.browserstack.com/) - Multi-platform testing site.

___

## **Testing**

### **Testing Devices**

The site was tested on various devices, including on mobile, laptop and desktop platforms. I list these below:

#### **Mobile Devices**

* Galaxy A5 (Running Android Oreo 8.0.0)
* Fairphone 3 (Running Fairphone OS C20134228)
* iPhone XR (Running iOS 13)
* iPhone SE (Running iOS 13)
* iPhone 7 (Running iOS 13.4.1)
* iPhone 6 (Running iOS 12.4.4)

#### **Laptop Devices**

* HP Pavilion (Running Windows 10)
* Dell Latitude (Running Windows 10)
* MacBook Air (Running Mojave)

#### **Desktop Devices**

* Asus G20CB-UK032T Core i7-6700 (Running Windows 10)

### **Developer Tools**

I tested the site in **Developer Tools** on six internet browsers (**Chrome**, **Firefox**, **Opera**, **Edge**, **Internet Explorer** & **Safari**). Bugs and errors were tackled successfully in this way throughout the development process, using **Live Server** in **VSCode** and the deployed version of the site on **Github Pages**.

* [**Chrome**](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjwkK_qBRD8ARIsAOteukDltqXTjp13--esZkC4d8eL6Ggma28pvUQiVvwnJwVA06i0YbiSIuwaArNOEALw_wcB&gclsrc=aw.ds) (Version 81.0.4044.138)

* [**Firefox**](https://www.mozilla.org/en-US/firefox/new/) (Version 76.0.1)

* [**Opera**](https://www.mozilla.org/en-US/firefox/new/) (Version 68.0.3618.104)

* [**Edge**](https://www.mozilla.org/en-US/firefox/new/) (Version 44.18362.449.0)

* [**Internet Explorer**](https://www.microsoft.com/en-ie/download/internet-explorer.aspx) (Version 11.836.18362.0)

* [**Safari**](https://www.apple.com/lae/safari/) (Version 13.1)

I used the full gamut of responsivity in **Developer Tools**, but I also tested on the specific resolutions shown below:

#### **Mobile Resolutions**

* iPhone 4 (320 x 480)
* Galaxy S5 (360 x 640)
* iPhone X (375 x 812)

#### **Tablet Resolutions**

* iPad (768 x 1024)
* iPad Pro (1024 x 1366)

#### **Desktop Resolutions**

* Laptop with MDPI Screen (1280 x 800)
* Laptop with HiDPI Screen (1440 x 900)
* Gaming Desktop (2560 x 1440)
* 4K Monitor (3840 x 2160)
* 4k Plus (4000 x 2200)

### **BrowserStack**

[**BrowserStack**](https://www.browserstack.com/) - Any platform that I couldn't test in developer tools or on my own devices, I tested here.

### **Media Queries**

There are 21 separate **Media Queries** in the [**CSS**](assets/css/style.css) code. Every imaginable variation, from the smallest phone to the largest 4K monitor, was used to test the responsivity of the site. There are often multiple elements, functions and attributes being targeted and styled within in any one **Media Query**. These ensure that the site looks like it should from 240px in width to over 2500px.

### **Validation**

* [**HTML Code Checker**](https://validator.w3.org) - I checked my HTML with the **W3C Markup Validation Service**. It received the following message:

???

* [**CSS Code Checker**](https://jigsaw.w3.org/css-validator) - I checked my CSS with the **W3C CSS Validation Service**. It received the following message:

???

* [**CSS Auto-prefixer**](https://autoprefixer.github.io) - The **CSS Online Auto-prefixer** provided a **Vendor Prefix** check for my code. It received the following message:

???

* [**Javascript Code Checker**](https://jshint.com/) - I checked my Javascript with the **JS Hint**. It received the following message:

???

* [**ARIA Checker**](http://wave.webaim.org/) - I used **Wave** (Web Accessibility Evaluation Tool) to check that my code was accessible to all users.  It received the following message:

???

### **User Scenarios**

#### Gamer looking for a new interactive experience

* **Navbar**
    1. Go to the **Landing Page** section.
    2. Click on the **Navbar** on the top left of the screen.
    3. Click on the links to either **Services**, **Restaurants** of **About Us** for more information.

#### Fantasy gamebook Fan seeking nostalgic entertainment

* **Restaurants Section**:
    1. Use either the **Navbar** link to **Restaurants** or scroll down from the **Landing Page** to the **Restaurants Section**.
    2. Read through the information for each restaurant partner, including their cuisine, philosophy and location.

#### Game reviewer looking for a product to review

* **Google Maps API**:
    1. Use either the **Navbar** link to **Services** or scroll down from the **Landing Page** to the **Services Section**.
    2. Use the **Google Maps API** to locate the **Michelin** starred restaurants.
    3. Click on each location Marker Pin for a Google Maps Place ID and the restaurant address.

### **Outstanding Bugs**

#### Mobile Bugs

* **Galaxy A5 Using Android** - **Stutter on Scroll**  

    On a **Galaxy A5** running **Samsung's Internet Browser** on **Android Oreo** (8.0.0) there was a strange stutter effect on scroll. This seemed to be caused by the main **Hero Image** which forms the background for the landing page. It appears as if the image resizes as the user scrolls. I was unable to find a fix for this, or to find reference to it elsewhere. This did not happen on other devices, and did not greatly impact on the UI.

#### Desktop Bugs

* **Internet Explorer** - **Radio Selection Buttons Pushed to Far Left**  

    On an **Asus G20CB-UK032T** running **Internet Explorer** on **Windows 10** there was a problem with the **Radio Selection Buttons**, which appeared to the extreme left of the element. This happened on no other browser, and is probably caused by **Internet Explorer's** lack of compatibility with the most recent effects and transitions.

___

## **Deployment**

### **Local**

* This project is deployed live on [**Github Pages**](https://an-slua-sidhe.github.io/milestone-2).

* You can run the code in your chosen local **Integrated Development Environment** (**IDE**, e.g. [**VS Code**](https://code.visualstudio.com), [**AWS CLoud9**](https://aws.amazon.com/cloud9)).
    1. Open the **Project Repository** in [**Github**](https://github.com/an-slua-sidhe/milestone-2).
    2. Look for the green *Clone or Download* button at the top right of the repository.
    3. If using [**Github Desktop**](https://desktop.github.com), chose to *Open in Desktop*.
    4. If you want to **Clone** the files into a **Git** repository, chose to copy the URL from the same menu (# 2.). Open your chosen **Command Line Interface** (**CLI**, e.g. [**Gitbash**](https://git-scm.com/downloads)) and use the following command:

        ```bash
        git clone https://github.com/an-slua-sidhe/milestone-2.git
        ```

    5. To set up the files manually in a local repository, chose to **Download ZIP** and remove the files from the ZIP folder. Place them into the chosen location. If desired, set up a **Git** repository in this folder in your **CLI** with the following command:

        ```bash
        git init
        ```

    6. You can check the state of your repository after initialising it by using this command:

        ```bash
        git status
        ```

### **Remote**

* To push the code to a remote repository, follow the steps below (I use **Github** as an example).

    1. After using the command 'git status' (see step 6 above) in the command line, check that the console reads:

        ```bash
        Nothing to commit
        working tree clean
        ```

    2. Next, link your remote repository. For **Github**, open your Github account and select *Repositories*. At the top right of the screen select *New*.

    3. Give your repository a name. Keep it short and avoid underscores.

    4. You can now choose a few different ways to link the local and remote repositories. The one we want here is "…*or push an existing repository from the command line*". Copy the code this option gives you and paste it into your command line. It should look something like this:

        ```bash
        git remote add origin https://github.com/an-slua-sidhe/milestone-2
        git push -u origin master
        ```

    5. Now you can push any changes from the command line with:

        ```bash
        git push
        ```

    6. If you check the status of of your local repository now (using 'git status') it should give you something like this:

        ```bash
        On branch master
        Your branch is up-to-date with 'origin/master'.
        nothing to commit, working tree clean
        ```

    7. Finally, to deploy the code live with **Github Pages**, open the repository in your **Github** account and select '*settings*' at the top right of the page. Scroll down to the *Github Pages* section. Click on the '*None*' button. Select the correct branch from the menu. Now click on the URL link to visit the deployed site.

### **Heroku**

* To push the code to a remote repository, follow the steps below (I use **Github** as an example).

    1. After using the command 'git status' (see step 6 above) in the command line, check that the console reads:

        ```bash
        Nothing to commit
        working tree clean
        ```

    2. Next, link your remote repository. For **Github**, open your Github account and select *Repositories*. At the top right of the screen select *New*.

    3. Give your repository a name. Keep it short and avoid underscores.

    4. You can now choose a few different ways to link the local and remote repositories. The one we want here is "…*or push an existing repository from the command line*". Copy the code this option gives you and paste it into your command line. It should look something like this:

        ```bash
        git remote add origin https://github.com/an-slua-sidhe/milestone-2
        git push -u origin master
        ```

    5. Now you can push any changes from the command line with:

        ```bash
        git push
        ```

    6. If you check the status of of your local repository now (using 'git status') it should give you something like this:

        ```bash
        On branch master
        Your branch is up-to-date with 'origin/master'.
        nothing to commit, working tree clean
        ```

    7. Finally, to deploy the code live with **Github Pages**, open the repository in your **Github** account and select '*settings*' at the top right of the page. Scroll down to the *Github Pages* section. Click on the '*None*' button. Select the correct branch from the menu. Now click on the URL link to visit the deployed site.

___

## **Credits**

### **Code Used**

* **Navbar Collapse when link selected**  
    Copied from a snippet found on [**Stack Overflow**](https://stackoverflow.com/questions/42401606/how-to-hide-collapsible-bootstrap-4-navbar-on-click).

### **Images Used**

* All images were sourced from [**Pixabay**](https://pixabay.com/).
* Google Maps marker icon made by [Freepik](https://www.flaticon.com/authors/freepik) and sourced from [www.flaticon.com](https://www.flaticon.com/).

* Art Credits: Fighting Fantasy Covers (Forest of Doom, Deathtrap Dungeon(?))
* Pinterest
* Deviant Art
* Roger Dean piece
* Thief image
* Sláine image
* My own assets

### **Acknowledgements**

* Fighting fantasy link with mention of Steve Jackson adn Ian Livingstone
* Acknowledge Inkle and their version of Sorcery! asd link
* Acknowledge the influence fantasy and games had on a happy childhood :)

* I received inspiration for this project from the many wonderful cafes, restaurants and bars that are thriving in Cork and the surrounding regions. The passion for food and the constant raising of standards that are displayed year-on-year by the indigenous hospitality industry are incredible. As this project was finalised during the pandemic of 2020, I think it is fitting to wish all culinary creatives a fruitful and prosperous future.

<!-- ![Original Fantasy Game Location Banner](static/images/misc/banner_2.jpg "Original Fantasy Game Location Banner") -->