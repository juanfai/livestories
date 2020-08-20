import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


this_dir = os.path.dirname(os.path.realpath(__file__))
time_lapse = 20


def file_path(file_name):
    """Builds the file path."""
    return f'{this_dir}/../resources/{file_name}'


def load_json(file_name):
    """Loads test data from a json file."""
    with open(file_path(file_name), 'r') as json_file:
        return json.loads(json_file.read())


def wait_visible(driver, locator, seconds=None):
    """Waits for an element locator to be visible in the UI."""
    if seconds is None:
        seconds = time_lapse
    WebDriverWait(driver, seconds).until(
            EC.visibility_of_element_located(locator)
    )


def wait_invisible(driver, locator, seconds=None):
    """Waits for an element locator to be invisible in the UI."""
    if seconds is None:
        seconds = time_lapse
    WebDriverWait(driver, seconds).until(
            EC.invisibility_of_element_located(locator)
    )


def wait_presence(driver, locator, seconds=None):
    """Waits for an element locator to be present in the DOM."""
    if seconds is None:
        seconds = time_lapse
    WebDriverWait(driver, seconds).until(
            EC.presence_of_element_located(locator)
    )
