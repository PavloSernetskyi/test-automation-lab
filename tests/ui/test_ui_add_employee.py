import pytest
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield driver
    driver.quit()

def test_add_employee(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()

    # Navigate to PIM
    pim_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
    pim_button.click()

    # Click Add
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_button.click()

    # Fill out the form
    first_name = "TestUser"
    last_name = "Auto" + str(int(time.time()))  # make it unique

    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)

    # Submit the form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Assert we landed back on the employee detail form
    wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
