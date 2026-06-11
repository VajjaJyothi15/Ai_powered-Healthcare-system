import bcrypt
import streamlit as st


def hash_password(password):
    """
    Hash a password before storing in database.
    """
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password, hashed_password):
    """
    Verify entered password against stored hash.
    """
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def initialize_session():
    """
    Initialize session state variables.
    """
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if "user_name" not in st.session_state:
        st.session_state.user_name = None

    if "user_role" not in st.session_state:
        st.session_state.user_role = None

    if "username" not in st.session_state:
        st.session_state.username = None

    if "role" not in st.session_state:
        st.session_state.role = None


def login_user(user_id, user_name, role):
    """
    Store logged-in user details.
    """
    normalized_role = "Admin" if role == "Hospital Staff" else role

    st.session_state.logged_in = True
    st.session_state.user_id = user_id
    st.session_state.user_name = user_name
    st.session_state.user_role = normalized_role
    st.session_state.username = user_name
    st.session_state.role = normalized_role


def logout_user():
    """
    Clear session data.
    """
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_name = None
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.role = None


def is_authenticated():
    return st.session_state.get("logged_in", False)


def get_current_role():
    return st.session_state.get("user_role", None)
