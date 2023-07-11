import pytest

from demoqa_collection.elements.pages.page_dynamic_properties import PageDynamicProperties


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def test_is_button_appears(self):
        page = PageDynamicProperties(self.driver)
        page.open()
        button = page.button_appeared()
        assert button.is_displayed()

    def test_is_button_enabled(self):
        page = PageDynamicProperties(self.driver)
        page.open()
        button = page.button_enabled_disabled()
        assert button.is_enabled()

    def test_is_button_color_changed(self):
        page = PageDynamicProperties(self.driver)
        page.open()
        button = page.button_change_color()
        initial_color = button.value_of_css_property('color')
        page.wait_for_text_danger()
        new_color = button.value_of_css_property("color")
        assert new_color != initial_color

        # дописати як отримати id
    def test_get_dynamic_text_id(self):
        page = PageDynamicProperties(self.driver)
        page.open()
        dynamic_text_id = page.get_dynamic_id_element_attrib('id')
        print(f'Dynamic text id: {dynamic_text_id}')
