import bs4 as bs
from ..extensions import db
from ..models import Lotto, Superszansa
from .htmltool import gethtml

def scrap_to_db(url):
    print(f"Scraping url: {url}")
    page = gethtml(url)
    page = bs.BeautifulSoup(page, "html.parser")
    for code in page.find_all("div", class_="game-main-box skip-contrast"):
        del date, time, nums1, nums2, name, id, nums_ss
        ss_id = None
        date = code.find("p", class_="sg__desc-title").get_text().strip()
        time = date[-5:].replace(":","") if ":" in date else None
        date = "".join(date.split(",")[1].strip().split(".")[::-1])   
        nums1 = []
        nums2 = []
        for row in code.find_all("div", class_="result-item"):
            name = row.find("p", class_="result-item__name").get_text().strip()           
            if name in ["Lotto", "Eurojackpot", "Multi Multi", "Ekstra Pensja", "Mini Lotto", "Kaskada"]:
                game = name.lower().replace(' ', '')
                id = row.find("p", class_="result-item__number").get_text().strip()
                for i in row.find_all("div", class_="scoreline-item"):
                    nums1.append(i.get_text().strip())
                nums1 = ",".join(nums1)
            elif name in ["Lotto Plus", "Plus", "Ekstra Premia"]:
                for i in row.find_all("div", class_="scoreline-item"):
                    nums2.append(i.get_text().strip())
                nums2 = ",".join(nums2)
            elif name == "Super Szansa":
                ss_id = row.find("p", class_="result-item__number").get_text().strip()
                for i in row.find_all("div", class_="scoreline-item"):
                    nums_ss.append(i.get_text().strip())
                nums_ss = ",".join(nums_ss)
                sql_query = (
                    f"IF NOT EXISTS(SELECT id FROM superszansa WHERE id = {ss_id}"
                    f"BEGIN"
                    f"INSERT INTO superszansza (id, nums1, date, time) VALUES ({ss_id}, '{nums_ss}', {date}, {time})"
                    f"END"
                )
                db.execute(sql_query)
            if game in ['lotto', 'multimulti', 'ekstrapensja']:         
                sql_query = (
                    f"IF NOT EXISTS(SELECT id FROM {game} WHERE id = {id}"
                    f"BEGIN"
                    f"INSERT INTO {game} (id, nums1, nums2, date, time, ss_id) VALUES ({id}, '{nums1}', '{nums2}', {date}, {time}, {ss_id})"
                    f"END"
                )
                db.execute(sql_query)
            elif game in ['eurojackpot', 'minilotto', 'kaskada']:         
                sql_query = (
                    f"IF NOT EXISTS(SELECT id FROM {game} WHERE id = {id}"
                    f"BEGIN"
                    f"INSERT INTO {game} (id, nums1, date, time, ss_id) VALUES ({id}, '{nums1}', {date}, {time}, {ss_id})"
                    f"END"
                )
                db.execute(sql_query)
            else:
                print(f'The game {game} not in DB.')
