import time

import pytest

from demoqa_collection.pages.page_alerts import PageAlerts


@pytest.mark.usefixtures('chrome')
class TestAlerts:

    def test_just_alert(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.just_alert()
        assert alert.text == 'You clicked a button'
        alert.accept()

    # дописати
    def test_timed_alerts(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.timed_alert()

    # дописати
    def test_confirm_box(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.confirm_box()

    def test_prompt_box(self):
        text = 'text to prompt box'
        page = PageAlerts(self.driver)
        page.open()
        alert = page.prompt_box()
        alert.send_keys(text)
        alert.accept()
        assert page.get_prompt_box_result()

