import streamlit as st
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Network Intrusion Detection System",
    page_icon="🔐",
    layout="wide"
)

# -----------------------------
# Load Model and Scaler
# -----------------------------
model = load_model("models/network_intrusion_detection_ann.keras")
scaler = joblib.load("models/scaler.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🔐 Network Intrusion Detection System using ANN")

st.write("""
Upload a CSV file containing the **52 network traffic features**.
The ANN model will classify each network connection as:

- ✅ Normal Traffic
- 🚨 Attack Traffic
""")

# -----------------------------
# Expected Features
# -----------------------------
expected_features = [
    "Destination Port",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Length of Fwd Packets",
    "Fwd Packet Length Max",
    "Fwd Packet Length Min",
    "Fwd Packet Length Mean",
    "Fwd Packet Length Std",
    "Bwd Packet Length Max",
    "Bwd Packet Length Min",
    "Bwd Packet Length Mean",
    "Bwd Packet Length Std",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow IAT Max",
    "Flow IAT Min",
    "Fwd IAT Total",
    "Fwd IAT Mean",
    "Fwd IAT Std",
    "Fwd IAT Max",
    "Fwd IAT Min",
    "Bwd IAT Total",
    "Bwd IAT Mean",
    "Bwd IAT Std",
    "Bwd IAT Max",
    "Bwd IAT Min",
    "Fwd Header Length",
    "Bwd Header Length",
    "Fwd Packets/s",
    "Bwd Packets/s",
    "Min Packet Length",
    "Max Packet Length",
    "Packet Length Mean",
    "Packet Length Std",
    "Packet Length Variance",
    "FIN Flag Count",
    "PSH Flag Count",
    "ACK Flag Count",
    "Average Packet Size",
    "Subflow Fwd Bytes",
    "Init_Win_bytes_forward",
    "Init_Win_bytes_backward",
    "act_data_pkt_fwd",
    "min_seg_size_forward",
    "Active Mean",
    "Active Max",
    "Active Min",
    "Idle Mean",
    "Idle Max",
    "Idle Min"
]

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # -----------------------------
    # Validate Columns
    # -----------------------------
    if list(df.columns) != expected_features:

        st.error("❌ Uploaded CSV does not contain the required 52 features in the correct order.")

        st.write("Expected Columns:")

        st.write(expected_features)

    else:

        if st.button("Predict"):

            # Scale Data
            scaled_data = scaler.transform(df)

            # Prediction Probabilities
            probabilities = model.predict(scaled_data)

            # Binary Prediction
            predictions = (probabilities > 0.5).astype(int)

            # Add Results
            df["Prediction"] = predictions

            df["Prediction"] = df["Prediction"].map({
                0: "Normal Traffic",
                1: "Attack Traffic"
            })

            df["Probability"] = probabilities

            normal_count = (df["Prediction"] == "Normal Traffic").sum()
            attack_count = (df["Prediction"] == "Attack Traffic").sum()

            col1, col2 = st.columns(2)

            with col1:
                st.success(f"Normal Traffic : {normal_count}")

            with col2:
                st.error(f"Attack Traffic : {attack_count}")

            # -----------------------------
            # Results
            # -----------------------------
            st.subheader("Prediction Results")

            st.dataframe(df)