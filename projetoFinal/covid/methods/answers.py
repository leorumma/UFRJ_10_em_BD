from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    WITH answer_count AS (
    SELECT count(*), questionid as id
    FROM tb_questiongroupformrecord
    GROUP BY questionid)

    SELECT description, sum(count) as count
    FROM answer_count, tb_questions
    WHERE questionid = id
    GROUP BY description;
    """


    df = pd.read_sql(query, con=con.realdata())

    return graphs.get_chart(df, "description", "count")
