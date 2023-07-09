from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckBox:
    page_url = 'https://demoqa.com/checkbox'

    list_of_folders = ['Home', 'Documents', 'Office']
    selected_elements = ['Public', 'General']

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # For white-box
        self.folder_target_loc = '//span[@class="rct-title"][text()="{}"]//ancestor::span[@class="rct-text"]//button'
        # For black-box
        self.folder_loc = '//span[@class="rct-title"][text()]//ancestor::span[@class="rct-text"]//button'

    def open(self) -> 'PageCheckBox':
        self.driver.get(self.page_url)
        return self

    def expand(self, folder_name):
        loc = self.folder_target_loc.format(folder_name)
        svg = f'{loc}//*[@class]'
        element = self.driver.find_element(By.XPATH, svg)
        if 'close' in element.get_attribute('class'):
            self.driver.find_element(By.XPATH, loc).click()

    def is_folder_expanded(self, folder_name):
        loc = self.folder_target_loc.format(folder_name)
        svg = f'{loc}//*[@class]'
        element = self.driver.find_element(By.XPATH, svg)
        return 'open' in element.get_attribute('class')

    def collapse(self, folder_name):
        loc = self.folder_target_loc.format(folder_name)
        svg = f'{loc}//*[@class]'
        element = self.driver.find_element(By.XPATH, svg)
        if 'open' in element.get_attribute('class'):
            self.driver.find_element(By.XPATH, loc).click()

    def check(self, folder_name: str) -> None:
        label_loc = f'//label[@for="tree-node-{folder_name.lower()}"]'
        input_ = f'{label_loc}/input[@type="checkbox"]'
        element_label = self.driver.find_element(By.XPATH, label_loc)
        element_input = self.driver.find_element(By.XPATH, input_)
        if not element_input.is_selected():
            element_label.click()

    def uncheck(self, folder_name: str) -> None:
        label_loc = f'//label[@for="tree-node-{folder_name.lower()}"]'
        input_ = f'{label_loc}/input[@type="checkbox"]'
        element_label = self.driver.find_element(By.XPATH, label_loc)
        element_input = self.driver.find_element(By.XPATH, input_)
        if element_input.is_selected():
            element_label.click()

    def get_results(self) -> list:
        results_loc = '//div[@id="result"]//span[@class="text-success"]'
        results_elements = self.driver.find_elements(By.XPATH, results_loc)

        # results: list = []
        # for element in results_elements:
        #     results.append(element.text)

        results = [element.text for element in results_elements]
        return results



