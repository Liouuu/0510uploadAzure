from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from soupsieve import select
from selenium.webdriver.common.by import By

def logInAzure(driver, account, password):   
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(account) #輸入帳號
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#i0118"))).send_keys(password) #輸入帳號
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click() #是，保持登入  
                                                                                  
def enter_projects(driver):   #Driod #mvbX #     
    #要再找一個可以傳參數的標籤 wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label='+str(project)+']'))).click() #進 對應專案    
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Droid"]'))).click() #進對應專案
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Boards']"))).click()   #進Boards
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Queries']"))).click()  #進預先設好的Query:TestCaseOnly
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(string(),"TestCaseOnly")]'))).click()  #進預先設好的Query:TestCaseOnly

def enter_testcase(driver):   #testcase編號    
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="l1-search-input"]'))).send_keys('33689')
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[1]'))).click() #click search icon
    time.sleep(1)
    wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@aria-label="Add attachment"]'))).click()


