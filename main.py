from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# Data untuk diinput
data_array = data_array = [
    "apel", "jeruk", "pisang", "mangga", "semangka", "nanas", "stroberi", "anggur",
    "kiwi", "melon", "lemon", "alpukat", "delima", "pepaya", "salak", "rambutan",
    "durian", "sirsak", "cempedak", "markisa", "blueberry", "cranberry", "pir",
    "ceri", "buah naga", "kelapa", "kedondong", "labu", "kismis", "jambu"
]


# Inisialisasi browser Edge
driver = webdriver.Edge()

# 1. Buka halaman login
driver.get("https://rewards.bing.com/")  # Ganti dengan URL login atau home yang mengarah ke login
print("Silakan login secara manual di browser yang muncul...")

# 2. Tunggu sampai login selesai (misalnya dengan menunggu elemen tertentu muncul)
while True:
    try:
        # Misalnya, kita tunggu elemen search box muncul
        driver.find_element(By.ID, "rewards-suggestedSearch-searchbox")
        print("Login terdeteksi. Melanjutkan program...")
        break
    except:
        time.sleep(1)

# 3. Jalankan automasi isi input dan Ctrl + W
for index, data in enumerate(data_array):
    if index > 0:
        # Buka tab baru
        driver.execute_script("window.open('https://rewards.bing.com/', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)

    try:
        # Cari input box
        input_box = driver.find_element(By.ID, "rewards-suggestedSearch-searchbox")

        # Isi dan submit
        input_box.clear()
        input_box.send_keys(data)
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # Ctrl + W untuk tutup tab
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()
        time.sleep(1)

        # Kembali ke tab sebelumnya (jika ada)
        if len(driver.window_handles) > 0:
            driver.switch_to.window(driver.window_handles[-1])

    except Exception as e:
        print(f"Error: {e}")
        break

# Tutup browser
driver.quit()
