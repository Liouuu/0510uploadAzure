import time
import sys
import os
o_path = os.getcwd() # 返回當前工作目錄
sys.path.append(o_path) # 新增自己指定的搜尋路徑import
import caseTools.MVBcom
import caseTools.pen_func
import caseTools.azure
import caseTools.drag_and_drop_to_canvas
import caseTools.export_table
import caseTools.screen_shot
import caseTools.check_and_reorgan_excel
import caseTools.canvas_compare
import caseTools.copy_to_new_folder
import caseTools.chrome_quitting
from selenium import webdriver

# options = webdriver.ChromeOptions() 
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# driver.get("https://stage.myviewboard.com/signin")
# driver.maximize_window()

#driver_Classroom
driver_Classroom=webdriver.Chrome(executable_path="chromedriver") #瀏覽器1
driver_Classroom.get("https://stage.myviewboard.com/signin")
driver_Classroom.maximize_window()
MVBcom_account = "kim.yj.liou@viewsonic.com" 
MVBcom_password = "Mandy877!" 

def case_33689 (driver_Classroom):  
#testcase上的step2
    return_list=caseTools.export_table.TestCase_steps('./excelTestcase/33689')   #讀testcase檔案 #得到list                             
    outputWorkbookFilename='33689_output'
    caseTools.export_table.new_sheet(outputWorkbookFilename)      #建立33689_output.excel
    caseTools.MVBcom.loginMVBcom(driver_Classroom,MVBcom_account,MVBcom_password)   #使用enetity account在MVB.com點擊開啟classroom
    caseTools.MVBcom.enter_classroom(driver_Classroom) 
    caseTools.pen_func.open_menu(driver_Classroom)                    #在右方工具列欄位雙擊筆的圖示 
    time.sleep(2)
    sample_open_pen_menu = "./img/sample/sample_open_pen_menu" + ".png"
    case_open_pen_menu = "./img/case/case_open_pen_menu" + ".png"  
    caseTools.screen_shot.pen_menu_screenshot(driver_Classroom,sample_open_pen_menu)
    time.sleep(1)
    caseTools.screen_shot.pen_menu_screenshot(driver_Classroom,case_open_pen_menu)
    result = caseTools.canvas_compare.canvas_compare_2(sample_open_pen_menu, case_open_pen_menu)
    time.sleep(2)
    if result == True:
        print("open_pen_menu pass")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[0], result='pass',img_path=case_open_pen_menu) 
    else:
        print("open_pen_menu Failed")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[0], result='Failed',img_path=case_open_pen_menu) 

#testcase上的step3
    caseTools.pen_func.select_pen_type(driver_Classroom,4)  #在選單上方筆的種類中選取AI PEN
    sample_select_AIpen = "./img/sample/sample_select_AIpen" + ".png"
    case_select_AIpen = "./img/case/case_select_AIpen" + ".png"  
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_select_AIpen)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_select_AIpen)
    result = caseTools.canvas_compare.canvas_compare_2(sample_select_AIpen, case_select_AIpen)
    time.sleep(2)
    if result == True:
        print("open_pen_menu pass")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[1], result='pass',img_path=case_select_AIpen) 
    else:
        print("open_pen_menu Failed")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[1], result='Failed',img_path=case_select_AIpen)

#testcase上的step4
    caseTools.pen_func.DrawLine(1170,415,1170,640)          #在AI PEN視窗右側畫畫
    sample_AIpen_draw = "./img/sample/sample_AIpen_draw" + ".png"
    case_AIpen_draw = "./img/case/case_AIpen_draw" + ".png"  
    time.sleep(4)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_AIpen_draw)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_AIpen_draw)
    result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_draw, case_AIpen_draw)
    time.sleep(2)
    if result == True:
        print("open_pen_menu pass")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[2], result='pass',img_path=case_AIpen_draw) 
    else:
        print("open_pen_menu Failed")

#testcase上的step5 
    caseTools.drag_and_drop_to_canvas.drag_and_drop_to_canvas(733,404,340,270)  #將搜尋結果拖曳至畫布上   
    sample_AIpen_to_canvas = "./img/sample/sample_AIpen_to_canvas" + ".png"
    case_AIpen_to_canvas = "./img/case/case_AIpen_to_canvas" + ".png" 
    time.sleep(4) 
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_AIpen_to_canvas)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_AIpen_to_canvas)
    result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_to_canvas, case_AIpen_to_canvas)
    time.sleep(2)
    if result == True:
        print("open_pen_menu pass")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[3], result='pass',img_path=case_AIpen_to_canvas) 
    else:
        print("open_pen_menu Failed")
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[3], result='Failed',img_path=case_AIpen_to_canvas)
    time.sleep(3)
    
case_33689(driver_Classroom)
caseTools.chrome_quitting(driver_Classroom) 
caseTools.check_and_reorgan_excel.check_and_reorgan_excel() #excelOutput內檔案只保留20個，超過則從舊的開始刪除
caseTools.copy_to_new_folder.copy_to_new_folder('33689') #excelOutput產生後，只複製最新一份至excelUpload

#driver_Azure
driver_Azure=webdriver.Chrome(executable_path="chromedriver") 
driver_Azure.get("https://viewsonic-ssi.visualstudio.com/")
driver_Azure.maximize_window()
Azure_account = "kim.liou@myviewboard.com" #固定使用此帳戶上傳
Azure_password = "Azure1111" 

caseTools.azure.login_azure(driver_Azure,Azure_account,Azure_password)
caseTools.azure.enter_projects(driver_Azure)
caseTools.azure.enter_testcase(driver_Azure)
caseTools.azure.click_attachments(driver_Azure)
caseTools.azure.click_upload_file(830,60,414,180) #830,60(檔案座標) 414,180(excelUpload第一個檔案座標)
caseTools.chrome_quitting(driver_Azure) 









