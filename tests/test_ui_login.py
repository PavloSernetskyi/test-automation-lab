import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pytest fixture to set up and tear down the Chrome browser for each test
@pytest.fixture
def driver():
    # Set up headless Chrome for GitHub Actions
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 🧠 Required in CI (no display)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Start a new Chrome browser instance
    driver = webdriver.Chrome()
    # Navigate to the OrangeHRM demo login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # Provide the driver to the test
    yield driver
    # Quit the browser after the test completes
    driver.quit()

def test_login(driver):
    # Create a WebDriverWait object to wait up to 10 seconds for elements
    wait = WebDriverWait(driver, 10)

    # Wait until the username input field is present in the DOM
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    # Find the password input field by its name attribute
    password_input = driver.find_element(By.NAME, "password")
    # Find the login button by its tag name (button)
    login_button = driver.find_element(By.TAG_NAME, "button")

    # Enter the username "Admin"
    username_input.send_keys("Admin")
    # Enter the password "admin123"
    password_input.send_keys("admin123")
    # Click the login button to submit the form
    login_button.click()

    # Assert that the word "Dashboard" appears in the page source after login
    assert "Dashboard" in driver.page_source