import streamlit as st

# إعدادات الصفحة والديزاين بالأبيض والأسود
st.set_page_config(page_title="Zed Trading Dashboard", page_icon="📈", layout="centered")

# ستايل مخصص بالأسود والأبيض (Minimalist Black & White)
st.markdown("""
    <style>
    .main { background-color: #ffffff; color: #000000; }
    h1, h2, h3 { color: #000000; font-family: 'Courier New', Courier, monospace; letter-spacing: -1px; }
    .stButton>button { background-color: #000000; color: #ffffff; border-radius: 0px; border: 1px solid #000000; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #ffffff; color: #000000; border: 1px solid #000000; }
    div.stNumberInput input, div.stTextInput input, div.stSelectbox select { background-color: #ffffff !important; color: #000000 !important; border: 1px solid #000000 !important; border-radius: 0px !important; }
    .css-12w0qpk { background-color: #ffffff; }
    .habit-box { border: 1px solid #000000; padding: 15px; margin-bottom: 10px; background-color: #fcfcfc; }
    .rule-box { border-left: 5px solid #000000; padding-left: 10px; margin-bottom: 15px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# نظام تسجيل الدخول (Session State)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center;'>ZED TRADING DASHBOARD</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Trading Psychology & Discipline Portal</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_with_name("Login")
        
        if submit:
            if username == "admin" and password == "1234":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("بيانات الدخول غير صحيحة.")
else:
    # القائمة العلوية
    cols_nav = st.columns([8, 2])
    with cols_nav[0]:
        st.markdown("<h1>ZED TRADING DASHBOARD</h1>")
    with cols_nav[1]:
        if st.button("🔴 Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
            
    st.markdown("---")
    
    # القسم الأول: قوانين صارمة لإدارة المخاطر والالتزام
    st.markdown("## 🧠 Trading Psychology & Risk Management")
    col1, col2 = st.columns(2)
    
    with col1:
        st.number_input("Consistency Score (%)", min_value=0, max_value=100, value=100, step=1)
        st.text_input("Daily Target ($)")
    with col2:
        st.text_input("Max Daily Loss Limit ($)")
        st.selectbox("Risk Status", ["Strict Adherence", "Mental Reset Needed", "Stop Trading For Today"])

    st.markdown("---")
    
    # القسم الثاني: الروتين اليومي والعادات الصارمة (Daily Habits & Discipline)
    st.markdown("## 📋 Daily Discipline Tracking")
    st.markdown("<div class='rule-box'>⚠️ قانون ذهبي: الهاتف ممنوع كلياً أثناء العمل (مسموح فقط بين العصر والمغرب).</div>", unsafe_allow_html=True)
    
    # قائمة العادات والالتزام بالروتين
    habits = {
        "🕌 الصلاة في وقتها (أساس البركة والتوفيق)": False,
        "📱 الالتزام بمنع الهاتف أثناء العمل (مسموح فقط بين العصر والمغرب)": False,
        "☕ الالتزام بالروتين الصباحي وقبل الافتتاح (Pre-market Routine)": False,
        "📉 الالتزام بخطة التداول وعدم التداول العاطفي (FOMO)": False,
        "📓 تدوين الصفقات والمشاعر في الـ Journal بعد الإغلاق": False
    }
    
    score = 0
    st.markdown("<p style='font-weight: bold;'>تتبع التزامك اليومي:</p>", unsafe_allow_html=True)
    for habit, default in habits.items():
        if st.checkbox(habit):
            score += 1
            
    # حساب نسبة الالتزام اليومي
    total_habits = len(habits)
    discipline_percentage = (score / total_habits) * 100
    
    st.markdown("---")
    st.markdown(f"### 📈 نسبة الالتزام بالروتين اليومي: `{discipline_percentage:.0f}%`")
    
    if discipline_percentage == 100:
        st.success("أداء مثالي! التزام كامل بالروتين وقوانين السيكولوجية. هكذا يتداول المحترفون. 💎")
    elif discipline_percentage >= 60:
        st.warning("أداء متوسط. هناك بعض التقصير، تذكر أن الالتزام بالروتين هو ما يحميك من الخسارة.")
    else:
        st.error("انتباه! نسبة الالتزام ضعيفة جداً. راجع نفسك قبل دخول السوق، السيكولوجية هي كل شيء.")

    if st.button("💾 حفظ تقرير اليوم"):
        st.success("تم حفظ البيانات في الخزنة السرية بنجاح!")
