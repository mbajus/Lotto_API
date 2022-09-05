from ..models import Lotto
import time, os

def check_db():
    os.environ['TZ'] = 'Europe/Warsaw'
    date = time.strftime('%Y%m%d')
    records = Lotto.query.with_entities(Lotto.id, Lotto.date)
    print(records)
    



