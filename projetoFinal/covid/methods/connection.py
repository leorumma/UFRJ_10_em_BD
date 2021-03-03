from sqlalchemy import create_engine

def get():
    connection_str = 'postgresql+psycopg2://viewer:readonly@34.66.66.28/postgres'
    return create_engine(connection_str)


def realdata():
    connection_str = 'postgresql+psycopg2://viewer:readonly@34.66.66.28/dadosreais'
    return create_engine(connection_str)