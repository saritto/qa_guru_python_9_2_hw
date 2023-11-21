import pytest

@pytest.fixture
def browser():
    print("Я выполняюсь перед тестами.")

    yield
    print("Я выполняюсь после теста.")

@pytest.fixture
def login_page(browser):
    pass

@pytest.fixture
def credentials():
    return "admin", "1234"

def test_login(login_page, credentials):
    assert credentials == ("admin", "1234"), "Неверный логин или пароль"
