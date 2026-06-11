from io import BytesIO

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def _dataframe_to_table_data(dataframe, max_rows=40):
    if dataframe is None or dataframe.empty:
        return [["Message"], ["No records found for this report."]]

    preview = dataframe.head(max_rows).copy()
    table_data = [list(preview.columns)]

    for _, row in preview.iterrows():
        table_data.append([str(value) for value in row.tolist()])

    return table_data


def _build_pdf(target, title, dataframe):
    doc = SimpleDocTemplate(
        target,
        pagesize=landscape(A4),
        rightMargin=24,
        leftMargin=24,
        topMargin=24,
        bottomMargin=24,
    )
    styles = getSampleStyleSheet()

    elements = [
        Paragraph(str(title), styles["Title"]),
        Spacer(1, 12),
    ]

    if isinstance(dataframe, pd.DataFrame):
        table_data = _dataframe_to_table_data(dataframe)
    else:
        table_data = [["Report Content"], [str(dataframe)]]

    table = Table(table_data, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565C0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
            ]
        )
    )
    elements.append(table)

    doc.build(elements)


def generate_pdf_report(filename, title, content):
    _build_pdf(filename, title, content)
    return filename


def generate_pdf_report_bytes(title, dataframe):
    buffer = BytesIO()
    _build_pdf(buffer, title, dataframe)
    buffer.seek(0)
    return buffer.getvalue()
