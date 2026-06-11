import pandas as pd


def generate_excel_report(
    dataframe,
    filename
):

    dataframe.to_excel(
        filename,
        index=False
    )

    return filename