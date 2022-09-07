from ..models import Lotto
from ..extensions import db
from .scraper import scrap_to_db
import time, os


def update():
    lastupdate()  
    ids = [0]
    for record in Lotto.query.with_entities(Lotto.id).all(): # getting list of lottery IDs in DB
        ids.append(record[0])
    ids.sort()
    miss_ids = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
    while miss_ids != []:
        miss_id = miss_ids[-1]
        miss_date = str(Lotto.query.get(miss_id+1).date) # the lastest closes date to the missing one
        scrap_to_db(f"https://www.lotto.pl/lotto/wyniki-i-wygrane/date,{miss_date[0:4]}-{miss_date[4:6]}-{miss_date[6:8]},250")
        miss_ids = miss_ids[0:max(miss_ids.index(miss_id)-248, 0)]
        print("LOOP")
    
def lastupdate(): # getting last 10 records
    url = "https://www.lotto.pl/lotto/wyniki-i-wygrane"
    scrap_to_db(url)


