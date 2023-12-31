from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
times = []
for i in time:
    times.append(i.text)

event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
events = []
for i in event:
    events.append(i.text)

events.remove(events[0])

all = {}
for i, j in zip(times, events):
    all["2023-" + i] = j

print(all)

# closes a page
driver.close()

# driver.quit() - closes entire browser