from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con
import covid.methods.graphs as graphs

def do_query(**kwargs):
    query = """
    WITH 
    outcome_types AS (
        SELECT values.listofvaluesid as id, values.description
        FROM tb_listtype AS list, 
            tb_listofvalues AS values 
        WHERE list.description = 'Outcome list'and list.listtypeid = values.listtypeid
    ),
    patient_answers AS(
        SELECT participantid, questionid, listofvaluesid, answer
        FROM tb_questiongroupformrecord AS answers
        INNER JOIN tb_formrecord AS formrecord
        ON answers.formrecordid = formrecord.formrecordid
        WHERE questionid=144 or listofvaluesid in (SELECT id FROM outcome_types)
    ),
    ages AS(
        SELECT participantid, CAST(answer as INTEGER) as age
        FROM patient_answers
        WHERE questionid = 144
    ),
    outcomes AS (
        SELECT participantid, listofvaluesid as outcome
        FROM patient_answers
        WHERE questionid != 144
    ),
    ages_outcomes AS(
    SELECT outcomes.participantid, age, outcome,
    CASE
        WHEN age < 40 THEN 0
        WHEN age > 60 THEN 2
        ELSE 1
    END AS agegroup
    FROM outcomes,ages
    WHERE outcomes.participantid = ages.participantid
    )

    SELECT agegroup, outcome, COUNT(*)
    FROM ages_outcomes
    GROUP BY outcome,agegroup
    ORDER BY agegroup;
    """


    df = pd.read_sql(query, con=con.get())

    df1 = df.pivot_table(columns=['outcome', 'agegroup'])
    outcomes = list(set(df['outcome']))

    rows = []
    for agegroup in set(df['agegroup']):
        row = [agegroup]
        for outcome in outcomes:
            row.append(df1[outcome,agegroup][0])
        rows.append(row)

    df2 = pd.DataFrame(rows, columns=['agegroup'] + outcomes)
    df2['agegroup'] = 'menores de 40 anos', 'entre 40 e 60 anos', 'maiores de 60 anos'

    return graphs.get_grouped_bar_chart(df2, "agegroup", outcomes[0], outcomes[1], "Mortes", "Altas")