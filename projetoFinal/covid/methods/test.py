from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def test_query(**kwargs):
    # query = """
    # select table_type, (count(table_name)::decimal / max(t.total)) as percent
    # from information_schema.tables
    # cross join (
    #     select total from (
    #         select 'anchor' as anchor, count(table_name) as total
    #         from information_schema.tables
    #         group by anchor
    #     ) as t1
    # ) as t
    # group by table_type;
    # """

    # df = pd.read_sql(query, con=con.get())

    # exemplo grouped bar chart

    df = pd.DataFrame([['giraffes', 20, 12],
                       ['orangutang', 14, 18],
                       ['monkeys', 23, 29]],
                      columns=['labels', 'trace1', 'trace2'])

    return graphs.get_grouped_bar_chart(df, 'labels', 'trace1', 'trace2',
                                        'SF Zoo', 'LA Zoo')
