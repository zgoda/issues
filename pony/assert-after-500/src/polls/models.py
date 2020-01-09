import os
from datetime import datetime

from pony import orm

db = orm.Database()


class Poll(db.Entity):
    name = orm.Required(str, 100)
    options = orm.Set('Option')


class Option(db.Entity):
    title = orm.Required(str, 100)
    poll = orm.Required(Poll)
    votes = orm.Set('Vote')


class Vote(db.Entity):
    option = orm.Required(Option)
    date_cast = orm.Required(datetime, default=datetime.utcnow)


db.bind(
    provider='sqlite', filename=os.environ.get('DB_FILENAME', ':memory:'),
    create_db=True,
)
db.generate_mapping(create_tables=True)
