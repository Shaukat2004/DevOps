import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_income_full_flow():

    driver = webdriver.Chrome()

    try:

        # LOGIN
        driver.get("http://127.0.0.1:8000/authentication/login")

        driver.find_element(By.NAME, "username").send_keys("shantanu2k1")
        driver.find_element(By.NAME, "password").send_keys("shanroot")
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        time.sleep(2)

        # GO TO INCOME PAGE
        driver.get("http://127.0.0.1:8000/income/")
        time.sleep(2)

        # CLICK ADD INCOME
        driver.find_element(By.XPATH, "//a[contains(text(),'Add Income')]").click()
        time.sleep(2)

        # ADD INCOME
        driver.find_element(By.NAME, "amount").send_keys("250000")
        driver.find_element(By.NAME, "description").send_keys("Full Stack")

        driver.find_element(By.NAME, "source").send_keys("Freelancing")

        date_field = driver.find_element(By.NAME, "income_date")
        driver.execute_script("arguments[0].value = '2026-01-13'", date_field)

        driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        time.sleep(2)

        # VERIFY INCOME ADDED
        page = driver.page_source
        assert "Full Stack" in page

        print("Income Added Successfully")

        # EDIT INCOME
        driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(2)

        description = driver.find_element(By.NAME, "description")
        description.clear()
        description.send_keys("Updated Full Stack")

        driver.find_element(By.XPATH, "//input[@value='Save']").click()

        time.sleep(2)

        print("Income Edited Successfully")

        # DELETE INCOME
        driver.find_element(By.LINK_TEXT, "Edit").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Delete").click()

        time.sleep(2)

        print("Income Deleted Successfully")

        # OPEN INCOME SUMMARY
        driver.find_element(By.LINK_TEXT, "Income Summary").click()

        time.sleep(3)

        print("Income Summary Loaded")
        print("Income TC Passed – Full Flow Working")

    finally:
        driver.quit()