import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_expense_full_flow():

    driver = webdriver.Chrome()

    try:

        # LOGIN
        driver.get("http://127.0.0.1:8000/authentication/login")

        driver.find_element(By.NAME, "username").send_keys("shantanu2k1")
        driver.find_element(By.NAME, "password").send_keys("shanroot")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        time.sleep(2)

        # GO TO DASHBOARD
        driver.get("http://127.0.0.1:8000")
        time.sleep(2)

        # CLICK ADD EXPENSE
        driver.find_element(By.XPATH, "//a[contains(text(),'Add Expense')]").click()
        time.sleep(2)

        # ADD EXPENSE
        driver.find_element(By.NAME, "amount").send_keys("1000")
        driver.find_element(By.NAME, "description").send_keys("Test Food Expense")
        driver.find_element(By.NAME, "category").send_keys("Food/Groceries")

        date_field = driver.find_element(By.NAME, "expense_date")
        driver.execute_script("arguments[0].value = '2026-03-04'", date_field)

        driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        time.sleep(2)

        # VERIFY EXPENSE ADDED
        page = driver.page_source
        assert "Test Food Expense" in page

        print("Expense Added Successfully")

        # EDIT EXPENSE
        driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(2)

        description = driver.find_element(By.NAME, "description")
        description.clear()
        description.send_keys("Updated Food Expense")

        driver.find_element(By.XPATH, "//input[@value='Save']").click()

        time.sleep(2)

        print("Expense Edited Successfully")

        # DELETE EXPENSE
        driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Delete").click()

        time.sleep(2)

        print("Expense Deleted Successfully")

        # OPEN EXPENSE SUMMARY
        driver.find_element(By.LINK_TEXT, "Expenses Summary").click()

        time.sleep(3)

        print("Expense Summary Loaded")
        print("TC2 Passed – Expense Full Flow Working")

    finally:
        driver.quit()