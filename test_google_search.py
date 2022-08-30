from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope="session", autouse=True)
def window_size():
    browser.config.window_height = 500
    browser.config.window_width = 1000


def test_google_should_find_selene():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_python_tests_in_selenide_search():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selenide').press_enter()
    browser.element('[id="search"]').should_not(have.text('User-oriented Web UI browser tests in Python'))
