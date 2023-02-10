import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='available environments: es, ru, en')


@pytest.fixture
def browser(request):
    ch_language = request.config.getoption("language")
    opts = Options()
    opts.add_experimental_option('prefs', {'intl.accept_languages': ch_language})
    browser = webdriver.Chrome(options=opts)
    yield browser
    browser.quit()
