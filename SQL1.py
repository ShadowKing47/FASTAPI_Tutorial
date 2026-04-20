# Demonstrates raw SQL execution and SQLAlchemy Core (Table/Column expressions)
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True)

connection = engine.connect()

# Create table only if it doesn't already exist
connection.execute(text("""
    CREATE TABLE IF NOT EXISTS users (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age  INTEGER
    )
"""))
connection.commit()

# Define the same table in SQLAlchemy Core so we can use expression-based queries
meta = MetaData()
people = Table(
    "users", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)
meta.create_all(engine)

# INSERT
stmt = people.insert().values(name="Alice", age=30)
connection.execute(stmt)
connection.commit()

# SELECT with a WHERE clause
stmt = people.select().where(people.c.age > 20)
result = connection.execute(stmt)
for row in result.fetchall():
    print(row)

# UPDATE
stmt = people.update().where(people.c.name == "Alice").values(age=31)
connection.execute(stmt)
connection.commit()

# DELETE
stmt = people.delete().where(people.c.name == "Alice")
connection.execute(stmt)
connection.commit()
