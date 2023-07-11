from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageRadioButton:
    page_url = 'https://demoqa.com/radio-button'

    button_yes = 'Yes'
    button_impressive = 'Impressive'
    button_no = 'No'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.radio_button_loc = (By.XPATH, '//div[contains(@class, "custom-radio")]')
        self.target_radio_button_xpath = '//div[contains(@class, "custom-radio")][.="{}"]'
        self.output_form = (By.CSS_SELECTOR, 'p.mt-3')
        self.no_button = (By.CSS_SELECTOR, '#noRadio')

    def open(self) -> 'PageRadioButton':
        self.driver.get(self.page_url)
        return self

    def get_all_possible_radio_buttons(self) -> list:
        button_elements = self.driver.find_elements(*self.radio_button_loc)
        return [el.text for el in button_elements]

    def get_radio_button_by_text(self, button_name):
        root_loc = self.target_radio_button_xpath.format(button_name)
        input_loc = root_loc + '//input'
        input_el = self.driver.find_element(By.XPATH, input_loc)
        return input_el

    def check(self, button_name: str) -> None:
        root_loc = self.target_radio_button_xpath.format(button_name)
        label_loc = root_loc + '//label'
        input_loc = root_loc + '//input'
        label_el = self.driver.find_element(By.XPATH, label_loc)
        input_el = self.driver.find_element(By.XPATH, input_loc)
        if not input_el.is_selected():
            label_el.click()

    def check_button_is_selected(self, button_name: str) -> bool:
        root_loc = self.target_radio_button_xpath.format(button_name)
        input_loc = root_loc + '//input'
        input_el = self.driver.find_element(By.XPATH, input_loc)
        return input_el.is_selected()

    def get_output(self) -> str:
        field = self.driver.find_element(*self.output_form)
        return field.text

    def enable_button(self) -> None:
        button_name = self.driver.find_element(*self.no_button)
        self.driver.execute_script('arguments[0].removeAttribute("disabled")', button_name)
