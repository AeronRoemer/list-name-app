
# Names App

Full stack web scraper/data managment application built on Django/Python. It finds and return a list of information needed to contact currently incarcerated people. It uses a list of the top 250 most common last names in the US to perform the search. It helps users manage data by tracking previously searched names, making them available as HTML and as downloadable CSVs. Custom Django commands are availabel as well, allowing the developer initializing the app to load in a previously existing CSV. 
## Concepts Demonstrated

The main technologies and concepts used in this project:

* Django
* Python
* Selenium 
* Tailwinds
* Postgres 

### Login Pages

Tailwind CSS is used as part of a lightweight, responsive visual experience. The entire website is hidden behind a login screen. 

| Tablet Login | Mobile Login |
| --- | --- |
| ![Login Screen as Seen On Table](/img/login-med.png) | ![Login Screen as Seen On Mobile](/img/login-small.png) |


### Main Pages

| Search Page |
| -- |
| ![The main page to search, shows the current name being serached, the ability to choose hom many names to retrieve, and a CSV or web view option](/img/home-screen-mobile.png) |

| Search Page |
| -- |
| ![A table with the names, case numbers and facilities of incarcerated people. First names and case numbers are hidden for privacy reasons.](/img/searched-page.png) |

### Deployment 

Deployment has been an ongoing process because Nginx hasn't been letting Selenium access the wider web. 
