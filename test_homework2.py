from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_configs():
    browser.config.window_width = 500
    browser.config.window_height = 1920
    yield
    browser.quit()


@pytest.fixture
def browser_configs_wider():
    browser.config.window_width = 2000
    browser.config.window_height = 1500
    yield
    browser.quit()


def test_google_has_no_answer(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('tdxqyg2d27w3fruevhesrht3t3oht5').press_enter()
    browser.element('p[role=heading]').should(have.text('По запросу tdxqyg2d27w3fruevhesrht3t3oht5 ничего не найдено.'))


def test_google_has_answer(browser_configs_wider):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
