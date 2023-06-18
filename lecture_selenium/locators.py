from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = Chrome(service=service)

driver.get('https://demoqa.com/text-box')
user_form = driver.find_element(By.ID, 'userForm')
full_name_fild = user_form.find_element(By.ID, 'userName')
full_name_fild.send_keys('Vasyl Shevchenko')
text = full_name_fild.get_attribute('value')

email_field = user_form.find_element(By.ID, 'userEmail')
email_field.send_keys('shevchenko@mail.com')

current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('My current address')

permanent_address = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
permanent_address.send_keys('My permanent address')

assert permanent_address.get_attribute('value') == 'My permanent address'

driver.quit()

