# from bs4 import BeautifulSoup
# import requests
# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.a)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# binary file needed for using browser
DRIVER_PATH = './driver/chromedriver'

# allows headless option where a Chrome window won't have to open
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# creates webdriver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")

current_name= "Smith"
try:
    # wait until current name form is present to add name and submit via click
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home_form:search_btn']")))
    driver.find_element_by_xpath("//*[@id='home_form:j_id_25']").send_keys(current_name)
    driver.find_element_by_xpath("//*[@id='home_form:search_btn']").click()
    print(driver.page_source)
    driver.quit()
except Exception as e: 
    print(e)
