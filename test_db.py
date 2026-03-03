from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Vikram2001@localhost:5432/questionnaire_db")

conn = engine.connect()
print("Database Connected Successfully!")
conn.close()