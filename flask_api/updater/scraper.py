from ast import Mult
import bs4 as bs
from sqlalchemy.orm import Session

from ..extensions import db
from ..models import Lotto, Eurojackpot, Multimulti, Ekstrapensja, Superszansa, Kaskada, Minilotto
from .htmltool import gethtml

def insert_db(record): # 
    if db.execute('SELECT id FROM %s WHERE id = %d' %(record.__tablename__, record.id)).fetchall() == []:   
        with Session(db) as session:
            session.add(record)
            session.commit()

def scrap_to_db(url):
    print(f"Scraping url: {url}")
    page = gethtml(url)
    page = bs.BeautifulSoup(page, "html.parser")
    for code in page.find_all("div", class_="game-main-box skip-contrast"):
        db_models = {
            "Lotto": Lotto(),
            "Eurojackpot": Eurojackpot(),
            "Multi Multi": Multimulti(),
            "Ekstra Pensja": Ekstrapensja(), 
            "Mini Lotto": Minilotto(),
            "Kaskada": Kaskada(),
        } # while exec() doesnt work on heroku
        date = code.find("p", class_="sg__desc-title").get_text().strip()
        time = date[-5:].replace(":","") if ":" in date else None
        date = "".join(date.split(",")[1].strip().split(".")[::-1])   
        for row in code.find_all("div", class_="result-item"):
            name = row.find("p", class_="result-item__name").get_text().strip()          
            if name in ["Lotto", "Eurojackpot", "Multi Multi", "Ekstra Pensja", "Mini Lotto", "Kaskada"]:
                # print('record = %s()' % name.replace(' ', '').lower().capitalize()) # doesnt work on heroku ??!
                # exec('record = %s()' % name.replace(' ', '').lower().capitalize())
                record = db_models[name]
                record.date = date
                record.time = time
                record.id = row.find("p", class_="result-item__number").get_text().strip()
                nums1 = []
                for i in row.find_all("div", class_="scoreline-item"):
                    nums1.append(i.get_text().strip())
                record.nums1 = ",".join(nums1)
            elif name in ["Lotto Plus", "Plus", "Ekstra Premia"]:
                nums2 = []
                for i in row.find_all("div", class_="scoreline-item"):
                    nums2.append(i.get_text().strip())
                record.nums2 = ",".join(nums2)
            elif name == "Super Szansa":
                ss_id = row.find("p", class_="result-item__number").get_text().strip()
                record.ss_id = ss_id
                for i in row.find_all("div", class_="scoreline-item"):
                    nums_ss.append(i.get_text().strip())
                nums_ss = ",".join(nums_ss)
                insert_db(Superszansa(id=ss_id, nums1=nums_ss, date=date, time=time))
            else:
                print(f'{name} game didnt match the db tables.')
        insert_db(record)
        record = None