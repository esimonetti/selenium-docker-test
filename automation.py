from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# connecting to a playground
driver.get("http://uitestingplayground.com/textinput")

el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME, "body"))

# finding the text box
box = driver.find_element(By.XPATH, "//input[@id='newButtonName']")

# is the text box visible?
print("Element visible: " + str(box.is_displayed()))

# finding the button to click on
button = driver.find_element(By.XPATH, "//button[@id='updatingButton']")

# showing the button text
print("Button text before: " + button.text)

# changing value of the text box
box.send_keys("Automation Demo")

# clicking on the button, changes the button label to the textbox value
button.click()

# checking the new button label
print("Button text after: " + button.text)

driver.close()
