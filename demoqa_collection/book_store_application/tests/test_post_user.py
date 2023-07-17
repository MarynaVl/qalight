from demoqa_collection.book_store_application.pages.page_book_store_users_api import PageBookStoreUsers


class TestUser:

    user_id = None

    def test_create_user(self):
        page = PageBookStoreUsers()
        user = page.create_user('Halyna', 'P@ssw0rd')
        self.user_id = user.get('id')

    def test_delete_user(self):
        page = PageBookStoreUsers()
        user_id = page.create_user('Halyna2', 'P@ssw0rd').get('id')
        page.delete_user(his_id=user_id)

