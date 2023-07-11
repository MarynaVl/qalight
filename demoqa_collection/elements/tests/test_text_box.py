import pytest
from selenium.common import NoSuchElementException

from demoqa_collection.elements.pages.page_text_box import PageTextBox

user_data = {'fullname': 'Halyna Petrenko',
             'email': 'halyna@mail.com',
             'email_invalid': 'mail.com',
             'curr_addr': 'Ukraine, Kyiv',
             'perm_addr': 'Ukraine, Lviv'}


@pytest.mark.usefixtures('chrome')
class TestTextBox:

    def test_full_name(self):
        page = PageTextBox(self.driver)
        page.open().set_full_name(user_data.get('fullname'))
        page.submit()
        name = page.get_full_name()
        assert name == user_data['fullname']

    def test_email_positive(self):
        page = PageTextBox(self.driver)
        page.open().set_email(user_data.get('email'))
        page.submit()
        email = page.get_email()
        assert email == user_data['email']

    def test_email_negative(self):
        page = PageTextBox(self.driver)
        page.open()
        page.set_email(user_data.get('email_invalid'))
        page.submit()
        is_error_present = page.is_error_in_email_present()
        with pytest.raises(NoSuchElementException):
            page.get_email()
        assert is_error_present

    def test_curr_addr(self):
        page = PageTextBox(self.driver)
        page.open().set_curr_addr(user_data.get('curr_addr'))
        page.submit()
        curr_addr = page.get_curr_addr()
        assert curr_addr == user_data['curr_addr']

    def test_perm_addr(self):
        page = PageTextBox(self.driver)
        page.open().set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        perm_addr = page.get_perm_addr()
        assert perm_addr == user_data['perm_addr']

    def test_full_form_positive(self):
        page = PageTextBox(self.driver)
        page.open()
        page.set_full_name(user_data.get('fullname'))
        page.set_email(user_data.get('email'))
        page.set_curr_addr(user_data.get('curr_addr'))
        page.set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        name = page.get_full_name()
        email = page.get_email()
        curr_addr = page.get_curr_addr()
        perm_addr = page.get_perm_addr()
        if name == user_data['fullname']:
            name = True
        if email == user_data['email']:
            email = True
        if curr_addr == user_data['curr_addr']:
            curr_addr = True
        if perm_addr == user_data['perm_addr']:
            perm_addr = True
        assert all([name, email, curr_addr, perm_addr])

    def test_full_form_negative(self):
        page = PageTextBox(self.driver)
        page.open()
        page.set_full_name('')  # Empty full name
        page.set_email(user_data.get('email_invalid'))  # Invalid email format
        page.set_curr_addr('')  # Empty current address
        page.set_perm_addr('')  # Empty permanent address
        page.submit()
        output_form = page.get_output_form()
        is_email_error_present = page.is_error_in_email_present()
        with pytest.raises(NoSuchElementException):
            page.get_email()
        assert is_email_error_present
        assert not output_form.is_displayed()

