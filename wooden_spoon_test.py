import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
commands to run on terminal:
pip install pytest
pip install selenium
venv\Scripts\activate
to see if the webdriver is  working fine (you see nothing if it works fine):  python -c "from selenium import webdriver" 
pip install --upgrade selenium
"""


# prompt on ChatGPT: write python program in pytest for finding wooden spoon on amazon
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You need to have chromedriver installed
    yield driver
    driver.quit()


def test_search_wooden_spoon(browser):
    browser.get("https://www.amazon.com")

    # Wait for the search bar to be present
    WebDriverWait(browser, 2).until(
        ec.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    # Locate the search bar and enter "wooden spoon"
    search_bar = browser.find_element("id", "twotabsearchtextbox")
    search_bar.send_keys("wooden spoon")
    search_bar.send_keys(Keys.RETURN)

    # You can add more assertions based on the search results page
    assert "Wooden Spoon" in browser.page_source
    # it seems python is very much readable
    

    # find the profile of user "Alip Mohammed" on googlescholar
    def test_search_user_profile(browser):
    browser.get("https://scholar.google.com/")

    # Wait for the search bar to be present
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "gs_hdr_tsi"))
    )

    # Locate the search bar and enter "Alip Mohammed"
    user_name = 'Alip Mohammed'
    search_bar = browser.find_element("id", "gs_hdr_tsi")
    search_bar.send_keys(user_name)
    search_bar.send_keys(Keys.RETURN)

    # You can add more assertions based on the search results page
    assert user_name in browser.page_source


