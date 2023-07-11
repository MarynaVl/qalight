from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageTextBox:
    page_url = 'https://demoqa.com/text-box'

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.submit_btn_loc: tuple = (By.CSS_SELECTOR, 'button#submit')
        self.full_name_field_loc: tuple = (By.CSS_SELECTOR, 'input#userName')
        self.email_field_loc: tuple = (By.CSS_SELECTOR, 'input#userEmail')
        self.curr_addr_text_area_loc: tuple = (By.CSS_SELECTOR, 'textarea#currentAddress')
        self.perm_addr_text_area_loc: tuple = (By.CSS_SELECTOR, 'textarea#permanentAddress')
        self.output_fullname_loc: tuple = (By.CSS_SELECTOR, 'p#name')
        self.output_email_loc: tuple = (By.CSS_SELECTOR, 'p#email')
        self.output_curr_addr: tuple = (By.CSS_SELECTOR, 'p#currentAddress')
        self.output_perm_addr: tuple = (By.CSS_SELECTOR, 'p#permanentAddress')
        self.output_form: tuple = (By.CSS_SELECTOR, '#output')

    def open(self) -> 'PageTextBox':
        self.driver.get(self.page_url)
        element = self.driver.find_element(By.CSS_SELECTOR, 'div.main-header')
        assert element.is_displayed()
        return self

    def fill_full_name(self, full_name: str) -> 'PageTextBox':
        field = self.driver.find_element(*self.full_name_field_loc)
        field.send_keys(full_name)
        return self

    def set_full_name(self, full_name: str) -> 'PageTextBox':
        field = self.driver.find_element(*self.full_name_field_loc)
        field.clear()
        field.send_keys(full_name)
        return self

    def set_email(self, email: str) -> 'PageTextBox':
        field = self.driver.find_element(*self.email_field_loc)
        field.clear()
        field.send_keys(email)
        return self

    def set_perm_addr(self, perm_address: str) -> 'PageTextBox':
        field = self.driver.find_element(*self.perm_addr_text_area_loc)
        field.clear()
        field.send_keys(perm_address)
        return self

    def set_curr_addr(self, curr_address: str) -> 'PageTextBox':
        field = self.driver.find_element(*self.curr_addr_text_area_loc)
        field.clear()
        field.send_keys(curr_address)
        return self

    def get_email_field_attribute(self, attr) -> str:
        field = self.driver.find_element(*self.email_field_loc)
        attribute = field.get_attribute(attr)
        return attribute

    def is_error_in_email_present(self) -> bool:
        is_error_present = 'field-error' in self.get_email_field_attribute('class')
        return is_error_present

    def get_full_name(self) -> str:
        field = self.driver.find_element(*self.output_fullname_loc)
        return field.text.split(':')[1].strip()

    def get_email(self) -> str:
        field = self.driver.find_element(*self.output_email_loc)
        return field.text.split(':')[1].strip()

    def get_email_field_attrib(self, attribute) -> str:
        attrib = self.driver.find_element(*self.email_field_loc).get_attribute(attribute)
        return attrib

    def get_curr_addr(self) -> str:
        field = self.driver.find_element(*self.output_curr_addr)
        return field.text.split(':')[1].strip()

    def get_perm_addr(self) -> str:
        field = self.driver.find_element(*self.output_perm_addr)
        return field.text.split(':')[1].strip()

    def get_output_form(self):
        output_form = self.driver.find_element(*self.output_form)
        return output_form

    def submit(self):
        submit_button = self.driver.find_element(*self.submit_btn_loc)
        # Scroll the page with JavaScript
        self.driver.execute_script('arguments[0].scrollIntoView();', submit_button)
        # Scroll the page with ActionChains
        # action = ActionChains(self.driver).scroll_to_element(submit_button)
        # action.perform()
        submit_button.click()
