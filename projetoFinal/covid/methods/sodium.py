from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    WITH 
    sodium_measurements as (
    SELECT CAST(answer as INTEGER) as mmol 
    FROM tb_questiongroupformrecord
    WHERE questionid=170
    )

    SELECT mmol/5*5 || '-' || mmol/5*5+5-1 as "mmol/L", count(*)
    FROM sodium_measurements
    GROUP BY mmol/5
    ORDER BY mmol/5;
    """


    df = pd.read_sql(query, con=con.realdata())

    return graphs.get_chart(df, "mmol/L", "count")
