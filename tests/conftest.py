import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .page_objects.helper import load_json


def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='forward-staging',
        help='Environment to hit (dev/qa/forward-staging). Defaults to "forward-staging".'
    )


@pytest.fixture(scope='class')
def env(request):
    return request.config.getoption('--env')


@pytest.fixture(scope='class')
def base_url(env):
    return f'https://{env}.livestories.com/'


@pytest.fixture(scope='class')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--ignore-certificate-errors')
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


@pytest.fixture(scope='class', autouse=True)
def setup_teardown(driver, base_url):
    driver.get(base_url)
    yield
    driver.close()


@pytest.fixture(scope='class')
def get_token(base_url):
    credentials = load_json('credentials.json')
    url = f'{base_url}/api/users/login'
    payload = {
        'email': credentials['user_name'],
        'password': credentials['password']
    }
    r = requests.post(url, json=payload)
    return f'Bearer {r.json()["token"]}'


@pytest.fixture(scope='class')
def session(get_token):
    header = {
        'authorization': get_token
    }
    s = requests.Session()
    s.headers.update(header)
    return s
