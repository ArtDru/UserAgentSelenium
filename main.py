from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
#
# user_agents_list = [
#     "hellowotld",
#     "zdarovazaebval",
#     "pythonruli"
# ]
useragent = UserAgent()

options = webdriver.ChromeOptions()

# options.add_argument("--proxy-server=217.77.225.170:8080")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.opera}")

driver = webdriver.Chrome(options=options)
try:
    driver.get("https://2ip.ru/")
    time.sleep(4)

finally:
    driver.quit()