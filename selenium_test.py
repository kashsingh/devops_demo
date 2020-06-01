from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://35.154.147.222/")
assert "Simple PHP Website" in driver.title
assert driver.find_element_by_id("Home")
assert driver.find_element_by_id("About Us")
assert driver.find_element_by_id("Products")
assert driver.find_element_by_id("Contact")
#assert driver.find_element_by_id("Noe")
driver.close()