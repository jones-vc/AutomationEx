from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set the path to the webdriver executables
# gecko_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\geckodriver.exe"
# chrome_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\chromedriver.exe"

# create a ChromeOptions object to configure Chrome driver...
chrome_options = Options()
# ... to keep chrome and chromedriver open ...
chrome_options.add_experimental_option("detach", True)

# ... and to avoid error messages in terminal that can be safely ignored
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# create a webdriver instance (chrome)
driver = webdriver.Chrome(options=chrome_options)

# go to webpage
driver.get("https://www.google.be")

# get title of page and print to console
page_title = driver.title
print(page_title)

# quit driver
# driver.quit()