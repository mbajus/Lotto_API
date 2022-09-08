from ..extensions import db
from ..models import Lotto
from .scraper import scrap_to_db

def update():
    lastupdate()  
    count = None
    last = 0
    while last != count:
        count = last
        ids = [0]
        for record in db.execute('SELECT id FROM lotto'): # getting list of lottery IDs in DB
            ids.append(record[0])
        ids.sort()
        miss_ids = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
        miss_date = str(db.query(Lotto).get(miss_ids[-1]+1).date)
        scrap_to_db(f"https://www.lotto.pl/lotto/wyniki-i-wygrane/date,{miss_date[0:4]}-{miss_date[4:6]}-{miss_date[6:8]},300")
        for record in db.execute('SELECT id FROM lotto'):
            ids.append(record[0])
        ids.sort()
        miss_ids = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
        last = len(miss_ids)
    return len(miss_ids)
 
def lastupdate(): # getting last 10 records
    url = "https://www.lotto.pl/lotto/wyniki-i-wygrane"
    scrap_to_db(url)