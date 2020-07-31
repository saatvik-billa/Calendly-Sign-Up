from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('') # path to chromedriver on your computer

# ---- FOR SCHEDULING SESSIONS ---- 

months_list = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
]

days_to_sign_up = [] # list of days (as strings) that you would like to sign up on (i.e. ['5', '12']

desired_month = '' # month of your session

if (months_list.index(desired_month)+1 < 10):
  month_num = f'0{months_list.index(desired_month)+1}'
elif (months_list.index(desired_month)+1 >= 10):
  month_num = f'{months_list.index(desired_month)+1}'

name = '' # your name
email = '' # your email
phone = '' # your number
url_endpoint = '' # unique endpoint calendly assigns to each host's account

for day in days_to_sign_up:
    driver.get(f'https://calendly.com/{url_endpoint}/60?back=1&month=2020-0{month_num}') 
    time.sleep(3)
    sign_up_day = driver.find_elements_by_xpath('//button[@class="_2lqEN___day-Button__cls1 U5hxE___day-Button__bookable _1Qg-r___BareButton__cls1 _2zIir___index-UnstyledButton__cls1"]')

    for i, s in enumerate(sign_up_day):
        if (s.text == day):
            sign_up_day[i].click()
            break
        else:
            continue

    time.sleep(2)
    driver.find_element_by_xpath('//button[@data-start-time="9:00am"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@data-container="confirm-button"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@name="full_name"]').send_keys(name)
    driver.find_element_by_xpath('//input[@name="email"]').send_keys(email)
    phone_numbers = driver.find_elements_by_xpath('//input[@type="tel"]')
    for p in phone_numbers:
        p.send_keys(phone)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(2)

driver.quit()

# SOME THINGS TO FIX
    # Make an option to select the time (right now it is hardcoded to 9:00 am) -- maybe include some user input functionality


