from time import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def drag_and_drop_to_canvas(X1,Y1,X2,Y2):    
    pyautogui.moveTo(X1, Y1, duration= 0.5)
    pyautogui.mouseDown()   
    pyautogui.moveTo(X2, Y2, duration= 0.5)
    pyautogui.mouseUp()
    time.sleep(1)