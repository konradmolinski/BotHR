import os
import Libka
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

'''logowanko'''
driver.get('https://cvkodas.lt/en')
button_Employers = driver.find_element_by_class_name("btn-employers").click()
button_Add = driver.find_element_by_class_name("button.btn-add").click()
email_box = driver.find_element_by_id("login_email").send_keys('')
password_box = driver.find_element_by_id("login_password").send_keys('')
button_login = driver.find_element_by_class_name("btn-login").click()

'''sciezka z folderem'''
my_dir = r""
os.chdir(my_dir)
job_list = os.listdir('.')
job_list.remove('geckodriver.log')
counter = 0

for job in job_list:

    '''ustawianie sciezki i tresci'''
    os.chdir(my_dir + '\\' + job_list[counter])
    text_con = Libka.text_container()

    '''pisanko do boxow'''
    new_job_button = driver.find_element_by_class_name("btn-add").click()

    first_box = driver.find_element_by_id("title").send_keys(text_con[0])
    second_box = driver.find_element_by_id("description").send_keys(text_con[1])
    third_box = driver.find_element_by_id("description_requirements").send_keys(text_con[2])
    fourth_box = driver.find_element_by_id("description_offers").send_keys(text_con[3])
    fifth_box = driver.find_element_by_id("salary_from")
    fifth_box.clear()
    fifth_box.send_keys(text_con[4])

    '''listy'''
    first_list = driver.find_element_by_id("city_id")
    Select(first_list).select_by_visible_text("Abroad (Germany)")

    '''final click'''
    button_click = driver.find_element_by_class_name("btn-confirm").click()
    counter += 1