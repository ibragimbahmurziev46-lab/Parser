import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
driver = webdriver.Firefox()
url = 'https://books.toscrape.com/index.html'

driver.get(url)
driver.maximize_window()


books = []
for page in range(1,6):
    articles = driver.find_elements(By.CSS_SELECTOR,"article.product_pod")
    for article in articles:
        title = article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = article.find_element(By.CSS_SELECTOR, ".price_color").text
        stock = article.find_element(By.CSS_SELECTOR, ".availability").text
        books.append(
            {
                "title":title,
                "price":price,
                "stock":stock
            }
        )

    button = driver.find_element(By.CSS_SELECTOR, 'li.next a').click()

print(books)

with open("books.json","w", encoding="UTF-8") as file:
    json.dump(books,file,ensure_ascii=False, indent=2)

print("Сохранение данных о книгах завершено!")

button = driver.find_element(By.CSS_SELECTOR, 'li.previous a').click()
button = driver.find_element(By.CSS_SELECTOR, 'li.previous a').click()
button = driver.find_element(By.CSS_SELECTOR, 'li.previous a').click()
button = driver.find_element(By.XPATH, '//*[@id="default"]/div[1]/div/div/div/section/div[2]/ol/li[15]/article/div[1]/a').click()

driver.save_screenshot(f"Thrist.png")

print("Скриншот сдлеан")


