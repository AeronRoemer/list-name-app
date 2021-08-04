Today: 
1. [x] Install Tailwind CSS
    * [x] Manage NPM install & build script
2. Add Auth
    * [x] Add user via admin page
3. [x] Investigate & Fix Error
4. [x] Accidentally Delete a Commit and have to re-do a bunch of stuff

Next:

* Beautify with Tailwind
* Consider Error Handling for User
* Keep Last Week's Searches
* Add next 100 names
* Clear DOM on back

### Deployment Concerns
* Web Browser (Install & Install Binary for Selenium)
* (FOR ASYNC) from root: uvicorn project.asgi:application 
    * or with flag --reload 
* Tailwind-re setup? 
* NPM

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