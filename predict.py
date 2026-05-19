import joblib
import pandas as pd

# Load saved model
model = joblib.load("phishing_model.pkl")

# Example input data
sample_data = {
    'URLLength': [100],
    'DomainLength': [20],
    'IsDomainIP': [0],
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
    'IsHTTPS': [1],
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
    'HasPasswordField': [1],
    'Bank': [0],
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

# Output
if prediction[0] == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Safe Website")