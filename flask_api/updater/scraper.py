import bs4 as bs
from ..extensions import db
from ..models import Lotto
from .htmltool import gethtml

def scrap_to_db(url):
    print(f"Scraping url: {url}")
    page = gethtml(url)
    page = bs.BeautifulSoup(page, "html.parser")
    ids = []
    for record in db.execute('SELECT id FROM lotto'): # getting list of lottery IDs in DB
        ids.append(record[0])
    for code in page.find_all("div", class_="game-main-box skip-contrast"):
        record = Lotto()
        date = code.find("p", class_="sg__desc-title").get_text().strip()
        if ":" in date:
            record.time = date[-5:].replace(":","")
        record.date = "".join(date.split(",")[1].strip().split(".")[::-1])   
        for row in code.find_all("div", class_="result-item"):
            name = row.find("p", class_="result-item__name").get_text().strip()
            id = row.find("p", class_="result-item__number").get_text().strip()
            nums = []
            for i in row.find_all("div", class_="scoreline-item"):
                nums.append(i.get_text().strip())
            nums = ",".join(nums)
            if name == "Lotto":
                record.nums1 = nums
                record.id = id
            elif name == "Lotto Plus":
                record.nums2 = nums
            elif name = "Super Szansa":
                record.ss_id = id
        if int(record.id) in ids:
            del record
        else:
            db.add(record)
            db.commit()  