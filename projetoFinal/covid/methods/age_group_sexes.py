from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    WITH ages_table AS (
        SELECT formrecordid as id, CAST(answer as INTEGER) as age 
        FROM tb_questiongroupformrecord
        WHERE questionid= (SELECT questionid FROM tb_questions WHERE description='Age (years)')
    ),
    sexes_table AS (
        SELECT formrecordid as id, answers.listofvaluesid as sex, description as sexname
        FROM tb_questiongroupformrecord as answers
        JOIN tb_listofvalues as sexes
        ON answers.listofvaluesid = sexes.listofvaluesid
        WHERE questionid=(SELECT questionid FROM tb_questions WHERE description='Sex at Birth')
    )

    select (age/10)*10 || '-' || (age/10)*10+10-1 as agegroup, sexname, count(*)
    from ages_table
    join sexes_table
    on ages_table.id = sexes_table.id
    group by age/10, sexname
    order by agegroup,sexname;
    """

    df = pd.read_sql(query, con=con.get())

    df1 = df.pivot_table(columns=['agegroup', 'sexname'])
    sexes = list(set(df['sexname']))

    rows = []
    for agegroup in sorted(set(df['agegroup'])):
        row = [agegroup]
        for sex in sexes:
            try:
                row.append(df1[agegroup, sex][0])
            except KeyError:
                row.append(0)
        rows.append(row)

    df2 = pd.DataFrame(rows, columns=['agegroup'] + sexes)

    return graphs.get_grouped_bar_chart(df2, 'agegroup', sexes[0], sexes[1],
                                        sexes[0], sexes[1])
