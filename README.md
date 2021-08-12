Today: 
1. Prevent Back button use
2. Deploy 
    * [x] Install NPM
    * [x] Update DB Info
    https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
    * [x] used: sudo apt install chromium-chromedriver
Next:

-------- 
* Deploy
--------
* Beautify Repo
* Authentication Options
* Testing
* Learn more about PostCss and PurgeCSS outside of TW

### Deployment Concerns
* Web Browser (Install & Install Binary for Selenium)
* Tailwind-re setup: NPM

### Prior: 
Day 1:
1. [X] Format Name List
2. [X] Selenium Form Entry
3. [X] Handle Data from Single Name
    * [X] Sort Page Source Data 
    * [X] Exception Handling
    * [X] Upgrade - Wait until Loaded
4. [X] Save Data to CSV

Day 2:
1. Loop Handle Data
    * conditional - new people, other sorting
    * [x] API (No Good)
    * [X] limit list to 50 and track last searched name
    * [X] Handle Error (Related to Looping?)
2. [X] Consider Deployment
3. [X] Django Basics (installed project and app, loading one page)
4. [X] Consider DB
5. [x] .env file (problem was it was different for Django)

Day 3: 
1. [X] Investigate Connection Methods
    * [X] Change Config to PSQL Defaults
2. [X] Create PSQL DB & Model
    * To see SQL used in migration in shell type: python manage.py sqlmigrate namesapp 0001
    * To check for problems: python manage.py check
3. [X] Handle Already Contacted Names
    * [X] Get List
    * [X] Sort Top 100
4. [X] Connect DB
    * [x] Show data in view

Day 4: 
1. [X] Page 3 of Tutorial
2. [X] View with Input
3. [x] Add old names to DB. Best way ? Create a command:
    * https://adityakedawat.medium.com/importing-csv-file-into-django-models-using-django-management-command-716eda305e61
4. [X] Page 4 of Tutorial

Day 5: 
1. [x] Tests Tutorial 
2. [x] 'with open'
3. [x] Keep track of current line (JSON)
    * Bug: If there's over 50, it won't advance. Will be fixed when DB is connected and checks names in list against names in DB
4. [x] Investigate Async for main.py
5. [x] Static Files Tutorial
6. [x] Django Page that adds One Person
7. [x] Test Main.py in Views

Day 6:
1. [x] Handle Data
    * [x] Check new names against DB names
    * [x] Send to DB
2. [x] book_and_case number as pk
3. [x] Get 50, Check & Display
4. [x] Read about deployment
5. [x] Setup env on VPS - installed and server running but didn't configure NginX
    * [x] pull from github
    * [x] postgres + DBs
    * [x] migrations
    * [x] install dependencies
        * [x] pykerberos error (installed things pykerberos was dependent on)

Day 7:
1. [x] Pass list data to next view
2. [x] Create header for view
3. [x] Create loading functionality for view
    * [x] dots
4. Beautify Pages
    * Install Tailwind CSS
5. [x] Investigate JS/React/Etc
    * Advantages of the server-first architecture for this project: With a client first (using React, Vue etc) Django's built-in support for templates, forms, and other front-end goodies are basically thrown out the window. Current setup leveraged built in Django views and templates, forms, the built-in login interface, etc.
    * graceful degreadation? (works without JS but is nicer with JS)

Day 8:
1. [x] Install Tailwind CSS
    * [x] Manage NPM install & build script
2. [x] Investigate & Fix Error in Scraping
3. [x] Accidentally Delete a Commit and have to re-do a bunch of stuff

Day 9: 
1. [x] Finalize Auth
    * [x] Add user via admin page
    * [x] Login-Logout Working

Day 10:
1. [x] Get redirects/links working in header
2. [x] Demand Login to View Pages/Redirect 
3. [x] Return List, CSV of All_Names
4. Improve Look of Home Page (links, etc)
    * [x] Display, Move Links
    * [x] Highlight/Hide Active Links
    * Tailwind for Header

Day 11: 
1. [x] Style Front Page
2. [x] Finish Styling Header
3. [x] Style Names List
4. [x] Style Login Screen
5. [x] Skeleton Next Pages
* How to Add Custom font to Tailwind (later)
Good styling resource/s: https://tailblocks.cc/
https://tailwindcomponents.com

Day 12:
1. [x] Style About Page 
2. [x] Handle Bad Logins
3. [x] Return View Options
4. [x] Keep Last Week's Searches
    * [x] Add to DB On Search
    * [x] Delete When Search is Re-Run
    * [x] Offer CSV (?)

Day 13:
1. [x] Previous Searches
    * [x] Show starting number
    * [x] Display in View
2. [x] Style CSV Button

Day 14: 
1. [x] Add Next 100 Names
2. [x] Set Default for Radio Button
3. [x] Beautify Loading Div