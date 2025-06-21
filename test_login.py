
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import mysql.connector

# Config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dkt@123',
    'database': 'prog8850db'
}

# Test data
username = "testuser"
password = "testpass"

# Start Chrome WebDriver
service = Service()
driver = webdriver.Chrome(service=service)
driver.get("http://127.0.0.1:5000/login")

# Fill form
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Wait for DB insertion
time.sleep(3)

# Verify in DB
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
        print("Test Passed: User inserted into DB.")
    else:
        print("Test Failed: User not found in DB.")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

driver.quit()
