import pytest
import logging


class TestFixtures:

    def test_in_class_1(self, my_first_fixture_placed_in_package):
        print('test_in_class_1 does something')

    def test_in_class_2(self, my_first_fixture_placed_in_package):
        print('test_in_class_2 does something')

    def test_in_class_3(self, class_fixture):
        print('test_in_class_3 does something')

    def test_in_class_4(self, class_fixture):
        print('test_in_class_4 does something')

    def test_in_class_5(self, fixture_with_yield_text):
        assert 'my' in fixture_with_yield_text

    def test_in_class_6(self, class_fixture):
        logging.error('test_in_class_6 does something')
        print('test_in_class_6 does something')

