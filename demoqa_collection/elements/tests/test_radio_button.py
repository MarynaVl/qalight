import pytest
from demoqa_collection.pages.page_radio_button import PageRadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButton:

    def test_radio_button(self):
        page = PageRadioButton(self.driver)
        page.open()
        assert len(page.get_all_possible_radio_buttons()) == 3

    def test_select_yes_button(self):
        page = PageRadioButton(self.driver)
        page.open()
        button = page.button_yes
        page.check(button)
        output_text = page.get_output()
        assert button in output_text

    def test_select_impressive_button(self):
        page = PageRadioButton(self.driver)
        page.open()
        button = page.button_impressive
        page.check(button)
        output_text = page.get_output()
        assert button in output_text

    def test_no_button_is_selected(self):
        page = PageRadioButton(self.driver)
        page.open()
        button = page.button_no
        page.enable_button()
        page.check(button)
        assert page.check_button_is_selected(button)

    def test_radio_button_info(self):
        page = PageRadioButton(self.driver)
        page.open()
        radio_buttons = page.get_all_possible_radio_buttons()
        radio_button_info = {}
        for button in radio_buttons:
            button_element = page.get_radio_button_by_text(button)
            button_info = {
                'is enabled': button_element.is_enabled(),
                'is selected': button_element.is_selected()
            }
            radio_button_info[button] = button_info
        print(radio_button_info)
