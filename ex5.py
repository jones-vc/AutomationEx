from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Import custom classes
from drivermanager import DriverManager
#from pageobjects import LoginPage
# from pageobjects import LoginPage, MenuPage, WelcomePage

# Initialize driver with get_driver function from DriverManager class
driver = DriverManager.get_driver() # Drivermanager.get_driver()

# Navigate to webpage - to be included in login method?
driver.get("https://satrngselcypr.z16.web.core.windows.net/")

# call logout method from MenuPage class first

# call login method from LoginPage class



# new_login = login("admin", "superduper")
username = "admin"
password = "superduper"
# PageObjects.login(username, password)

# DriverManager.get_driver().get("https://satrngselcypr.z16.web.core.windows.net/")
    
# Create instances of the page objects
# menu = MenuPage()
# login = LoginPage()
# welcome = WelcomePage()
    
# Initialize the page object elements
# menu.initElements()
# login.initElements()
# welcome.initElements()
    
# Logout, set language to French, and login with credentials
# menu.logout()
# login.setLanguageTo("French")
# login.loginWith("admin", "superduper")
    
# Wait for the welcome message to load and check if it contains "Welcome"
# WebDriverWait(DriverManager.getDriver(), 10).until(EC.presence_of_element_located((By.ID, "welcomeMessage")))
# if "Welcome" in welcome.getWelcomeMessage():
#     print("PASSED: Welcome message does contain welcome")
# else:
#     print("FAILED: Welcome message doesn't contain welcome")
    
# Kill the driver instance
# DriverManager.killDriver()