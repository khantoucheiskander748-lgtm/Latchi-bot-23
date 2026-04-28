from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://qxbroker.com/en/sign-in/")

print("🔵 Chrome opened.")
print("سجل الدخول لحساب Quotex يدويًا داخل المتصفح.")
input("بعد ما تدخل كامل وتوصل للمنصة اضغط Enter هنا...")

time.sleep(3)

cookies = driver.get_cookies()
print("ALL COOKIES =>")
for c in cookies:
    print(c)

found = False
for c in cookies:
    if c["name"].lower() == "ssid":
        print("\n✅ SSID =", c["value"])
        found = True

if not found:
    print("\n❌ SSID NOT FOUND")

input("Press Enter to close browser...")
driver.quit()