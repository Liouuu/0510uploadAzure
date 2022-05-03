from selenium import webdriver
import caseTools.logInAzure as logInAzure

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

account = "kim.liou@myviewboard.com" 
password = "Azure1111" 

driver.get("https://viewsonic-ssi.visualstudio.com/")
driver.maximize_window()

logInAzure.logInAzure(driver,account,password)
logInAzure.enter_projects(driver)


