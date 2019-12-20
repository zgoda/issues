import os

from pony import orm

db = orm.Database()


class ToDo(db.Entity):
    title = orm.Required(str, 120, unique=True)
    done = orm.Required(bool, default=False)


db.bind(
    provider='sqlite', filename=os.environ.get('DB_FILENAME', ':memory:'),
    create_db=True,
)
db.generate_mapping(create_tables=True)
