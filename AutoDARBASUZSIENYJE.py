import os
import time
import Libka
from selenium import webdriver
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

'''logowanko'''
driver.get('http://www.darbasuzsienyje.org/')
email_box = driver.find_element_by_name("login")
email_box.send_keys('')
password_box = driver.find_element_by_name("pass")
password_box.send_keys('')
button_login = driver.find_element_by_id("btn_login").click()

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
    checkbox_name = text_con[-1]
    '''pisanko do boxow'''
    time.sleep(2)
    new_job_button = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/div[2]").click()

    first_box = driver.find_element_by_name("job_name").send_keys(text_con[0])

    first_list = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                              "/tbody[1]/tr[2]/td[2]/div[1]/dl[1]/dt[1]").click()
    choose_value = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[2]"
                                                "/td[2]/div[1]/dl[1]/div[1]/dd[1]/div[1]/ul[1]/li[3]/div[1]").click()

    checkbox = driver.find_element_by_xpath("//*[contains(text(), '%s')]//ancestor::span" % checkbox_name).click()

    second_box = driver.find_element_by_name("city_and_location").send_keys(text_con[1])
    third_box = driver.find_element_by_name("job_type_text").send_keys(text_con[2])
    fourth_box = driver.find_element_by_name("job_addi_info").send_keys(text_con[3])
    fifth_box = driver.find_element_by_name("job_requirements").send_keys(text_con[4])
    sixth_box = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                             "/tbody[1]/tr[9]/td[2]/input[1]").send_keys(text_con[5])
    seventh_box = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                             "/tbody[1]/tr[11]/td[2]/input[1]").send_keys(text_con[6])
    eight_box = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                             "/tbody[1]/tr[12]/td[2]/input[1]").send_keys(text_con[7])

    '''listy'''
    second_list = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                               "/tbody[1]/tr[11]/td[2]/div[1]/dl[1]/dt[1]")
    choose_value1 = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[11]"
                                                 "/td[2]/div[1]/dl[1]/div[1]/dd[1]/div[1]/ul[1]/li[4]/div[1]")
    Libka.scroll_shim(driver, second_list)
    ActionChains(driver).move_to_element(second_list).click(second_list).click(second_list).move_to_element(choose_value1)\
        .click(choose_value1).click(choose_value).perform()

    third_list = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]"
                                              "/tbody[1]/tr[12]/td[2]/div[1]/dl[1]/dt[1]")
    choose_value2 = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[12]"
                                                 "/td[2]/div[1]/dl[1]/div[1]/dd[1]/div[1]/ul[1]/li[2]/div[1]")
    ActionChains(driver).move_to_element(third_list).click(third_list).move_to_element(choose_value2)\
        .click(choose_value2).perform()

    '''listy z datami'''
    the_future_date = date.today() + timedelta(days = 14)

    year_list = driver.find_element_by_name("valid_yy")
    the_year = driver.find_element_by_xpath("//div[contains(text(),'%s')]" % the_future_date.year)
    ActionChains(driver).move_to_element(year_list).click(year_list).move_to_element(the_year).click(the_year).perform()

    month_list = driver.find_element_by_name("valid_mm")
    scroll = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[16]/td[2]"
                                          "/div[2]/dl[1]/div[1]/dd[1]/div[1]")
    the_month = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[16]/td[2]"
                                             "/div[2]/dl[1]/div[1]/dd[1]/div[1]/ul[1]/li[%s]/div[1]"
                                             % (the_future_date.month + 1))
    ActionChains(driver).move_to_element(month_list).click(month_list).perform()
    ActionChains(driver).move_to_element(scroll).click_and_hold(scroll).perform()
    Libka.list_scroller(scroll, the_month)

    day_list = driver.find_element_by_name("valid_dd")
    scroll_1 = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[16]"
                                            "/td[2]/div[3]/dl[1]/div[1]/dd[1]/div[1]")
    the_day = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[3]/table[1]/tbody[1]/tr[16]/td[2]"
                                          "/div[3]/dl[1]/div[1]/dd[1]/div[1]/ul[1]/li[%s]/div[1]" % (the_future_date.day +1))
    ActionChains(driver).move_to_element(day_list).perform()
    ActionChains(driver).click(day_list).click(day_list).perform()
    ActionChains(driver).move_to_element(scroll_1).click_and_hold(scroll_1).perform()
    Libka.list_scroller(scroll_1, the_day)
    '''wstawianie jpg'''
    os.chdir('..')
    driver.find_element_by_name("file").send_keys(os.getcwd()+"")



    '''final button'''
    submit_button = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[2]/form[1]/div[5]").click()
    counter += 1


