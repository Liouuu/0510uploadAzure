from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from soupsieve import select
from selenium.webdriver.common.by import By
import pyautogui
width, height = pyautogui.size()
(1920, 1080)

def login_azure(driver, account, password):   
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#i0116'))).send_keys(account) #輸入帳號
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#i0118"))).send_keys(password) #輸入帳號
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#idSIButton9"))).click() #是，保持登入  
                                                                                  
def enter_projects(driver):   #Driod #mvbX...     
    #要再找一個可以傳參數的標籤 wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label='+str(project)+']'))).click() #進 對應專案    
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Droid"]'))).click() #進對應專案
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Boards']"))).click()   #進Boards
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Queries']"))).click()  #進預先設好的Query:TestCaseOnly
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(string(),"TestCaseOnly")]'))).click()  #進預先設好的Query:TestCaseOnly

def enter_testcase(driver):   #testcase編號...    
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="l1-search-input"]'))).send_keys('33689')
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[1]'))).click() #click search icon
    time.sleep(3)

def click_attachments(driver):                                                                 
    ul=wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/ul'))) #先定位role="tablist"的ul
    li = ul.find_elements_by_xpath('li') #往下找li
    li[-2].click() #點擊Attachments (固定會在倒數第二li)
    wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-new-item-container"))).click() #點擊Attachments +

def click_upload_file(X1,Y1,X2,y2):    
    pyautogui.moveTo(X1,Y1, duration= 0.5) #檔案路徑座標
    time.sleep(1)
    pyautogui.click(clicks=2)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a') 
    time.sleep(3)
    pyautogui.write('C:/Users/Liouki/sample_uploadAzure/excelUpload')  #excelUpload檔案路徑
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(X2, y2, duration= 0.5) #第一個檔案座標
    time.sleep(3)
    pyautogui.click(clicks=2)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'enter') #save
    time.sleep(3)










    


