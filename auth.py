import streamlit as st
from database import (
    login_user,
    signup_user,
    create_profile,
    get_profile_username,
    send_reset_password_email,
    update_user_password,
    get_search_history,
    delete_history_record,
    update_history_sentiment,
    save_search,
    update_profile_username,
)

def init_session_state():
    if "selected_ticker" not in st.session_state:
        st.session_state.selected_ticker = ""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = ""
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "home"
    if "landing_section" not in st.session_state:
        st.session_state.landing_section = "home"
    if "reset_session" not in st.session_state:
        st.session_state.reset_session = False
    if "processed_recovery_token" not in st.session_state:
        st.session_state.processed_recovery_token = None
    if "supabase_access_token" not in st.session_state:
        st.session_state.supabase_access_token = None
    if "supabase_refresh_token" not in st.session_state:
        st.session_state.supabase_refresh_token = None

def do_logout():
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_email = ""
    st.session_state.username = ""
    st.session_state.auth_mode = "home"
    st.session_state.landing_section = "home"
    st.session_state.reset_session = False


def login_section():
    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">Login to Your Account</div>', unsafe_allow_html=True)

    email_input = st.text_input("Email", key="login_email")
    password_input = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", use_container_width=True, key="login_submit_btn"):
        if not email_input.strip() or not password_input.strip():
            st.warning("Please enter email and password.")
        else:
            response = login_user(email_input.strip(), password_input.strip())

            if response and response.user:
                st.session_state.logged_in = True
                st.session_state.user_id = response.user.id
                st.session_state.user_email = response.user.email

                st.session_state.username = get_profile_username(
                    response.user.id,
                    response.user.email
                )

                st.session_state.auth_mode = "home"
                st.rerun()
            else:
                st.error("Invalid email or password.")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Forgot Password", use_container_width=True, key="go_to_forgot_password"):
            st.session_state.auth_mode = "forgot_password"
            st.rerun()

    with c2:
        if st.button("Back Home", use_container_width=True, key="back_from_login"):
            st.session_state.auth_mode = "home"
            st.session_state.landing_section = "home"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    
def forgot_password_section():
    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">Forgot Password</div>', unsafe_allow_html=True)

    forgot_email = st.text_input("Enter your email", key="forgot_password_email")

    if st.button("Send Reset Email", use_container_width=True, key="forgot_password_btn"):
        if not forgot_email.strip():
            st.warning("Please enter your email.")
        else:
            success = send_reset_password_email(forgot_email.strip())
            if success:
                st.success("Password reset email sent. Please check your inbox and open the newest reset link.")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Back to Login", use_container_width=True, key="back_to_login_from_forgot"):
            st.session_state.auth_mode = "login"
            st.rerun()

    with c2:
        if st.button("Back Home", use_container_width=True, key="back_home_from_forgot"):
            st.session_state.auth_mode = "home"
            st.session_state.landing_section = "home"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def signup_section():
    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">Create Your Account</div>', unsafe_allow_html=True)

    username_input = st.text_input("Username", key="signup_username")
    email_input = st.text_input("Email", key="signup_email")
    password_input = st.text_input("Password", type="password", key="signup_password")

    if st.button("Sign Up", use_container_width=True, key="signup_submit_btn"):
        if not username_input.strip() or not email_input.strip() or not password_input.strip():
            st.warning("Please fill all fields.")
        else:
            response = signup_user(email_input.strip(), password_input.strip())
            if response and response.user:
                create_profile(response.user.id, username_input.strip(), email_input.strip())

                login_response = login_user(email_input.strip(), password_input.strip())
                if login_response and login_response.user:
                    st.session_state.logged_in = True
                    st.session_state.user_id = login_response.user.id
                    st.session_state.user_email = login_response.user.email
                    st.session_state.username = username_input.strip()
                    st.session_state.auth_mode = "home"
                    st.rerun()
                else:
                    st.success("Account created. Please login.")
                    st.session_state.auth_mode = "login"
                    st.rerun()
            else:
                st.error("Signup failed.")

    if st.button("Back to Home", use_container_width=True, key="back_from_signup"):
        st.session_state.auth_mode = "home"
        st.session_state.landing_section = "home"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def reset_password_section():
    st.markdown('<div class="auth-box">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">Reset Your Password</div>', unsafe_allow_html=True)

    new_password = st.text_input("New Password", type="password", key="reset_new_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="reset_confirm_password")

    if st.button("Update Password", use_container_width=True, key="reset_password_submit"):
        if not st.session_state.get("reset_session", False):
            st.error("Reset session missing or expired. Please use the password reset link again.")
        elif not new_password.strip() or not confirm_password.strip():
            st.warning("Please fill both fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        elif len(new_password) < 6:
            st.warning("Password must be at least 6 characters.")
        else:
            success = update_user_password(new_password)

            if success:
                st.success("Password updated successfully. Please login with your new password.")

                st.session_state.reset_session = False
                st.session_state.processed_recovery_token = None
                st.session_state.supabase_access_token = None
                st.session_state.supabase_refresh_token = None
                st.session_state.auth_mode = "login"

                try:
                    st.query_params.clear()
                except Exception:
                    pass

                st.rerun()
            else:
                st.error("Failed to update password.")

    if st.button("Back to Login", use_container_width=True, key="back_from_reset"):
        st.session_state.reset_session = False
        st.session_state.processed_recovery_token = None
        st.session_state.supabase_access_token = None
        st.session_state.supabase_refresh_token = None
        st.session_state.auth_mode = "login"

        try:
            st.query_params.clear()
        except Exception:
            pass

        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
def show_navbar():
    nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns([2.3, 1, 1, 1, 1, 1, 1])

    with nav1:
        st.markdown('<div class="landing-logo">TeamMasters AI</div>', unsafe_allow_html=True)

    with nav2:
        if st.button("Features", use_container_width=True, key="nav_features"):
            st.session_state.landing_section = "features"

    with nav3:
        if st.button("Why Us?", use_container_width=True, key="nav_whyus"):
            st.session_state.landing_section = "whyus"

    with nav4:
        if st.button("FAQ", use_container_width=True, key="nav_faq"):
            st.session_state.landing_section = "faq"

    with nav5:
        if st.button("Pricing", use_container_width=True, key="nav_pricing"):
            st.session_state.landing_section = "pricing"

    with nav6:
        if st.button("Tutorials", use_container_width=True, key="nav_tutorials"):
            st.session_state.landing_section = "tutorials"

    with nav7:
        if st.button("Home", use_container_width=True, key="nav_home"):
            st.session_state.landing_section = "home"

    st.markdown("<div style='margin-bottom: 18px;'></div>", unsafe_allow_html=True)


def show_home_section():
    st.markdown("""
    <div class="landing-hero">
        <div class="landing-badge">BACKED BY AI-POWERED MARKET RESEARCH</div>
        <div class="landing-title">Smarter Stock Research, without the noise</div>
        <div class="landing-subtitle">
            Ask any investing question and get a structured answer on valuation, risks, catalysts,
            and what to watch next.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:
        if st.button("Try for Free", use_container_width=True, key="try_for_free_btn"):
            st.session_state.auth_mode = "signup"
            st.rerun()

        if st.button("Login", use_container_width=True, key="home_login_btn"):
            st.session_state.auth_mode = "login"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">AI Sentiment Analysis</div>
            <div class="feature-text">
                Analyze stock news sentiment instantly from real financial headlines and convert
                large amounts of information into a simple market view.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Track Price Trends</div>
            <div class="feature-text">
                View stock movement with clean charts and market signals so users can connect
                news sentiment with price direction.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">Save Search History</div>
            <div class="feature-text">
                Users can log in and keep their own personal stock research history for future use,
                making the platform more useful over time.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Platform Highlights")
    h1, h2, h3 = st.columns(3)

    with h1:
        st.info("Clean, beginner-friendly stock research experience")
    with h2:
        st.info("Useful for portfolio projects, demos, and class presentations")
    with h3:
        st.info("Combines sentiment analysis, stock data, and user accounts")


def show_features_section():
    st.markdown("## Features")
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">What TeamMasters AI Can Do</div>
        <div class="feature-text">
            • Analyze stock-related news articles<br>
            • Calculate positive, neutral, and negative sentiment<br>
            • Show stock price trend charts<br>
            • Save user-specific stock searches<br>
            • Provide a modern dashboard after login<br>
            • Support multiple users with separate accounts
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_whyus_section():
    st.markdown("## Why Us?")
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Why TeamMasters AI Stands Out</div>
        <div class="feature-text">
            TeamMasters AI is designed for students, beginners, and project demos that need a simple
            but powerful stock research interface.
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_faq_section():
    st.markdown("## Frequently Asked Questions")

    with st.expander("What does TeamMasters AI do?"):
        st.write("It analyzes stock-related news, gives sentiment results, shows price trends, and allows users to save their stock research history.")

    with st.expander("Do I need an account?"):
        st.write("You can view the landing page without an account, but you need to sign in to use the full dashboard and saved search features.")


def show_pricing_section():
    st.markdown("## Pricing")
    st.info("Free plan available. Pro plan can be added later.")


def show_tutorials_section():
    st.markdown("## Tutorials")
    st.write("1. Create account")
    st.write("2. Login")
    st.write("3. Search ticker")
    st.write("4. Review results")


def show_bottom_cta():
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## Ready to Start?")

    c1, c2, c3 = st.columns([1, 1, 1])

    with c2:
        if st.button("Create Account", use_container_width=True, key="bottom_signup_btn"):
            st.session_state.auth_mode = "signup"
            st.rerun()

        if st.button("Sign In", use_container_width=True, key="bottom_signin_btn"):
            st.session_state.auth_mode = "login"
            st.rerun()


def show_landing_page():
    show_navbar()

    if st.session_state.auth_mode == "home":
        section = st.session_state.landing_section

        if section == "home":
            show_home_section()
        elif section == "features":
            show_features_section()
        elif section == "whyus":
            show_whyus_section()
        elif section == "faq":
            show_faq_section()
        elif section == "pricing":
            show_pricing_section()
        elif section == "tutorials":
            show_tutorials_section()

        show_bottom_cta()

    elif st.session_state.auth_mode == "login":
        login_section()

    elif st.session_state.auth_mode == "forgot_password":
        forgot_password_section()

    elif st.session_state.auth_mode == "signup":
        signup_section()

    elif st.session_state.auth_mode == "reset_password":
        reset_password_section()
