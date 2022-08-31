import bs4 as bs
from flask_api.extensions import db
from flask_api.models import Lotto
import webdriver

def initialdb():
    page = webdriver.gethtml("https://www.lotto.pl/lotto/wyniki-i-wygrane/date,1957-08-29,10")
    page = bs.BeautifulSoup(page, "html.parser")


    for code in page.find_all("div", class_="game-main-box skip-contrast"):
        record = Lotto()
        date = code.find("p", class_="sg__desc-title").get_text().strip()
        if ":" in date:
            record.time = date[-5:].replace(":","")
        else:
            record.time = "" # older records from lotto.pl page doesn't have time assignment
        record.date = "".join(date.split(",")[1].strip().split(".")[::-1])   

        for row in code.find_all("div", class_="result-item"):
            name = row.find("p", class_="result-item__name").get_text().strip()
            id = row.find("p", class_="result-item__number").get_text().strip()
            nums = []
            for i in row.find_all("div", class_="scoreline-item"):
                nums.append(i.get_text().strip())
            nums = ",".join(nums)
            if name == "Lotto":
                record.nums = nums
                record.id = id
            elif name == "Lotto Plus":
                record.numsp = nums
            # elif name = "Super Szansa":
            #     record.ssid = id
        db.session.add(record)
        db.session.commit()
    return page.get_text()




