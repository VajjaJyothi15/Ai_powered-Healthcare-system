import pandas as pd

from config.database import get_connection


def get_financial_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT
                patient_user_id,
                insurance_provider,
                policy_number
            FROM insurance
            """,
            conn
        )

    except Exception:

        df = pd.DataFrame(
            {
                "Revenue": [0],
                "Expenses": [0],
                "Profit": [0]
            }
        )

    conn.close()

    return df