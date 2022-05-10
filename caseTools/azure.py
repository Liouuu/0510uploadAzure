from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import pyautogui
# import caseTools.chrome_quitting
from selenium import webdriver
import os
width, height = pyautogui.size()
(1920, 1080)
driver_Azure=webdriver.Chrome(executable_path="chromedriver") 

def login_azure(driver, account, password):   
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(account) #輸入帳號
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#i0118"))).send_keys(password) #輸入密碼
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click() #是，保持登入  
                                                                     
# def enter_projects(driver,project_name):   #project_name= Driod mvbX...     
#     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="'+project_name+'"]'))).click() #進對應專案
#     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Boards']"))).click()   #進Boards
#     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Queries']"))).click()  #進預先設好的Query:TestCaseOnly
#     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(string(),"TestCaseOnly")]'))).click()  #進預先設好的Query:TestCaseOnly
   
# def enter_testcase(driver,caseID):   #testcase編號...       
#     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="l1-search-input"]'))).send_keys(caseID)
#     try:
#         wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[1]'))).click() #click search icon
#     except:
#         pyautogui.press('enter')  
#     time.sleep(3)

def click_attachments(driver): 
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Attachments"]'))).click()
    time.sleep(3)

def upload_file(driver,previousOneFile,excelUploadPath): 
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="add-new-item-container"]'))).click()
        time.sleep(2)
    except:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add attachment']"))).click()
        time.sleep(2)
    finally:
        pass
    pyautogui.typewrite(os.path.abspath(excelUploadPath+previousOneFile))
    time.sleep(2)
    pyautogui.hotkey('enter') 
    time.sleep(2)
    # pyautogui.hotkey('ctrl', 'enter') #save
    # driver.quit
    # pyautogui.moveTo(X1,Y1, duration= 0.5) #檔案路徑座標
    # time.sleep(1)
    # pyautogui.click(clicks=2)
    # time.sleep(1)
    # pyautogui.hotkey('ctrl', 'a') 
    # time.sleep(3)
    # pyautogui.write(excelUploadPath)  #你的excelUpload檔案路徑
    # time.sleep(3)
    # pyautogui.press('enter')
    # time.sleep(3)
    # pyautogui.moveTo(X2, y2, duration= 0.5) #第一個檔案座標
    # time.sleep(3)
    # pyautogui.click(clicks=2)
    # time.sleep(3)
    # pyautogui.hotkey('ctrl', 'enter') #save

def delete_thePreviousOnefile(driver,previousOneFile):
    if previousOneFile!=None:
        try:                                                               
            wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='"+ previousOneFile + "']"))).click()  #上次丟的檔名
            pyautogui.hotkey('delete')
            time.sleep(1)
            wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='ok-button bolt-button enabled primary bolt-focus-treatment']"))).click()
            wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[class='menu-item drop-down-save save-only']"))).click()
            # pyautogui.hotkey('ctrl', 'enter') #save
        except:
            pass    

def getPreviousUploadFile(Filepath):
    try:
        previousOneFile=os.listdir(Filepath)
        print('previousOneFile等於',previousOneFile[0])
        return(previousOneFile[0])
    except:
        pass













    


