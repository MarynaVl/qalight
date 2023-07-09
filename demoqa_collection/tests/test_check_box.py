import pytest
from demoqa_collection.pages.page_check_box import PageCheckBox


@pytest.mark.usefixtures('chrome')
class TestCheckBox:

    def test_expand_folder(self):
        page = PageCheckBox(self.driver)
        page.open()
        page.expand('Home')
        page.expand('Documents')
        page.expand('WorkSpace')
        page.check('Angular')
        page.check('React')
        results = page.get_results()

    def test_mass_expand(self):
        page = PageCheckBox(self.driver)
        page.open()
        folders = page.list_of_folders
        the_last_folder = ''
        for folder in folders:
            page.expand(folder)
            the_last_folder = folder
        assert page.is_folder_expanded(the_last_folder)
