import pytest


@pytest.fixture(scope='function')
def my_first_fixture_placed_in_package():
    print('Setup before each test')
    yield
    print("TearDown after each test")


@pytest.fixture(scope='class')
def class_fixture():
    print('\nSetup before class')
    yield
    print("\nTearDown after class")


@pytest.fixture(scope='class')
def class_fixture():
    print('\nSetup before class')
    yield
    print("\nTearDown after class")


