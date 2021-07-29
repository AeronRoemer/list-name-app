Today: 
1. [X] Page 3 of Tutorial
2. [X] View with Input
3. [x] Add old names to DB. Best way ? Create a command:
    * https://adityakedawat.medium.com/importing-csv-file-into-django-models-using-django-management-command-716eda305e61

Next:
* Continue Tutorial
* Consider Output Format vs. Document Storage CSV, SQL Tables
    * Push Names to Table, Store Other data Temporarily. 
* Consider Deployment
* Handle Data: sorting, storage
* Consider 'Loading' wait screen for name retrieval. 
* Consider Front End
* Consider Oauth


### Deployment Concerns
* Web Browser (Install & Install Binary for Selenium)
* Is the Git repo Okay cause I didn't already make the driver a binary
* Install PSQL and create DB 

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