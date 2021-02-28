from sqlalchemy import create_engine

def get():
    connection_str = 'postgresql+psycopg2://postgres:teste-faculdade@34.66.66.28/postgres'
    return create_engine(connection_str)
