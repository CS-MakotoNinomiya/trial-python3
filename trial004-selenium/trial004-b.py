import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_NAME = "tools/chromedriver.exe"

try:
    path_base = os.path.dirname(os.path.abspath(__file__))
    driver_file = os.path.normpath(
        os.path.join(path_base, "../" + DRIVER_NAME))

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path=driver_file, options=options)

    driver.get('http://172.20.7.90/redmine/login')
    print("____ title : " + driver.title)

    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys("ninomiya")
    password.send_keys("MakotoNinomiya")
    time.sleep(1)

    login_button = driver.find_element_by_name("login")
    login_button.click()

    driver.get('http://172.20.7.90/redmine/projects/iij/wiki/Python3')
    print("____ title : " + driver.title)

    element = driver.find_element_by_xpath("//*[@id='content']/fieldset/legend")
    element.click()
    time.sleep(5)

    selector = driver.find_element_by_name("attachments[dummy][file]")
    selector.send_keys(os.path.normpath(
        os.path.join(path_base, "./download.pdf")))
    time.sleep(1)

    add_button = driver.find_element_by_name("commit")
    add_button.click()
    time.sleep(5)

except Exception as e:
    except_str = traceback.format_exc()
    print('==== exception traceback start.')
    print(except_str)
    print('==== exception traceback end.')
