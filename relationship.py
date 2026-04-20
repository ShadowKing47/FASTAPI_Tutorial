# Demonstrates a SQLAlchemy Core join between two related tables.
from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, Float, ForeignKey,
)

engine = create_engine("sqlite:///./test.db", echo=True)
meta = MetaData()

people = Table(
    "people", meta,
    Column("id",   Integer, primary_key=True),
    Column("name", String,  nullable=False),
)

things = Table(
    "things", meta,
    Column("id",          Integer, primary_key=True),
    Column("name",        String,  nullable=False),
    Column("description", String,  nullable=True),
    Column("price",       Float,   nullable=False),
    # Foreign key links each thing back to its owner in the people table
    Column("owner",       Integer, ForeignKey("people.id")),
)

meta.create_all(engine)

# Join people and things on the owner FK, then fetch each person's name + item name
join_stmt = people.join(things, people.c.id == things.c.owner)
result_stmt = (
    people.select()
    .select_from(join_stmt)
    .add_columns(things.c.name.label("item"))
)

with engine.connect() as connection:
    results = connection.execute(result_stmt)
    for row in results.fetchall():
        print(row)
