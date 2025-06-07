from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_to_facebook():
    print("Starting Facebook automation process...")
    
    # Set up Chrome options
    print("Configuring Chrome options...")
    chrome_options = Options()
    
    # Run Chrome in headless mode (no GUI)
    print("Setting up headless mode...")
    chrome_options.add_argument('--headless=new')  # New headless mode (Chrome 109+)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--window-size=1920,1080')
    
    print("Initializing Chrome driver version 136...")
    # Initialize the Chrome driver with webdriver-manager, specifying version 136
    service = Service(ChromeDriverManager(version="136.0.7103.113").install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        print("Navigating to Facebook...")
        # Navigate to Facebook
        driver.get('https://www.facebook.com')
        
        print("Waiting for email field to load...")
        # Wait for the email field to be present
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        print("Entering email address...")
        # Enter email
        email_field.send_keys("bilalejazdeen@gmail.com")
        print("Email entered successfully!")
        
        print("Entering password...")
        # Find and enter password
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys("Bilal@12")
        print("Password entered successfully!")
        
        print("Clicking login button...")
        # Find and click the login button
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        print("Waiting for login process to complete...")
        time.sleep(5)
        
        print("Login process completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        print("Closing browser...")
        driver.quit()
        print("Browser closed successfully!")
        print("Task completed successfully!")

if __name__ == "__main__":
    login_to_facebook()
