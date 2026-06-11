import streamlit as st

from config.database import initialize_database
from config.auth_config import initialize_session, logout_user

from modules.authentication.login import login_page
from modules.authentication.register import register_page

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from utils.roles import (
    patient_role,
    doctor_role,
    admin_role
)

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Healthcare Prediction & Resource Management System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# DATABASE INITIALIZATION
# ----------------------------------

initialize_database()
initialize_session()

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.main-header {
    text-align:center;
    font-size:36px;
    font-weight:bold;
    color:#1565C0;
}

.sub-header {
    text-align:center;
    font-size:18px;
    color:gray;
}

.metric-card {
    padding:15px;
    border-radius:10px;
    background-color:#f5f5f5;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# HOME PAGE
# ----------------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class='main-header'>
        🏥 AI-Powered Healthcare Prediction &
        Resource Management System
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-header'>
        Intelligent Healthcare Platform using
        Artificial Intelligence, Machine Learning,
        Resource Optimization and Predictive Analytics
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Login",
            "Register"
        ]
    )

    if menu == "Login":
        login_page()

    elif menu == "Register":
        register_page()
else:

    display_name = st.session_state.get("username") or st.session_state.get("user_name")
    display_role = st.session_state.get("role") or st.session_state.get("user_role")

    st.sidebar.success(f"Welcome {display_name}")
    st.sidebar.write(f"Role: {display_role}")

    if st.sidebar.button("Logout"):
        logout_user()
        st.rerun()

    if display_role == "Patient":
        patient_role()

    elif display_role == "Doctor":
        doctor_role()

    elif display_role == "Admin":
        admin_role()

    else:
        st.error("Invalid role assigned.")
