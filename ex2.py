from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set the path to the webdriver executables
gecko_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\geckodriver.exe"
chrome_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\chromedriver.exe"

# to keep chrome and chromedriver open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# create a webdriver instance (chrome)
driver = webdriver.Chrome(chrome_options=chrome_options)

# go to webpage
driver.get("https://www.google.be")

# get title of page and print to console
page_title = driver.title
print(page_title)

# navigate to bing and print the title
driver.get("https://www.bing.com")
page_title2 = driver.title
print(page_title2)

# go back to google and check if title is the same
driver.back()
if driver.title == page_title:
    print("passed")
else:
    print("failed")

# quit driver
driver.quit()
