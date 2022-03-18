from sqlalchemy import create_engine
from Models.models import Base, Session
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert


# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = "postgresql+psycopg2://postgres:Python123@pg13:5432/postgres"
# DATABASE_URI = "postgresql+psycopg2://postgres:Python123@localhost:5432/postgres"

engine = create_engine(DATABASE_URI, echo=False)
session = Session(bind=engine)
meta = sqlalchemy.MetaData()
meta.bind = engine
meta.reflect(views=True)

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

def upsert(table, conn, keys, data_iter):
    # upsert_args = {"constraint": "hist_data_1_min_date_contract_uc"}
    for data in data_iter:
        data = {k: data[i] for i, k in enumerate(keys)}
        insert_stmt = insert(meta.tables[table.name]).values(**data)
        upsert_stmt = insert_stmt.on_conflict_do_nothing()
        conn.execute(upsert_stmt)
        
if __name__=="__main__":
    create_db()