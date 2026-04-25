import streamlit as st


def apply_global_styles():
    st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle at top, #0f1b13 0%, #071018 40%, #050b12 100%);
            color: #e5e7eb;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 1rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .landing-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255,255,255,0.08);
            padding: 16px 24px;
            border-radius: 16px;
            margin-bottom: 40px;
            backdrop-filter: blur(8px);
        }

        .landing-logo {
            font-size: 26px;
            font-weight: 800;
            color: white;
        }

        .landing-menu {
            font-size: 16px;
            color: #d1d5db;
            font-weight: 600;
        }

        .landing-hero {
            text-align: center;
            padding-top: 30px;
            padding-bottom: 20px;
        }

        .landing-badge {
            color: #73c545;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 24px;
            letter-spacing: 1px;
        }

        .landing-title {
            font-size: 4rem;
            font-weight: 800;
            line-height: 1.1;
            color: #f9fafb;
            text-shadow: 0 0 18px rgba(255,255,255,0.15);
            margin-bottom: 22px;
        }

        .landing-subtitle {
            font-size: 1.35rem;
            color: #9ca3af;
            max-width: 900px;
            margin: 0 auto 30px auto;
            line-height: 1.8;
        }

        .feature-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(115,197,69,0.22);
            border-radius: 20px;
            padding: 24px;
            min-height: 180px;
            margin-top: 24px;
            backdrop-filter: blur(8px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.20);
        }

        .feature-title {
            font-size: 1.25rem;
            font-weight: 800;
            color: #8dd34f;
            margin-bottom: 12px;
        }

        .feature-text {
            font-size: 1rem;
            color: #d1d5db;
            line-height: 1.7;
        }

        .auth-box {
            max-width: 520px;
            margin: 40px auto;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 28px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.22);
        }

        .auth-title {
            font-size: 2rem;
            font-weight: 800;
            color: white;
            margin-bottom: 20px;
            text-align: center;
        }

        .hero-box {
            background: linear-gradient(135deg, rgba(37,99,235,0.20), rgba(79,70,229,0.20));
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 28px;
            margin-bottom: 22px;
            box-shadow: 0 12px 32px rgba(0,0,0,0.28);
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
            line-height: 1.15;
        }

        .hero-subtitle {
            font-size: 1rem;
            color: #cbd5e1;
            line-height: 1.7;
        }

        .metric-card {
            background: linear-gradient(180deg, rgba(30,41,59,0.95), rgba(15,23,42,0.95));
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 20px;
            padding: 18px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.22);
            min-height: 110px;
        }

        .metric-label {
            font-size: 0.92rem;
            color: #94a3b8;
            margin-bottom: 8px;
        }

        .metric-value {
            font-size: 1.4rem;
            font-weight: 800;
            color: white;
            line-height: 1.2;
        }

        .metric-change {
            font-size: 0.9rem;
            color: #60a5fa;
            margin-top: 6px;
        }

        .section-label, .quick-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: white;
            margin-top: 18px;
            margin-bottom: 10px;
        }

        .article-card {
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 14px;
        }

        .article-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: white;
            margin-bottom: 6px;
        }

        .article-meta {
            font-size: 0.88rem;
            color: #94a3b8;
            margin-bottom: 8px;
        }

        .article-desc {
            font-size: 0.95rem;
            color: #e2e8f0;
            margin-bottom: 10px;
        }

        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding: 12px 18px;
            border-radius: 16px;
            background: rgba(255,255,255,0.05);
        }

        .topbar-left {
            color: white;
            font-weight: 800;
            font-size: 1.1rem;
        }

        .topbar-right {
            color: #cbd5e1;
            font-size: 1rem;
        }

        div[data-baseweb="input"] > div {
            background-color: #0f172a !important;
            border: 1px solid #334155 !important;
            border-radius: 16px !important;
            min-height: 52px !important;
        }

        div[data-baseweb="input"] input {
            color: white !important;
            font-size: 16px !important;
        }

        div.stButton > button {
            border: none !important;
            border-radius: 16px !important;
            height: 50px;
            font-weight: 700;
            font-size: 16px;
            color: white !important;
            background: linear-gradient(135deg, #5ea126, #4b8a1d) !important;
            box-shadow: 0 8px 20px rgba(94,161,38,0.30);
            margin-top: 8px;
        }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("""
<style>
/* Navbar buttons */
div.stButton > button {
    border: none !important;
    border-radius: 14px !important;
    height: 46px;
    font-weight: 700;
    font-size: 15px;
    color: white !important;
    background: linear-gradient(135deg, #5ea126, #4b8a1d) !important;
    box-shadow: 0 8px 20px rgba(94,161,38,0.25);
    margin-top: 6px;
}

.landing-logo {
    font-size: 28px;
    font-weight: 900;
    color: #8dd34f;
    letter-spacing: 1px;
    text-shadow: 0 0 10px rgba(141, 211, 79, 0.35);
    padding-top: 8px;
}

.landing-hero {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
}

.landing-badge {
    color: #73c545;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 20px;
    letter-spacing: 1px;
}

.landing-title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.1;
    color: #f9fafb;
    margin-bottom: 18px;
}

.landing-subtitle {
    font-size: 1.2rem;
    color: #9ca3af;
    max-width: 850px;
    margin: 0 auto 30px auto;
    line-height: 1.7;
}

.feature-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(115,197,69,0.22);
    border-radius: 20px;
    padding: 24px;
    min-height: 180px;
    margin-top: 20px;
    backdrop-filter: blur(8px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.20);
}

.feature-title {
    font-size: 1.2rem;
    font-weight: 800;
    color: #8dd34f;
    margin-bottom: 12px;
}

.feature-text {
    font-size: 1rem;
    color: #d1d5db;
    line-height: 1.7;
}

.auth-box {
    max-width: 520px;
    margin: 30px auto;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.22);
}

.auth-title {
    font-size: 2rem;
    font-weight: 800;
    color: white;
    margin-bottom: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
    
st.markdown("## Account Settings")


   
   

   