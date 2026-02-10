from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json



driver = webdriver.Edge()
url = 'http://www.scrapethissite.com/pages/ajax-javascript/'
driver.get(url)
driver.maximize_window()

years = ['2010','2011','2012', '2013', '2014', '2015']

for year in years:
    print(f"Обрабатывается {year} год...")
    
    try:
        link = driver.find_element(By.LINK_TEXT, year)
        link.click()
        
        wait = WebDriverWait(driver, 10)


        table = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".table tbody tr"))
        )
        
        movies = []
        for i in table:
            try:
                title = i.find_element(By.CSS_SELECTOR, "td.film-title").text
                nominations = i.find_element(By.CSS_SELECTOR, "td.film-nominations").text
                awards = i.find_element(By.CSS_SELECTOR, "td.film-awards").text
                
                movie_data = {
                    "year": year,
                    "title": title,
                    "nominations": nominations,  
                    "awards": awards               
                }
                
                movies.append(movie_data)
                
            except Exception as e:
                print(f"Ошибка при обработке строки таблицы: {e}")
                continue

        filename = f"oscar_movies_{year}.json"
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(movies, file, ensure_ascii=False, indent=2)
        
        print(f"Данные за {year} год сохранены в файл: {filename}")
        

        driver.get(url)
        
    except Exception as e:
        print(f"Ошибка при обработке {year} года: {e}")
        continue

driver.quit()
print("\nСбор данных завершен!")
print("Созданные файлы:")
