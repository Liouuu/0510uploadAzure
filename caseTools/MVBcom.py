from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as wait

def loginMVBcom(driver, account, password):
    WebDriverWait(driver, 10).until(                                #讓瀏覽器等待(最多10秒)，等到ID為"mat-input-0"的element出現才繼續進行
            EC.presence_of_element_located((By.CSS_SELECTOR,'#c_main > input.s1'))   
        )
    account_blank = driver.find_element_by_css_selector('#c_main > input.s1')
    account_blank.send_keys(account)
    login_but = driver.find_element_by_css_selector("#c_main > button.login-submit.inspect.s1")
    login_but.click()
    #WebDriverWait(driver, 10).until(
     #       EC.presence_of_element_located((By.XPATH, "/html/body/div/input[2]"))
     #   )
    time.sleep(2)
    password_blank = driver.find_element_by_css_selector("#c_main > input.s2")
    password_blank.send_keys(password)
    continue_but = driver.find_element_by_css_selector("#c_main > button.login-submit.submit.s2")
    continue_but.click()

def enter_classroom(driver):
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mat-card"))
        )
    driver.find_element_by_class_name("mat-card").click() #定位進Classroom的icon的html tag
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1]) #因為開分頁的關係，此code為切換程式run on的目標視窗
    # WebDriverWait(driver, 10).until(                              
    # EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div[3]/div/div[2]')) 
    #             )           
    # driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[2]").click()  #是否開啟新課程，點選確認

    try:    #處理出現「開啟多個教室...」時的情況 #如果有出現此狀況備註在testcase備註欄
        WebDriverWait(driver, 20).until(                                
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[3]/div/div[2]"))
                )
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[2]").click()  #點擊確認
        time.sleep(1)               
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()  #彈出框點擊重新整理
    except:
        pass
    wait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[1]/div/div"))).click() #關閉"what's new" 

    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div[2]/div/div[1]/img")) 
    #     )
    # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div[2]/div/div[1]/img").click()   #關閉開啟儀表板  


