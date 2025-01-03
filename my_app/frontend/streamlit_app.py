# frontend/streamlit_app.py

import streamlit as st
import pandas as pd
import requests

def main():
    st.title("Data Entry App")

    st.header("Enter Information")
    lead_dbp = st.text_input("Lead DBP:")
    study = st.text_input("Study:")
    email = st.text_input("Email:")
    study_status = st.text_input("Study Status:")

    if st.button("Submit"):
        # FastAPI endpoint
        backend_url = "http://localhost:8000/submit_info"
        
        payload = {
            "lead_dbp": lead_dbp,
            "study": study,
            "email": email,
            "study_status": study_status
        }
        
        try:
            response = requests.post(backend_url, params=payload)
            if response.status_code == 200:
                data = response.json()
                st.success(data.get("message", "Information saved!"))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to the backend: {e}")
    
    st.header("View Saved Data")
    if st.button("Load Data"):
        # Endpoint to get all records
        get_info_url = "http://localhost:8000/get_info"
        try:
            response = requests.get(get_info_url)
            if response.status_code == 200:
                data = response.json()  # This is a list of dicts
                if data:
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                else:
                    st.warning("No records found.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to the backend: {e}")

if __name__ == "__main__":
    main()
