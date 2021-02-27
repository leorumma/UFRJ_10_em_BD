from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query():
    query = """
    WITH 
    outcomes AS (
        SELECT values.listofvaluesid as id, values.description
        FROM tb_listtype AS list, 
            tb_listofvalues AS values 
        WHERE list.description = 'Outcome list'and list.listtypeid = values.listtypeid
    ),
    counts AS (
        SELECT COUNT(*),listofvaluesid 
        FROM tb_questiongroupformrecord 
        WHERE listofvaluesid IN (SELECT id FROM outcomes)
        GROUP BY listofvaluesid
    )

    SELECT count,description from counts,outcomes 
    WHERE id = listofvaluesid;
    """


    df = pd.read_sql(query, con=con.get())

    return graphs.get_chart(df, "description", "count")
