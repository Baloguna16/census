import random
from datetime import datetime

from flask_script import Manager #docs: https://flask-script.readthedocs.io/en/latest/

from __init__ import create_app
import tools.parser as parser

app = create_app()
manager = Manager(app)

@manager.option('-d', '--dimension', default='year')
@manager.option('-f', '--file', default=None)
def parse(dimension, file):
    if dimension == 'year':
        if file == None:
            parser.by_year()
        else:
            parser.by_year(file)
    elif dimension == 'win':
        if file == None:
            parser.by_win()
        else:
            parser.by_win(file)
    elif dimension == 'seats':
        if file == None:
            parser.by_seats()
        else:
            parser.by_seats(file)
    elif dimension == 'votes':
        if file == None:
            parser.by_votes()
        else:
            parser.by_votes(file)
    print('All done.')



if __name__ == "__main__":
    manager.run()
