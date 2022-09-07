from ..models import Lotto
from ..extensions import db
from .scraper import scrap_to_db
import time, os


def update():
    lastupdate()  
    ids = []
    for record in Lotto.query.with_entities(Lotto.id).all(): # getting list of lottery IDs in DB
        ids.append(record[0])
    print(ids)
    ids.sort(reverse=True)
    print(ids)
    
    
def lastupdate():
    url = "https://www.lotto.pl/lotto/wyniki-i-wygrane"
    scrap_to_db(url)


