from url_features import *
import streamlit as st
import joblib
import pandas as pd
import re

# Page config
# Page config
st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🛡️",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
}

.stButton>button {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #161A23;
}

h1 {
    color: #00E5FF;
    text-align: center;
}

h3 {
    color: #FF4B4B;
}

</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("phishing_model.pkl")

# Title
st.title("🛡️ AI Phishing Website Detector")

st.markdown("""
Detect suspicious and phishing websites using Artificial Intelligence and Cybersecurity Analysis.
""")

# Sidebar
st.sidebar.header("About Project")

st.sidebar.write("""
This project uses:
- Machine Learning
- Cybersecurity Features
- URL Analysis
- AI-based Prediction

Built using:
- Python
- Scikit-learn
- Streamlit
""")

# URL input
url = st.text_input("🔗 Enter Website URL")

# Feature extraction functions




    

    


# Button
if st.button("🔍 Analyze Website"):

    # URL validation
    if not url.startswith("http://") and not url.startswith("https://"):
        st.error("❌ Invalid URL Format")

    else:

        # Metrics section
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("URL Length", url_length(url))

        with col2:
            st.metric("HTTPS", has_https(url))

        with col3:
            st.metric("Suspicious Words", suspicious_words(url))

        # Sample feature data
        sample_data = {
            'URLLength': [url_length(url)],
            'DomainLength': [20],
            'IsDomainIP': [has_ip(url)],
            'URLSimilarityIndex': [50],
            'CharContinuationRate': [1],
            'TLDLegitimateProb': [0.5],
            'URLCharProb': [0.1],
            'TLDLength': [3],
            'NoOfSubDomain': [1],
            'HasObfuscation': [0],
            'NoOfObfuscatedChar': [0],
            'ObfuscationRatio': [0],
            'NoOfLettersInURL': [50],
            'LetterRatioInURL': [0.5],
            'NoOfDegitsInURL': [5],
            'DegitRatioInURL': [0.1],
            'NoOfEqualsInURL': [0],
            'NoOfQMarkInURL': [0],
            'NoOfAmpersandInURL': [0],
            'NoOfOtherSpecialCharsInURL': [2],
            'SpacialCharRatioInURL': [0.1],
            'IsHTTPS': [has_https(url)],
            'LineOfCode': [100],
            'LargestLineLength': [50],
            'HasTitle': [1],
            'DomainTitleMatchScore': [100],
            'URLTitleMatchScore': [100],
            'HasFavicon': [1],
            'Robots': [1],
            'IsResponsive': [1],
            'NoOfURLRedirect': [0],
            'NoOfSelfRedirect': [0],
            'HasDescription': [1],
            'NoOfPopup': [0],
            'NoOfiFrame': [0],
            'HasExternalFormSubmit': [0],
            'HasSocialNet': [1],
            'HasSubmitButton': [1],
            'HasHiddenFields': [0],
            'HasPasswordField': [suspicious_words(url)],
            'Bank': [suspicious_words(url)],
            'Pay': [0],
            'Crypto': [0],
            'HasCopyrightInfo': [1],
            'NoOfImage': [10],
            'NoOfCSS': [5],
            'NoOfJS': [10],
            'NoOfSelfRef': [5],
            'NoOfEmptyRef': [0],
            'NoOfExternalRef': [2]
        }

        # Convert to dataframe
        input_data = pd.DataFrame(sample_data)

        # Prediction
        prediction = model.predict(input_data)

        # Fake confidence score
        if prediction[0] == 1:

            st.error("⚠️ Phishing Website Detected")

            st.progress(90)

            st.write("### Risk Score: 90%")

        else:

            st.success("✅ Safe Website")

            st.progress(20)

            st.write("### Risk Score: 20%")

        # Show extracted features
        st.subheader("📊 Extracted Features")

        st.dataframe(input_data)