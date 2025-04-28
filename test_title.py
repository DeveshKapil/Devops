from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (important for CI/CD)
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920,1080")  # Optional: Define screen size
chrome_options.add_argument("--user-data-dir=/tmp/temporary-user-data-dir")  # Fresh profile

# Setup Chrome driver service
service = Service("/usr/local/bin/chromedriver")  # Make sure this path is correct

# Initialize the WebDriver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Verify page title
    if driver.title == "Google":
        print("Verified")
    else:
        print("Unverified")

finally:
    # Always quit the driver (important for Jenkins jobs to free memory)
    driver.quit()
