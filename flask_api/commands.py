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

@click.command(name='updatedb')
@with_appcontext
def updatedb():
    html = gethtml("https://www.lotto.pl/lotto/wyniki-i-wygrane/date,1957-08-29,10")
    print(html)
    return html

@click.command(name='dbrecords')
@with_appcontext
def dbrecords():
    initialdb()

