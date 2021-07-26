# from bs4 import BeautifulSoup
# import requests
# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.a)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = './driver/chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")
print(driver.page_source)
driver.quit()