from selenium import webdriver

# set the path to the webdriver executables - Noticed that this is not needed in python in current selenium version 4.8.2
# even the drivers do not need to be downloaded on pc
# gecko_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\geckodriver.exe"
# chrome_path = "C:\\Users\\jvancaelenberg\\Code\\Drivers\\chromedriver.exe"

# create a webdriver instance (firefox)
driver = webdriver.Firefox()

# go to webpage
driver.get("https://www.google.be")

# get title of page and print to console
page_title = driver.title
print(page_title)

# quit driver
# driver.quit()