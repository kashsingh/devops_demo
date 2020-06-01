from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set below options for AWS headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1400,1500")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("enable-automation")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")

print("Starting headless browser.")
driver = webdriver.Chrome(options=chrome_options)
print("Browser started")

print("Fetching URL")
driver.get("http://35.154.147.222/")

print("Executing tests")
assert "Simple PHP Website" in driver.title
assert driver.find_element_by_id("Home")
assert driver.find_element_by_id("About Us")
assert driver.find_element_by_id("Products")
assert driver.find_element_by_id("Contact")
print("All tests cleared")

# Uncomment below line to fail a test
#assert driver.find_element_by_id("Noe")

driver.close()