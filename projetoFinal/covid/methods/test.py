from django.http import JsonResponse, HttpResponse
import json
import pandas as pd

import covid.methods.connection as con

def test_query():
    df = pd.read_sql('select * from information_schema.tables', con=con.get())

    output = {
        "title": "test",
        "headers": [],
        "content": json.loads(df.to_json(orient="split"))
    }

    return JsonResponse(output)
