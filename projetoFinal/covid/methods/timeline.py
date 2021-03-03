from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    SELECT count(*), to_char(date_trunc('month', dtregistroform), 'YYYY-MM') AS month
    FROM tb_formrecord
    GROUP BY month
    ORDER BY month;
    """


    df = pd.read_sql(query, con=con.realdata())

    return graphs.get_single_line_chart(df, "month", "count")
