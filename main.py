import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from openai import OpenAI

# Specify the path to chromedriver inside the Downloads folder
service = Service('/Users/ibrahimmn/Downloads/chromedriver-mac-arm64/chromedriver')

# Specify the remote debugging address and port
options = Options()
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--headless")

# Create a webdriver instance using the Service object
driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://www.google.com")


from gpt import ask_question, CHAT_GPT_LINK

# ask_question(driver)

from focus_scarping_window import *

focus_scarping_window(driver)

exit(0)

input("Are you in units page? (Click enter to confirm): ")

# username: asaluau414124130059
# password: 786945

# print("looking for mandotory courses")
# # view mandatory courses
# view_button = WebDriverWait(driver, 60).until(
#     EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/div/div/a")))
# view_button.click()
#
# watch_course_button = WebDriverWait(driver, 60).until(
#     EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div/div[2]/table/tbody/tr/td[8]/div/button[1]")))
# watch_course_button.click()
#
#
# # Wait until a pop-up is loaded with "access course" button
# access_course = WebDriverWait(driver, 60).until(
#     EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button"))
# )
# access_course.click()



# /html/body/div[2]/div/section/div[2]/div/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div[22]/div/div/div/div[1]
# /html/body/div[2]/div/section/div[2]/div/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div[23]/div/div/div/div[1]
print("looking for unit button")
unit_15 = WebDriverWait(driver, 120).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/section/div[2]/div/div[1]/div/div[4]/div/div/div/div/div/div[2]/div/div[16]/div/div/div/div[1]")))
unit_15.click()

print("looking for start button")
start_button = WebDriverWait(driver, 120).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div[2]/div/button"))
)
start_button.click()


# Question
print("looking for question")
question = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/span[2]/span/span/div/div/div/span/span/section/section[1]/h4"))
    )
print(question.text)

question_desc = driver.find_element(By.CLASS_NAME, "questionDesc")
print(question_desc.text)

