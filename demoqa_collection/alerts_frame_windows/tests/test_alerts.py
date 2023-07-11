import pytest

from demoqa_collection.alerts_frame_windows.pages.page_alerts import PageAlerts


@pytest.mark.usefixtures('chrome')
class TestAlerts:

    def test_just_alert(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.get_just_alert()
        assert alert.text == 'You clicked a button'
        alert.accept()

    def test_timed_alerts(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.get_timed_alert()
        assert page.alert_appeared()

    def test_confirm_box_accept(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.get_confirm_box()
        alert.accept()
        confirm_result = page.get_confirm_result()
        assert 'Ok' in confirm_result

    def test_confirm_box_dismiss(self):
        page = PageAlerts(self.driver)
        page.open()
        alert = page.get_confirm_box()
        alert.dismiss()
        confirm_result = page.get_confirm_result()
        assert 'Cancel' in confirm_result

    def test_prompt_box(self):
        text = 'text to prompt box'
        page = PageAlerts(self.driver)
        page.open()
        alert = page.get_prompt_box()
        alert.send_keys(text)
        alert.accept()
        assert page.get_prompt_box_result()
        print(page.get_prompt_box_result())

