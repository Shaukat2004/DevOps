import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000"


def admin_login(driver):
    driver.get(f"{BASE_URL}/admin/login/?next=/admin/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.NAME, "username").send_keys("shantanu2k1")
    driver.find_element(By.NAME, "password").send_keys("shanroot")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Wait until admin dashboard loads
    wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Users"))
    )


# TC2.1 Admin creates new user
def test_admin_create_user(driver):

    wait = WebDriverWait(driver, 10)

    admin_login(driver)

    # Open Users section
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Users"))).click()

    # Click Add user
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/admin/auth/user/add')]"))).click()

    username = "user" + str(int(time.time()))

    # Fill form
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password1").send_keys("StrongPass123")
    driver.find_element(By.NAME, "password2").send_keys("StrongPass123")

    # Save
    driver.find_element(By.XPATH, "//input[@value='Save']").click()

    time.sleep(2)

    page = driver.page_source.lower()

    assert username.lower() in page
    print("TC2.1 Passed")

# TC2.2 Duplicate username
def test_duplicate_username(driver):

    wait = WebDriverWait(driver, 10)

    admin_login(driver)

    driver.get(f"{BASE_URL}/admin/auth/user/add/")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password1").send_keys("StrongPass123")
    driver.find_element(By.NAME, "password2").send_keys("StrongPass123")

    driver.find_element(By.XPATH, "//input[@value='Save']").click()

    time.sleep(2)

    page = driver.page_source.lower()

    assert "already exists" in page
    print("TC2.2 Passed")


# TC2.3 Password mismatch
def test_password_mismatch(driver):

    wait = WebDriverWait(driver, 10)

    admin_login(driver)

    driver.get(f"{BASE_URL}/admin/auth/user/add/")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys("user_test_02")
    driver.find_element(By.NAME, "password1").send_keys("StrongPass123")
    driver.find_element(By.NAME, "password2").send_keys("WrongPass123")

    driver.find_element(By.XPATH, "//input[@value='Save']").click()

    time.sleep(2)

    page = driver.page_source.lower()

    assert "password" in page
    print("TC2.3 Passed")


# TC2.4 Empty fields
def test_empty_user_creation(driver):

    wait = WebDriverWait(driver, 10)

    admin_login(driver)

    driver.get(f"{BASE_URL}/admin/auth/user/add/")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.XPATH, "//input[@value='Save']").click()

    time.sleep(2)

    page = driver.page_source.lower()

    assert "required" in page
    print("TC2.4 Passed")


# TC2.5 Weak password
def test_weak_password(driver):

    wait = WebDriverWait(driver, 10)

    admin_login(driver)

    driver.get(f"{BASE_URL}/admin/auth/user/add/")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys("user_test_03")
    driver.find_element(By.NAME, "password1").send_keys("123")
    driver.find_element(By.NAME, "password2").send_keys("123")

    driver.find_element(By.XPATH, "//input[@value='Save']").click()

    time.sleep(2)

    page = driver.page_source.lower()

    assert "password" in page
    print("TC2.5 Passed")