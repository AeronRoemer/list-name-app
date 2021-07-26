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
xpaths = "/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[2]/td[1]"
current_name= "Smith"

try:
    # wait until current name form is present to add name and submit via click
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home_form:search_btn']")))
    # adds current name to last name search form area and submits search, driver holds results
    driver.find_element_by_xpath("//*[@id='home_form:j_id_25']").send_keys(current_name)
    driver.find_element_by_xpath("//*[@id='home_form:search_btn']").click()
    # gets rows and cols of table returned from search
    # 1 added to length to account for header, looks at all rows: /tbody/tr
    rows = 1 +len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr"))
    # looks at all cols in a given row: /tr[1]/
    cols = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[1]/td"))
    for row in range(2, rows):
        for col in range(1, cols+1):
            value = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[{col}]").text
            print(value)
    driver.quit()
except Exception as e: 
    print(e)

