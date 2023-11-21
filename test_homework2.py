from selene.support.shared import browser
from selene import be, have

def test_google_has_no_answer():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('tdxqyg2d27w3fruevhesrht3t3oht5495i9g4').press_enter()
    browser.element('p[role=heading]').should(have.text('По запросу tdxqyg2d27w3fruevhesrht3t3oht5495i9g4 ничего не найдено.'))

def test_google_has_answer():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

