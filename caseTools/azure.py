from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import pyautogui
import caseTools.chrome_quitting
from selenium import webdriver
width, height = pyautogui.size()
(1920, 1080)
driver_Azure=webdriver.Chrome(executable_path="chromedriver") 

def login_azure(driver, account, password):   
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(account) #輸入帳號
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#i0118"))).send_keys(password) #輸入密碼
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click() #是，保持登入  
    except:
        print("login_azure出錯，關閉瀏覽器")
        caseTools.chrome_quitting(driver_Azure)
        pass 
   
                                                                                  
def enter_projects(driver,project_name):   #project_name= Driod mvbX...     
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="'+project_name+'"]'))).click() #進對應專案
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Boards']"))).click()   #進Boards
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Queries']"))).click()  #進預先設好的Query:TestCaseOnly
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(string(),"TestCaseOnly")]'))).click()  #進預先設好的Query:TestCaseOnly
    except:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(string(),"TestCaseOnly")]'))).click()  
        # wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'actions-column-wrapper'))).click()  #如果點不到的話透過classname再點一次

def enter_testcase(driver,caseID):   #testcase編號...       
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="l1-search-input"]'))).send_keys(caseID)
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[1]'))).click() #click search icon
    except:
        pyautogui.press('enter')  
    time.sleep(3)

def click_attachments(driver): 
    # try:
    #     ul=wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/ul'))) #先定位role="tablist"的ul
    # except:                                                                
    #     ul=wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/ul'))) #先定位role="tablist"的ul
    # li = ul.find_elements_by_xpath('li') #往下找li
    # li[-2].click() #點擊Attachments (固定是在倒數第二li)
    # wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul. div:nth-child(6)'))).click() 
    # wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'work-item-form-tabs'))).find_element_by_xpath("//div[contains(@aria-label, 'Attachments')]").click()                               
    # li = driver.find_element_by_class_name('work-item-form-tabs').find_element_by_xpath("//div[contains(@aria-label, 'Attachments')]")
    # li.click()
    # Attachments
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-new-item-container"))).click() #點擊Attachments + 
    except:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[contains(string(),"Add attachment")]'))).click() #點擊Attachments +



def click_upload_file(X1,Y1,X2,y2,excelUploadPath):    
    pyautogui.moveTo(X1,Y1, duration= 0.5) #檔案路徑座標
    time.sleep(1)
    pyautogui.click(clicks=2)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a') 
    time.sleep(3)
    pyautogui.write(excelUploadPath)  #你的excelUpload檔案路徑
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(X2, y2, duration= 0.5) #第一個檔案座標
    time.sleep(3)
    pyautogui.click(clicks=2)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'enter') #save
    time.sleep(3)









    


