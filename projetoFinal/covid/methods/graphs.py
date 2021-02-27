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
