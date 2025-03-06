import random
import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as selenium_exceptions
from pynput.keyboard import Controller

from focus_scarping_window import focus_scarping_window

CHAT_GPT_LINK = "https://www.chatgpt.com/"

def initialize_gpt(driver):

    driver.execute_script(f'window.open("{CHAT_GPT_LINK}", "_blank");')

    # Switch to the chatgpt tab
    driver.switch_to.window(driver.window_handles[1])

def click_stay_logged_out(driver: WebDriver, delay: bool):
    try:
        if delay:
            element = WebDriverWait(driver, 25).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/a")))
        else:
            element = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/a")
        element.click()
    except:
        return

def ask_question(driver: WebDriver):

    if "chatgpt.com" in driver.current_url:

        ques = input("Ask me anything: ")

        # select text field
        text_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div[2]/div/div/div/div/div/div[4]/form/div/div/div/div/div[1]")))
        text_box.click()

        keyboard = Controller()
        time.sleep(2)
        focus_scarping_window()
        for letter in ques:
            time.sleep(random.uniform(0.070, 0.233))
            keyboard.type(letter)

    else:
        if len(driver.window_handles) < 2:
            driver.execute_script(f'window.open("{CHAT_GPT_LINK}", "_blank");')
            # close this popup
            click_stay_logged_out(driver, delay=True)
        else:
            for i in range(len(driver.window_handles)):
                if "chatgpt.com" in driver.current_url: break

                driver.switch_to.window(driver.window_handles[i])
                # sometimes when you switch back to logged out chatgpt tab it suddenly shows this popup
                click_stay_logged_out(driver, delay=False)
            ask_question(driver)