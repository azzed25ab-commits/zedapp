import streamlit as st

st.set_page_config(page_title="RS Circle Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .stApp { background-color: #08090a; color: #d1d4dc; }
    [data-testid="stSidebar"] { background-color: #0c0d0e; border-right: 1px solid #1e222d; }
    .metric-card { background-color: #131722; border: 1px solid #1e222d; padding: 20px; border-radius: 8px; text-align: center; }
    .metric-value { font-size: 32px; font-weight: bold; color: #26a69a; }
    .metric-label { font-size: 14px; color: #787b86; }
    .gauge-container { text-align: center; padding: 30px; background: #131722; border-radius: 12px; border: 1px solid #1e222d; }
    .gauge-value { font-size: 50px; font-weight: bold; color: #26a69a; text-shadow: 0 0 15px rgba(38, 166, 154, 0.4); }
    .calendar-box { background-color: #131722; border: 1px solid #1e222d; border-radius: 12px; padding: 20px; }
    div.stButton > button { background-color: #1e222d !important; color: #d1d4dc !important; border: 1px solid #2a2e39 !important; }
    div.stButton > button:hover { border-color: #26a69a !important; color: #26a69a !important; }
    .login-box { max-width: 400px; margin: 80px auto; padding: 30px; background-color: #131722; border: 1px solid #1e222d; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def check_login(username, password):
    if username == "admin" and password == "1234":
        st.session_state['logged_in'] = True
        st.rerun()
    else:
        st.error("❌ Username ولا Password غلط!")

if not st.session_state['logged_in']:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#26a69a;'>🔐 RS Circle Login</h2>", unsafe_allow_html=True)
    user_input = st.text_input("Username", placeholder="Username")
    pass_input = st.text_input("Password", type="password", placeholder="Password")
    if st.button("دخول للموقع 🚀", use_container_width=True):
        check_login(user_input, pass_input)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    with st.sidebar:
        st.markdown("<h2 style='color:#26a69a; font-weight:bold;'>🟢 RS Circle</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<div style='background-color:#131722; padding:15px; border-radius:8px; border:1px solid #1e222d;'><p style='margin:0; font-weight:bold; color:#d1d4dc;'>👤 Azddine Ab...</p></div>", unsafe_allow_html=True)
        for option in ["🏠 Dashboard", "🕒 Trade History", "📊 Charts", "🏆 Leaderboard", "⚙️ Settings"]:
            st.button(option, use_container_width=True, key=option)
        if st.button("🚪 Log Out", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    st.markdown("### 📊 Habit Tracker")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1: st.markdown('<div class="metric-card"><div class="metric-value">0</div><div class="metric-label">HABIT PTS</div></div>', unsafe_allow_html=True)
    with col_m2: st.markdown('<div class="metric-card"><div class="metric-value" style="color:#ff5252;">50%</div><div class="metric-label">WEIGHT</div></div>', unsafe_allow_html=True)
    with col_m3: st.markdown('<div class="metric-card"><div class="metric-value">120</div><div class="metric-label">LEFT</div></div>', unsafe_allow_html=True)

    st.write("")
    for h in [{"name": "🌅 Wake Up Early", "desc": "Rise at 8:00 AM"}, {"name": "💪 Exercise", "desc": "Physical activity"}]:
        col_h1, col_h2, col_h3 = st.columns([4, 1, 1])
        with col_h1: st.markdown(f"<div style='padding:10px;'><b>{h['name']}</b><br><small style='color:#787b86;'>{h['desc']}</small></div>", unsafe_allow_html=True)
        with col_h2: st.button("📷 Proof required", key=f"proof_{h['name']}")
        with col_h3: st.checkbox("Done", key=f"check_{h['name']}")
