from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    WITH 
    o2_measurements as (
        SELECT formrecordid as o2id, avg(CAST(answer as INTEGER)) as o2ratio 
        FROM tb_questiongroupformrecord
        WHERE questionid=246
        GROUP BY o2id
        FETCH FIRST 70 ROW ONLY
    ),
    co2_measurements as (
        SELECT formrecordid as co2id, avg(CAST(answer as INTEGER)) as co2ratio 
        FROM tb_questiongroupformrecord
        WHERE questionid=247
        GROUP BY co2id
        FETCH FIRST 100 ROW ONLY
    ),
    ratios as (
        SELECT co2id,CASE WHEN o2id IS NOT NULL AND co2id IS NOT NULL THEN CAST(o2ratio/co2ratio*100 AS INTEGER) ELSE NULL END as ratio
        FROM co2_measurements
        FULL OUTER JOIN o2_measurements
        ON co2id = o2id
    )

    SELECT count(*) as "total de exames",CASE WHEN ratio/20 IS NOT NULL THEN ratio/20*20 || '-' || ratio/20*20+20-1 ELSE 'Indisponível' END as "razão"
    FROM ratios
    GROUP BY ratio/20;
    """


    df = pd.read_sql(query, con=con.realdata())

    return graphs.get_chart(df, "razão", "total de exames")
