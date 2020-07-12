from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    book_btn = browser.find_element_by_id("book")
    book_btn.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer_holder = browser.find_element_by_id("answer")
    answer_holder.send_keys(y)

    button_and = browser.find_element_by_id("solve")
    button_and.click()

finally:
    time.sleep(10)
    browser.quit()