from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query():
    query = """
    WITH ages_table AS (SELECT CAST(answer as INTEGER) as age FROM tb_questiongroupformrecord where questionid=144)

    SELECT count(*) FROM ages_table WHERE age < 40
    UNION SELECT count(*) FROM ages_table WHERE age >= 40 and age < 60
    UNION SELECT count(*) FROM ages_table WHERE age >= 60;
    """


    df = pd.read_sql(query, con=con.get())

    groups = [">40", "entre 40 e 60", ">60"]
    df["group"] = groups
    print(df)

    return graphs.get_chart(df, "group", "count")
