from ..models import Lotto
from .scraper import scrap_to_db

def update():
    lastupdate()  
    ids = [0]
    for record in Lotto.query.with_entities(Lotto.id).all(): # getting list of lottery IDs in DB
        ids.append(record[0])
    ids.sort()
    miss_ids = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
    miss_date = str(Lotto.query.get(miss_ids[-1]+1).date)
    scrap_to_db(f"https://www.lotto.pl/lotto/wyniki-i-wygrane/date,{miss_date[0:4]}-{miss_date[4:6]}-{miss_date[6:8]},300")
    for record in Lotto.query.with_entities(Lotto.id).all():
        ids.append(record[0])
    ids.sort()
    miss_ids = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
    if miss_ids.count() == 0:
        return "Database is up to date!"
    else:
        return f"Still {miss_ids.count()} records missing in database."
 
def lastupdate(): # getting last 10 records
    url = "https://www.lotto.pl/lotto/wyniki-i-wygrane"
    scrap_to_db(url)