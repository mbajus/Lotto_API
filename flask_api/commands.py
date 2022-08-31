import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Lotto
from .datascraper.htmltool import gethtml
from .datascraper.scraper import initialdb


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

@click.command(name='getpage')
@with_appcontext
def getpage():
    html = gethtml("https://www.lotto.pl/lotto/wyniki-i-wygrane/date,1957-08-29,10")
    return html

@click.command(name='dbrecords')
@with_appcontext
def dbrecords():
    result = initialdb()