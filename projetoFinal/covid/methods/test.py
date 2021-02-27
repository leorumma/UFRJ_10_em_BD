from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def test_query():
    query = """
    select table_type, count(table_name)
    from information_schema.tables
    group by table_type
    """

    df = pd.read_sql(query, con=con.get())

    return graphs.get_bar_chart(df, "table_type", "count")
