import streamlit as st
import time

# إعدادات الصفحة وهوية البراند
st.set_page_config(page_title="فزعة جار - النموذج الأولي", page_icon="🤝")

# الألوان المعتمدة (CSS)
st.markdown(f"""
    <style>
    .main {{ background-color: #f5f5f5; }}
    .stButton>button {{
        background-color: #8338EC;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        height: 3em;
        font-weight: bold;
    }}
    .stButton>button:hover {{ background-color: #00AC73; color: white; }}
    .fazza-card {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #00AC73;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }}
    h1, h2, h3 {{ color: #8338EC; text-align: right; direction: rtl; }}
    p {{ text-align: right; direction: rtl; }}
    </style>
    """, unsafe_allow_html=True)

# الواجهة الرئيسية
st.title("🤝 تطبيق فزعة جار")
st.subheader("الجار للجار.. بضغطة زر")

# تبديل الحالات (State Management)
if 'step' not in st.session_state:
    st.session_state.step = 'home'

# --- الشاشة الأولى: طلب الفزعة ---
if st.session_state.step == 'home':
    st.markdown('<div class="fazza-card"><p>مرحباً بك يا جارنا العزيز! وش محتاج اليوم؟</p></div>', unsafe_allow_html=True)
    
    option = st.selectbox("", ["اختر نوع الفزعة", "اشتراك سيارة", "دريل / مثقاب", "سلم طويل", "مساعدة في نقل غرض"])
    
    if option != "اختر نوع الفزعة":
        if st.button("أرسل طلب فزعة للحي"):
            st.session_state.step = 'searching'
            st.rerun()

# --- الشاشة الثانية: البحث عن جار (الذكاء الاصطناعي) ---
elif st.session_state.step == 'searching':
    st.markdown('<div style="text-align:center">', unsafe_allow_html=True)
    st.write("جاري تحديد الجيران المتواجدين حالياً...")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    
    st.success("تم العثور على 3 جيران متاحين في نطاق 250 متر!")
    time.sleep(1)
    st.session_state.step = 'matched'
    st.rerun()

# --- الشاشة الثالثة: تم قبول الفزعة ---
elif st.session_state.step == 'matched':
    st.balloons()
    st.markdown("""
        <div class="fazza-card">
            <h3 style="color:#00AC73">أبشر بسعدك!</h3>
            <p>جارك <b>صالح (موثق عبر نفاذ)</b> قبل طلبك.</p>
            <p>📍 يبعد عنك: 3 دقائق مشياً (180 متر)</p>
            <p>التواصل: 💬 فتح المحادثة الآمنة</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("تم قضاء الحاجة (تقييم النخوة)"):
        st.success("تمت الفزعة! رصيدك الاجتماعي زاد +10 نقاط")
        if st.button("العودة للرئيسية"):
            st.session_state.step = 'home'
            st.rerun()
