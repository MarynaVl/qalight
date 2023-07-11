import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageDynamicProperties:

    url = 'https://demoqa.com/dynamic-properties'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.dynamic_id_element_loc = By.XPATH, '//div/p[text()][not(contains(@id, "error"))][not(@jsselected)]'
        self.enable_disable_button_loc = By.CSS_SELECTOR, '#enableAfter'
        self.change_color_button_loc = By.CSS_SELECTOR, '#colorChange'
        self.appear_button_loc = By.CSS_SELECTOR, '#visibleAfter'
        self.change_color_text_danger = By.CSS_SELECTOR, '#colorChange.text-danger'

    def open(self) -> 'PageDynamicProperties':
        self.driver.get(self.url)
        return self

    def get_dynamic_id_element_attrib(self, attribute: str) -> str:
        element = self.driver.find_element(*self.dynamic_id_element_loc)
        return element.get_attribute(attribute)

    def button_enabled_disabled(self) -> WebElement:
        button = self.driver.find_element(*self.enable_disable_button_loc)
        WebDriverWait(self.driver, 6).until(ec.element_to_be_clickable(button))
        return button

    def button_change_color(self) -> WebElement:
        button = self.driver.find_element(*self.change_color_button_loc)
        return button

    def button_appeared(self) -> WebElement:
        return WebDriverWait(
            self.driver, timeout=6).until(
            ec.visibility_of_element_located(self.appear_button_loc))

    def wait_for_text_danger(self):
        return WebDriverWait(self.driver, timeout=6).until(
            ec.presence_of_element_located(self.change_color_text_danger))
