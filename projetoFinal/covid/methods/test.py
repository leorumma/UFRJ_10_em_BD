from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def test_query():
    query = """
    select table_type, (count(table_name)::decimal / max(t.total)) as percent
    from information_schema.tables
    cross join (
        select total from (
            select 'anchor' as anchor, count(table_name) as total
            from information_schema.tables
            group by anchor
        ) as t1
    ) as t
    group by table_type;
    """

    df = pd.read_sql(query, con=con.get())

    return graphs.get_chart(df, "table_type", "percent")
