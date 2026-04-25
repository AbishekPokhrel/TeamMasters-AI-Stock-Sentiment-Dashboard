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
    except Exception:
        return None


def login_user(email, password):
    try:
        return supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
    except Exception:
        return None


def create_profile(user_id, username, email):
    try:
        supabase.table("profiles").insert({
            "id": user_id,
            "username": username,
            "email": email
        }).execute()
    except Exception:
        pass


def get_profile_username(user_id):
    try:
        response = supabase.table("profiles").select("username").eq("id", user_id).execute()
        if response.data and len(response.data) > 0:
            return response.data[0]["username"]
        return ""
    except Exception:
        return ""


def save_search(user_id, ticker, company_name, sentiment, score):
    try:
        supabase.table("search_history").insert({
            "user_id": user_id,
            "ticker": ticker.upper(),
            "company_name": company_name,
            "sentiment": sentiment,
            "score": float(score)
        }).execute()
    except Exception:
        pass


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
    except Exception:
        return []


def delete_history_record(record_id, user_id):
    try:
        (
            supabase.table("search_history")
            .delete()
            .eq("id", record_id)
            .eq("user_id", user_id)
            .execute()
        )
    except Exception:
        pass


def update_history_sentiment(record_id, user_id, new_sentiment):
    try:
        (
            supabase.table("search_history")
            .update({"sentiment": new_sentiment})
            .eq("id", record_id)
            .eq("user_id", user_id)
            .execute()
        )
    except Exception:
        pass
