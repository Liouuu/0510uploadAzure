from time import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui


def whole_canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath('//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]')
    canvas.screenshot(save_path)

def click_pen_icon_screenshot(driver, save_path):  # //*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]
    pen_menu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[5]/div/div[2]/div[5]')
    pen_menu.screenshot(save_path)

def pen_menu_screenshot(driver, save_path):         # //*[@id=\"toolbar-menu-layer\"]/div[2]
    pen_menu = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div")
    pen_menu.screenshot(save_path)