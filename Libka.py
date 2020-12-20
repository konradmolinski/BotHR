import os
from selenium.webdriver.common.keys import Keys

def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)

def text_container():
    current_text = (os.listdir('.'))
    boxes = [''] * len(current_text)
    cntr = 0

    for text_name in current_text:
        with open(text_name, 'rt') as fin:
            for line in fin:
                boxes[cntr] += line
            cntr += 1
    return boxes

def list_scroller(scroll_element, element_to_click): 
    while True:
        scroll_element.send_keys(Keys.ARROW_DOWN)
        if element_to_click.is_displayed() == True:
            element_to_click.click()
            break
        else:
            pass