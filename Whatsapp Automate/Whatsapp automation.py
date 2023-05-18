# Import the necessary modules and classes from the Selenium package
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

# Set up the Chrome driver with the desired options and user data directory
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/abc/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome('C:/Users/abc/Desktop/selenium/chromedriver.exe', options=options)

# Open WhatsApp web
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 10)

# Wait for 20 seconds to allow time for scanning the QR code and loading the WhatsApp web interface
time.sleep(20)

try:
    # Specify the contact name you want to send messages to
    contact_name = "Enter Contact Name or number"

    # Find the search box element and enter the contact name
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)

    # Check if contact not found
    if driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div[1]/div/span'):
        print("Contact not found")
    else:
        # Specify the message you want to send
        message = "Hello, how are you?"

        # Loop through a range of 7 (sending 7 messages in this case)
        for x in range(7):
            message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
            message_box.click()
            message_box.clear()
            message_box.send_keys(message)  # Enter your message
            message_box.send_keys(Keys.RETURN)  # Press Enter to send the message
            time.sleep(0.2)

        # Wait for 5 seconds before closing the browser
        time.sleep(5)
except NoSuchElementException as se:
    print("Error: ", str(se))

# Close the browser
driver.quit()
