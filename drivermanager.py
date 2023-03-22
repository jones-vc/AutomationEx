from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# create custom class DriverManager
class DriverManager:
    
    # driver is a static variable to later hold the driver instance
    # the variable is initialised with None to signify "empty"
    driver = None 
    
    # https://www.geeksforgeeks.org/class-method-vs-static-method-python/
    @staticmethod
    def get_driver(): # defining the method get_driver
        if DriverManager.driver is None: # check if driver has not already been initialized
            DriverManager.set_chrome_driver() # if so (not initialized), set Chrome driver by default by calling set_chrome_driver function
        return DriverManager.driver

    @staticmethod
    def set_chrome_driver():
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        DriverManager.driver = webdriver.Chrome(options=chrome_options)

    @staticmethod
    def set_firefox_driver():
        DriverManager.driver = webdriver.Firefox()

    @staticmethod
    def kill_driver():
        if DriverManager.driver is None:
            print("There is no active driver. Nothing to kill") # if driver has not been initialized, print message indicating no active driver
        else:
            print("Killing the driver")
            DriverManager.driver.quit() # working?
            DriverManager.driver = None 