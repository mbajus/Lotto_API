from ..models import Lotto
from ..extensions import db
import time, os

def update():
    os.environ['TZ'] = 'Europe/Warsaw'
    date = time.strftime('%Y%m%d')
    records = Lotto.query.with_entities(Lotto.id, Lotto.date)
    print(records)
    
def lastupdate():
    pass


