def test_open_homepage(driver):
    driver.get("http://127.0.0.1:8000")
    assert "Budget Tracker" in driver.title