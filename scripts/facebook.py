from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_to_facebook():
    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Uncomment this line if you want to run in headless mode
    
    # Initialize the Chrome driver with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Navigate to Facebook
        driver.get('https://www.facebook.com')
        
        # Wait for the email field to be present
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        # Enter email
        email_field.send_keys("bilalejazdeen@gmail.com")
        
        # Find and enter password
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys("Bilal@12")
        
        # Find and click the login button
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        # Wait for a few seconds to see the result
        time.sleep(5)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Keep the browser open for a while
        time.sleep(10)
        # Uncomment the next line if you want the browser to close automatically
        # driver.quit()

if __name__ == "__main__":
    login_to_facebook()
