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
import caseTools.check_excel_amount
import caseTools.canvas_compare
import caseTools.copy_to_new_folder
import caseTools.chrome_quitting
from selenium import webdriver

# options = webdriver.ChromeOptions() 
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# driver.get("https://stage.myviewboard.com/signin")
# driver.maximize_window()

driver_Classroom=webdriver.Chrome(executable_path="chromedriver") #瀏覽器1
driver_Classroom.get("https://stage.myviewboard.com/signin")
driver_Classroom.maximize_window()
MVBcom_account = "kim.yj.liou@viewsonic.com" 
MVBcom_password = "Mandy877!" 

#開始創造caseID腳本
caseID='33689'
def case_33689 (driver_Classroom):  
#step2
    a=0
    return_list=caseTools.export_table.TestCase_steps('./excelTestcase/'+caseID)   #讀testcase檔案得到list #我從第四格B開始              
    outputWorkbookFilename= caseID+'_output'
    caseTools.export_table.new_sheet(outputWorkbookFilename)      #建立caseID_output.excel
    caseTools.MVBcom.loginMVBcom(driver_Classroom,MVBcom_account,MVBcom_password)   #使用enetity account在MVB.com點擊開啟classroom
    caseTools.MVBcom.enter_classroom(driver_Classroom) 
    caseTools.pen_func.open_menu(driver_Classroom)                    #在右方工具列欄位雙擊pen icon
    time.sleep(2)
    sample_open_pen_menu = "./img/sample/"+caseID+"sample_open_pen_menu" + ".png"
    case_open_pen_menu = "./img/case/"+caseID+"case_open_pen_menu" + ".png"  
    caseTools.screen_shot.pen_menu_screenshot(driver_Classroom,sample_open_pen_menu)
    time.sleep(1)
    caseTools.screen_shot.pen_menu_screenshot(driver_Classroom,case_open_pen_menu)
    result = caseTools.canvas_compare.canvas_compare_2(sample_open_pen_menu, case_open_pen_menu)
    time.sleep(2)
    if result == True:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Pass',img_path=case_open_pen_menu) 
    else:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Failed',img_path=case_open_pen_menu) 
    a=a+1
#step3
    caseTools.pen_func.select_pen_type(driver_Classroom,4)  #在選單上方筆的種類中選取AI PEN
    sample_select_AIpen = "./img/sample/"+caseID+"sample_select_AIpen" + ".png"
    case_select_AIpen = "./img/case/"+caseID+"case_select_AIpen" + ".png"  
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_select_AIpen)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_select_AIpen)
    result = caseTools.canvas_compare.canvas_compare_2(sample_select_AIpen, case_select_AIpen)
    time.sleep(2)
    if result == True:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Pass',img_path=case_select_AIpen) 
    else:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Failed',img_path=case_select_AIpen)
    a=a+1
#step4
    caseTools.pen_func.DrawLine(1170,415,1170,640)          #在AI PEN視窗右側畫畫
    sample_AIpen_draw = "./img/sample/"+caseID+"sample_AIpen_draw" + ".png"
    case_AIpen_draw = "./img/case/"+caseID+"case_AIpen_draw" + ".png"  
    time.sleep(4)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_AIpen_draw)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_AIpen_draw)
    result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_draw, case_AIpen_draw)
    time.sleep(2)
    if result == True:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Pass',img_path=case_AIpen_draw) 
    else:
        print('step4',return_list)
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Failed',img_path=case_AIpen_draw) 
    a=a+1
#step5 
    caseTools.drag_and_drop_to_canvas.drag_and_drop_to_canvas(733,404,340,270)  #將搜尋結果拖曳至畫布上   
    sample_AIpen_to_canvas = "./img/sample/"+caseID+"sample_AIpen_to_canvas" + ".png"
    case_AIpen_to_canvas = "./img/case/"+caseID+"case_AIpen_to_canvas" + ".png" 
    time.sleep(4) 
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,sample_AIpen_to_canvas)
    time.sleep(1)
    caseTools.screen_shot.whole_canvas_screenshot(driver_Classroom,case_AIpen_to_canvas)
    result = caseTools.canvas_compare.canvas_compare_2(sample_AIpen_to_canvas, case_AIpen_to_canvas)
    time.sleep(2)
    if result == True:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Pass',img_path=case_AIpen_to_canvas) 
    else:
        caseTools.export_table.export_table(outputWorkbookFilename,step=return_list[a],result='Failed',img_path=case_AIpen_to_canvas)
    time.sleep(3)
#caseID腳本結束

case_33689(driver_Classroom)
caseTools.chrome_quitting.chrome_quitting(driver_Classroom) 
caseTools.check_excel_amount.maintain_20("./excelOutput") #只留20份
caseTools.copy_to_new_folder.copy_to_new_folder(caseID) #最新的excel 檔名+上日期 複製到excelUpload資料夾
time.sleep(2)
caseTools.check_excel_amount.maintain_1("./excelUpload") #只留1份

#開始進入Azure並上傳最新檔案
driver_Azure=webdriver.Chrome(executable_path="chromedriver") 
driver_Azure.get("https://viewsonic-ssi.visualstudio.com/")
driver_Azure.maximize_window()
Azure_account = "kim.liou@myviewboard.com" #固定用此帳戶
Azure_password = "Azure1111" 

caseTools.azure.login_azure(driver_Azure,Azure_account,Azure_password)
caseTools.azure.enter_projects(driver_Azure)
caseTools.azure.enter_testcase(driver_Azure)
caseTools.azure.click_attachments(driver_Azure)
caseTools.azure.click_upload_file(830,60,414,180,'C:/Users/Liouki/sample_uploadAzure/excelUpload') #座標是固定的 830,60(檔案x1,y1) 414,180(第一個檔案清單x2,y2) ; #你的excelUpload檔案路徑
caseTools.chrome_quitting.chrome_quitting(driver_Azure) 
#Azure上傳動作全部結束









