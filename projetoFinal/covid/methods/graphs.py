import pandas as pd

def get_chart(df: pd.DataFrame, x_column, y_column, width=80):

    bg_color = "rgba(158,202,225,0.8)"

    if not isinstance(df, pd.DataFrame):
        raise Exception("Not a pandas dataFrame")

    return dict(zip(df[x_column].tolist(), df[y_column].tolist()))


def get_card(value: str, desc: str, icon: int) -> dict:
    # ajust
    max_desc_len = 60

    if len(desc) > max_desc_len:
        raise Exception(f'Description text too big. Keep under {max_desc_len} chars')

    return {"value": value, "desc":  desc}

def get_grouped_bar_chart(df: pd.DataFrame, x_column, y_column_trace1, y_column_trace2,
                           name_trace1, name_trace2, width=80):

    if not isinstance(df, pd.DataFrame):
        raise Exception("Not a pandas dataFrame")

    trace1 = {
        "label": name_trace1,
        "backgroundColor": "rgba(90, 230, 213, 0.8)",
        "barThickness": width,
        "data": df[y_column_trace1].tolist()
    }

    trace2 = {
        "label": name_trace2,
        "backgroundColor": "rgba(90, 230, 213, 0.8)",
        "barThickness": width,
        "data": df[y_column_trace2].tolist(),
    }

    return {
        #"labels": df[x_column].tolist(),
        "labels": anonymize(df[x_column].tolist()),
        "datasets": [trace1, trace2]
    }
