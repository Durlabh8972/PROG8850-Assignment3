
# Assignment 3 - Web App with MySQL & Selenium Automation

## Overview
This project implements a Flask web app with a login form connected to a MySQL database and tested using Selenium.

## Prerequisites
- Python 3.x
- pip
- MySQL Server
- Google Chrome
- ChromeDriver

## Setup Instructions

### Step 1: MySQL Database
1. Login to MySQL:
```bash
mysql -u root -p
```
2. Run the script:
```sql
SOURCE db_setup.sql;
```

### Step 2: Install Python Dependencies
```bash
pip install flask mysql-connector-python selenium
```

### Step 3: Run Flask App
```bash
python app.py
```
Visit `http://127.0.0.1:5000/login` in your browser.

### Step 4: Run Selenium Script
Ensure Flask app is running, then:
```bash
python test_login.py
```

## Files
- `app.py` - Flask app
- `templates/login.html` - HTML form
- `db_setup.sql` - SQL to setup DB
- `test_login.py` - Selenium test
- `README.md` - Instructions

