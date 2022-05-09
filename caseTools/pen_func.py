from time import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui



def open_menu(driver):        
    pen_butuon = driver.find_element_by_xpath('//div[@aria-label="t2b"]')
    pen_butuon.click()                 
    try: #如果menu沒有顯示，再按一次                                    
        WebDriverWait(driver, 3).until(                   
                EC.presence_of_element_located((By.XPATH, '//*[@id=\"toolbar-menu-layer\"]/div'))
            )
    except:
        pen_butuon.click()

def select_pen_type (driver, pen_type): #1 for marker, 2 for highlighter...
    WebDriverWait(driver, 10).until(                 
            EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(pen_type)+']/div/div/div'))
        )                                           
    pen = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(pen_type)+']/div/div/div')
    pen.click()


# def select_marker (driver):
#     WebDriverWait(driver, 10).until(                 
#             EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div[2]/div[2]/div[1]/div/div/div'))
#         )                               
#     marker = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[2]/div[2]/div[1]/div/div/div')
#     marker.click()

# def select_highlighter (driver): 
#     WebDriverWait(driver, 10).until(                 
#             EC.element_to_be_clickable((By.XPATH,'//*[@id="toolbar-menu-layer"]/div[2]/div[2]/div[2]/div/div'))
#         )                             
#     highlighter = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[2]/div[2]/div[2]/div/div')
#     highlighter.click()
#     try: #如果highlughter的menu沒有出現，再按一次
#         WebDriverWait(driver, 3).until(                                
#                 EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div[2]')) 
#             )
#     except:
#         highlighter.click()


def adjust_marker_thickness(driver, val):  #range of val is 0~35
    #select_pen_type(driver, 1)
    WebDriverWait(driver, 10).until(           
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div/div[3]/div/div[1]/div/div/div/span/span[3]"))
        )                     
    thickness_bar_thumb = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div/div[3]/div/div[1]/div/div/div/span/span[3]")
    thickness_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[1]/div/div/div/span/span[1]")  
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,-thickness_bar.size['width'],0).perform()  #都先拉到0
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,val*thickness_bar.size['width']/35,0).perform()

def adjust_marker_transparency(driver, val):   #range of val is 0~35
    #select_pen_type(driver, 1)
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div/div[3]/div/div[2]/div/div/div/span/span[3]"))
        )                                                 
    transparency_bar_thumb = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div/div[3]/div/div[2]/div/div/div/span/span[3]")
    transparency_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/div/span") 
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,-transparency_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,val*transparency_bar.size['width']/35,0).perform()

def adjust_highlighter_thickness(driver, val):  #range of val is 0~35
    #select_pen_type(driver, 2)
    pyautogui.moveTo(1646,589) #讓滑鼠經過，以消失tooltip
    pyautogui.moveTo(1675,660) 
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span/span[3]"))
        )
    thickness_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span/span[3]")
    thickness_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span")
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,-thickness_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,val*thickness_bar.size['width']/35,0).perform()
    time.sleep(0.5)    

                                
def adjust_laserpen_thickness(driver, val):  #range of val is 0~35
    #select_pen_type(driver, 3)
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span/span[3]"))
        )
    thickness_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span/span[3]")
    thickness_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div[3]/div/div[2]/div/div/span")
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,-thickness_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,val*thickness_bar.size['width']/35,0).perform()

def select_marker_up_color(driver, num): #range of num is 1~7
    #select_pen_type(driver, 1)
    time.sleep(0.5)
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[3]/div/div[3]/button['+str(num)+']/div') 
    color_up.click()

def select_marker_down_color(driver, num): #range of num is 1~128
    #select_pen_type(driver, 1)
    time.sleep(0.5)
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[3]/div/div/div[4]/button['+str(num)+']/div/div')
    color_up.click()

def select_highlighter_color (driver,num2): #num2=1-5
    #select_pen_type(driver, 2)               
    time.sleep(1)                          #//*[@id="toolbar-menu-layer"]/div/div[3]/div/div[1]/div/button['+str(num2)+']/div/div    
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[3]/div/div[1]/div/button['+str(num2)+']/div/div') 
    color_up.click()

def select_laserpen_color (driver,num3): #num2=1-5
    #select_pen_type(driver, 3)
    time.sleep(0.5)
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[3]/div/div[1]/button['+str(num3)+']/div/div')
    color_up.click()

def close_pen_menu(driver):
    driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div/div').click() 
                                                  

def DrawLine(X1,Y1,X2,Y2):    
    pyautogui.moveTo(X1, Y1, duration= 0.5)
    pyautogui.mouseDown()   
    pyautogui.moveTo(X2, Y2, duration= 0.5)
    pyautogui.mouseUp()
    time.sleep(1)

# def canvas_screenshot(driver, save_path):
#     canvas = driver.find_element_by_xpath('//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]')
#     canvas.screenshot(save_path)


# def click_pen_screenshot(driver, save_path):
#     pen_menu = driver.find_element_by_xpath('//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]')
#     pen_menu.screenshot(save_path)

# def menu_screenshot(driver, save_path):         # //*[@id=\"toolbar-menu-layer\"]/div[2]
#     pen_menu = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div")
#     pen_menu.screenshot(save_path)






