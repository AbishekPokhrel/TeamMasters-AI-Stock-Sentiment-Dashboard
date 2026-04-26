import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def signup_user(email, password):
    try:
        return supabase.auth.sign_up({
            "email": email,
            "password": password
        })
    except Exception as e:
        st.error(f"Signup error: {e}")
        return None


def login_user(email, password):
    try:
        return supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
    except Exception as e:
        st.error(f"Login error: {e}")
        return None


def logout_user():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass


def send_reset_password_email(email):
    try:
        APP_URL = "https://teammasters-ai-stock-sentiment-dashboard-akkrcdbykusryyyknbljy.streamlit.app"

        supabase.auth.reset_password_for_email(
            email,
            {
                "redirect_to": APP_URL
            }
        )
        return True
    except Exception as e:
        st.error(f"Password reset error: {e}")
        return False

def update_user_password(new_password):
    try:
        supabase.auth.update_user({
            "password": new_password
        })
        return True
    except Exception as e:
        st.error(f"Update password error: {e}")
        return False


def create_profile(user_id, username, email):
    try:
        existing = (
            supabase.table("profiles")
            .select("id")
            .eq("id", user_id)
            .execute()
        )

        if existing.data:
            return True

        response = (
            supabase.table("profiles")
            .insert({
                "id": user_id,
                "username": username,
                "email": email
            })
            .execute()
        )

        return bool(response.data)

    except Exception as e:
        st.error(f"Create profile error: {e}")
        return False


def get_profile_username(user_id, email=None):
    try:
        response = (
            supabase.table("profiles")
            .select("username")
            .eq("id", user_id)
            .execute()
        )

        if response.data and len(response.data) > 0:
            return response.data[0]["username"]

        if email:
            response = (
                supabase.table("profiles")
                .select("username")
                .eq("email", email)
                .execute()
            )

            if response.data and len(response.data) > 0:
                return response.data[0]["username"]

        return ""

    except Exception as e:
        st.error(f"Get profile error: {e}")
        return ""


def update_profile_username(user_id, new_username, email=None):
    try:
        new_username = new_username.strip()

        if not new_username:
            st.error("Username cannot be empty.")
            return False

        response = (
            supabase.table("profiles")
            .update({"username": new_username})
            .eq("id", user_id)
            .execute()
        )

        if response.data:
            return True

        if email:
            response = (
                supabase.table("profiles")
                .update({"username": new_username})
                .eq("email", email)
                .execute()
            )

            if response.data:
                return True

        return False

    except Exception as e:
        st.error(f"Update username error: {e}")
        return False


def save_search(user_id, ticker, company_name, sentiment, score):
    try:
        response = (
            supabase.table("search_history")
            .insert({
                "user_id": user_id,
                "ticker": ticker.upper(),
                "company_name": company_name,
                "sentiment": sentiment,
                "score": float(score)
            })
            .execute()
        )

        return bool(response.data)

    except Exception as e:
        st.error(f"Save search error: {e}")
        return False


def get_search_history(user_id):
    try:
        response = (
            supabase.table("search_history")
            .select("*")
            .eq("user_id", user_id)
            .order("searched_at", desc=True)
            .execute()
        )

        return response.data if response.data else []

    except Exception as e:
        st.error(f"Get history error: {e}")
        return []


def delete_history_record(record_id, user_id):
    try:
        response = (
            supabase.table("search_history")
            .delete()
            .eq("id", record_id)
            .eq("user_id", user_id)
            .execute()
        )

        return bool(response.data)

    except Exception as e:
        st.error(f"Delete error: {e}")
        return False


def update_history_sentiment(record_id, user_id, new_sentiment):
    try:
        response = (
            supabase.table("search_history")
            .update({"sentiment": new_sentiment})
            .eq("id", record_id)
            .eq("user_id", user_id)
            .execute()
        )

        return bool(response.data)

    except Exception as e:
        st.error(f"Update error: {e}")
        return False
