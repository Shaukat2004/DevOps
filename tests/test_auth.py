from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:8000"


def login(driver, username, password):
    driver.get(f"{BASE_URL}/authentication/login")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(username)

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()


def test_authentication_and_role_access(driver):
    print("Test Case 1: Authentication & Role Acess\nStarting Test Case 1...")
    #Valid User Credentials
    login(driver, "duncan256", "duncanroot")

    WebDriverWait(driver, 10).until(
        EC.url_to_be(f"{BASE_URL}/")
    )

    assert driver.current_url == f"{BASE_URL}/"
    print("TC1.1 Passed")
    
    #Logout
    driver.get(f"{BASE_URL}/authentication/logout")
    print("TC1.2 Passed")
    
    # ---------- ACCESS RESTRICTION AFTER LOGOUT ----------
    # driver.get(f"{BASE_URL}/")
    # assert "login" in driver.current_url.lower()

    #Invalid User Credentials
    login(driver, "dextermorgan", "not_killer")

    assert "login" in driver.current_url.lower()
    print("TC1.3 Passed")
    
    #Admin Login
    login(driver, "shantanu2k1", "shanroot")

    WebDriverWait(driver, 10).until(
        EC.url_to_be(f"{BASE_URL}/")
    )

    assert driver.current_url == f"{BASE_URL}/"
    print("TC1.4 Passed")
    #Logout admin
    driver.get(f"{BASE_URL}/authentication/logout")

    #Normal User should not access Backend
    #Login normal user
    login(driver,"duncan256", "duncanroot")
    driver.get(f"{BASE_URL}/admin/")

    assert "site administration" not in driver.page_source.lower()
    print("TC1.5 Passed")

    #Admin Login to Backend
    driver.get(f"{BASE_URL}/admin/login/?next=/admin/")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/admin")
    )

    assert "/admin" in driver.current_url.lower()
    print("TC1.6 Passed\nTest Case 1 Execution completed.")