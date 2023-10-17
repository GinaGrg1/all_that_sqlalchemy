from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column, Integer, String, create_engine

engine = create_engine('postgresql+psycopg2://postgres:regina@localhost:5432/postgres',
        echo=False)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("fullname", String),
    Column("name", String(30)),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False)
)

print(user_table.c.keys()) # ['id', 'fullname', 'name']
print(user_table.c.name)   # user_account.name

metadata_obj.create_all(engine)
