

import time
import requests
from selenium.webdriver.common.keys import Keys
import sys
import os
o_path = os.getcwd() # 返回當前工作目錄
sys.path.append(o_path) # 新增自己指定的搜尋路徑import
import caseTools.MVBcom
import caseTools.pen_func
import caseTools.logInAzure
import caseTools.drag_and_drop_to_canvas
import caseTools.export_table
import caseTools.screen_shot
import caseTools.canvas_compare
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions() 
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# driver.get("https://stage.myviewboard.com/signin")
# driver.maximize_window()


driver_Classroom=webdriver.Chrome(executable_path="chromedriver")# 例項化瀏覽器 
# driver_Classroom.get("https://stage.myviewboard.com/signin")
# driver_Classroom.maximize_window()

MVBcom_account = "kim.yj.liou@viewsonic.com" 
MVBcom_password = "Mandy877!" 

def case_33689 ():  
#testcase上的step2
    # return_list=caseTools.export_table.TestCase_steps('./excelTestcase/33689')   #讀testcase檔案 #得到list                             
    # outputWorkbookFilename='33689_output'
    # caseTools.export_table.new_sheet(outputWorkbookFilename)      #建立33689_output.excel
    caseTools.MVBcom.loginMVBcom(driver_Classroom,MVBcom_account,MVBcom_password)   #使用enetity account在MVB.com點擊開啟classroom
    caseTools.MVBcom.enter_classroom(driver_Classroom) 
#     caseTools.pen_func.open_menu(driver)                    #在右方工具列欄位雙擊筆的圖示 
#     time.sleep(2)
#     sample_open_pen_menu = "./img/sample/sample_open_pen_menu" + ".png"
#     case_open_pen_menu = "./img/case/case_open_pen_menu" + ".png"  
#     caseTools.screen_shot.pen_menu_screenshot(driver,sample_open_pen_menu)
#     time.sleep(1)
#     caseTools.screen_shot.pen_menu_screenshot(driver,case_open_pen_menu)
#     result = caseTools.canvas_compare.canvas_compare_2(sample_open_pen_menu, case_open_pen_menu)
#     time.sleep(2)
#     if result == True:
#         print("open_pen_menu pass")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[0], result='pass',img_path=case_open_pen_menu) 

#     else:
#         print("open_pen_menu Failed")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[0], result='Failed',img_path=case_open_pen_menu) 

# #testcase上的step3
#     caseTools.pen_func.select_pen_type(driver,4)  #在選單上方筆的種類中選取AI PEN
#     sample_select_AIpen = "./img/sample/sample_select_AIpen" + ".png"
#     case_select_AIpen = "./img/case/case_select_AIpen" + ".png"  
#     caseTools.screen_shot.whole_canvas_screenshot(driver,sample_select_AIpen)
#     time.sleep(1)
#     caseTools.screen_shot.whole_canvas_screenshot(driver,case_select_AIpen)
#     result = caseTools.canvas_compare.canvas_compare_2(sample_select_AIpen, case_select_AIpen)
#     time.sleep(2)
#     if result == True:
#         print("open_pen_menu pass")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[1], result='pass',img_path=case_select_AIpen) 

#     else:
#         print("open_pen_menu Failed")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[1], result='Failed',img_path=case_select_AIpen)

# #testcase上的step4
#     caseTools.pen_func.DrawLine(1170,415,1170,640)          #在AI PEN視窗右側畫畫
#     sample_AIpen_draw = "./img/sample/sample_AIpen_draw" + ".png"
#     case_AIpen_draw = "./img/case/case_AIpen_draw" + ".png"  
#     time.sleep(4)
#     caseTools.screen_shot.whole_canvas_screenshot(driver,sample_AIpen_draw)
#     time.sleep(1)
#     caseTools.screen_shot.whole_canvas_screenshot(driver,case_AIpen_draw)
#     result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_draw, case_AIpen_draw)
#     time.sleep(2)
#     if result == True:
#         print("open_pen_menu pass")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[2], result='pass',img_path=case_AIpen_draw) 

#     else:
#         print("open_pen_menu Failed")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[2], result='Failed',img_path=case_AIpen_draw) 

# #testcase上的step5
#     caseTools.drag_and_drop_to_canvas.drag_and_drop_to_canvas(733,404,340,270)  #將搜尋結果拖曳至畫布上   
#     sample_AIpen_to_canvas = "./img/sample/sample_AIpen_to_canvas" + ".png"
#     case_AIpen_to_canvas = "./img/case/case_AIpen_to_canvas" + ".png" 
#     time.sleep(4) 
#     caseTools.screen_shot.whole_canvas_screenshot(driver,sample_AIpen_to_canvas)
#     time.sleep(1)
#     caseTools.screen_shot.whole_canvas_screenshot(driver,case_AIpen_to_canvas)
#     result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_to_canvas, case_AIpen_to_canvas)
#     time.sleep(2)
#     if result == True:
#         print("open_pen_menu pass")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[3], result='pass',img_path=case_AIpen_to_canvas) 

#     else:
#         print("open_pen_menu Failed")
#         caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[3], result='Failed',img_path=case_AIpen_to_canvas) 

# # case_33689 ()


# # # 自動化操作創研系統的線索導入功能
# # def ui_auto_operation():
# #     # 模擬登陸
# #     # rep = requests.Session()
# #     browser = webdriver.Firefox()
# #     browser.implicitly_wait(10)  # 設置隱性等待,等待10S加載出相關控件再執行之後的操作
# #     browser.maximize_window()
# #     browser.get('http://www.*******.com.cn/****/Login.aspx')
# #     # time.sleep(10) # 強制等待一般只用於測試
# #     # browser.refresh()
# #     # 輸入用戶名
# #     username = browser.find_element_by_xpath('//*[@id="txtUserName"]')
# #     username.clear()
# #     username.send_keys('*******')
# #     print('username input success')
# #     # 輸入密碼
# #     browser.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('******')
# #     print('password input success')
# #     # # 加載驗證碼
# #     # yzm = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[3]/dd/input')
# #     # yzm.send_keys(input('輸入驗證碼:'))
# #     # 點擊登陸
# #     browser.find_element_by_xpath('//*[@id="btnLogin"]').click()
# #     print('login success')
# #     # cookies = browser.get_cookies()
# #     # for cookie in cookies:
# #     #    rep.cookies.set(cookie['name'], cookie['value'])
# #     # 爬取對應網頁的數據
# #     browser.current_window_handle
# #     browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/div/a/span').click()
# #     # 切換到當前窗口
# #     browser.current_window_handle
# #     # time.sleep(5)
# #     tow_drive = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/ul/li[5]/a')
# #     tow_drive.click()
# #     print('turn success')
# #     browser.current_window_handle
# #     # time.sleep(2)
# #     # 切換到iframe框架裏面
# #     browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrame"]'))
# #     # # 輸入框只讀屬性的修改
# #     # js = 'document.getElementById("Text1").removeAttribute("readonly");'
# #     # browser.execute_script(js)
# #     # # 定位並且輸入路徑數據
# #     # receiveStart = browser.find_element_by_xpath('//*[@id="Text1"]')
# #     # receiveStart.clear()
# #     # receiveStart.send_keys('C:\\fakepath\\5096.xls')
# #     # # receiveStart.send_keys(Keys.RETURN)
# #     # 點擊上傳文件按鈕
# #     browser.find_element_by_xpath('//*[@id="btn1"]').click()
# #     # 調用寫好的exe實現上傳,autoup.exe的建立參考下面的網站
# #     # https://www.cnblogs.com/sunjump/p/7268805.html
# #     os.system("C:\\fakepath\\autoup.exe")
# #     # time.sleep(5)
# #     load = browser.find_element_by_xpath('//*[@id="btn_lead"]')
# #     load.click()
# #     try:
# #         # 每隔2s就去掃描彈出框是否存在,總時長是60s,存在就繼續執行之後代碼
# #         WebDriverWait(browser, 60, 2).until(EC.alert_is_present())
# #         # 處理彈出alert框
# #         alert = browser.switch_to.alert
# #         alert.accept()
# #     finally:
# #         browser.close()
# #         # browser.quit()


# # if __name__ == '__main__':
# #     # @version : 3.4
# #     # @Author  : robot_lei
# #     # @Software: PyCharm Community Edition
# #     ui_auto_operation()

# case_33689 ()

#開第二個瀏覽器
driver_Azure=webdriver.Chrome(executable_path="chromedriver") 
driver_Azure.get("https://viewsonic-ssi.visualstudio.com/")
driver_Azure.maximize_window()

Azure_account = "kim.liou@myviewboard.com" 
Azure_password = "Azure1111" 

caseTools.logInAzure.logInAzure(driver_Azure,Azure_account,Azure_password)
caseTools.logInAzure.enter_projects(driver_Azure)
caseTools.logInAzure.enter_testcase(driver_Azure)
print(os.getcwd()) 








