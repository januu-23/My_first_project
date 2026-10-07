import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
    min-height: 100vh;
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
    text-shadow: 2px 3px 8px rgba(0,0,0,0.3);
}

.subtitle {
    text-align: center;
    color: #f5f5f5;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Converter card */
.converter-card {
    background: rgba(255,255,255,0.95);
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

/* Labels */
label {
    font-weight: 700 !important;
    color: #4a148c !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0 8px 20px rgba(221,36,118,0.4);
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 12px 25px rgba(221,36,118,0.6);
}

/* Result */
.result-box {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-top: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.result-title {
    font-size: 18px;
    font-weight: 600;
}

.result-value {
    font-size: 32px;
    font-weight: 800;
}

/* Currency cards */
.currency-card {
    background: rgba(255,255,255,0.9);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.currency-name {
    color: #6a1b9a;
    font-size: 20px;
    font-weight: bold;
}

.currency-rate {
    color: #333;
    font-size: 16px;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    margin-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CURRENCY DATA ----------------

rates = {
    "USD": 1.00,
    "INR": 83.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "AUD": 1.53,
    "CAD": 1.36
}

symbols = {
    "USD": "$",
    "INR": "₹",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "AUD": "A$",
    "CAD": "C$"
}

currency_names = {
    "USD": "US Dollar 🇺🇸",
    "INR": "Indian Rupee 🇮🇳",
    "EUR": "Euro 🇪🇺",
    "GBP": "British Pound 🇬🇧",
    "JPY": "Japanese Yen 🇯🇵",
    "AUD": "Australian Dollar 🇦🇺",
    "CAD": "Canadian Dollar 🇨🇦"
}


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title"> Currency Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ Convert your money quickly, easily and beautifully ✨</div>',
    unsafe_allow_html=True
)


# ---------------- CONVERTER ----------------

st.markdown('<div class="converter-card">', unsafe_allow_html=True)

amount = st.number_input(
    "💰 Enter Amount",
    min_value=0.0,
    value=100.0,
    step=1.0
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "🌎 From Currency",
        list(rates.keys())
    )

with col2:
    to_currency = st.selectbox(
        "🌍 To Currency",
        list(rates.keys())
    )

st.write("")

convert = st.button("💱 CONVERT NOW")

st.markdown('</div>', unsafe_allow_html=True)


# ---------------- CONVERSION ----------------

if convert:

    usd_amount = amount / rates[from_currency]

    converted_amount = usd_amount * rates[to_currency]

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-title">Conversion Result</div>
            <div class="result-value">
                {symbols[from_currency]}{amount:,.2f}
                {from_currency}
                =
                {symbols[to_currency]}{converted_amount:,.2f}
                {to_currency}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- POPULAR CURRENCIES ----------------

st.markdown("### 🌟 Popular Currencies")

col1, col2, col3 = st.columns(3)

popular = ["USD", "INR", "EUR"]

for col, currency in zip([col1, col2, col3], popular):

    with col:
        st.markdown(
            f"""
            <div class="currency-card">
                <div class="currency-name">
                    {symbols[currency]} {currency}
                </div>
                <div class="currency-rate">
                    {currency_names[currency]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        💜  Currency Converter <br>
        Built with Python 🐍 + Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True
)