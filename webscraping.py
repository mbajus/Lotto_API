from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sqlite3
import bs4 as bs

# conn = sqlite3.connect('lottodb.sqlite')
# cur = conn.cursor()

ser = Service("./chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ser, options=op)
driver.get("https://www.lotto.pl/wyniki")
soup = bs.BeautifulSoup(driver.page_source, "html.parser")
with open("xd.html", "w", encoding="utf-8") as f:
    f.write(str(soup.prettify()))
driver.close()

for code in soup.find_all("div", class_="game-main-box skip-contrast"):
    date = code.find("p", class_="sg__desc-title").get_text().strip()

    for row in code.find_all("div", class_="result-item"):
        name = row.find("p", class_="result-item__name").get_text().strip()
        nr = row.find("p", class_="result-item__number").get_text().strip()
        nums = []
        for i in row.find_all("div", class_="scoreline-item"):
            nums.append(i.get_text().strip())
        print(f"{name}, number {nr}, with results {nums}. On date {date}")




# cur.execute("CREATE TABLE IF NOT EXISTS lotto (id INTEGER PRIMARY KEY, nums TEXT NOT NULL, numsplus TEXT, date TEXT NOT NULL, time TEXT, super_id INTEGER) WITHOUT ROWID")




# with open("page.txt", "r") as f:
#     page = f.read()