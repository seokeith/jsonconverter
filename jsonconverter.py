import streamlit as st
import pandas as pd
import json
import csv
from io import StringIO

def convert_json_to_csv(uploaded_file):
    # Read the uploaded JSON data
    uploaded_data = uploaded_file.getvalue().decode('utf-8')
    data = json.loads(uploaded_data)
    
    # Convert to DataFrame for easy CSV conversion
    df = pd.DataFrame(data)
    
    # Convert DataFrame to CSV
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()

# Streamlit app
st.title('JSON to CSV Converter')

uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

if uploaded_file:
    try:
        csv_data = convert_json_to_csv(uploaded_file)
        st.success('Conversion successful!')
        
        # Provide download link for CSV
        st.download_button(label="Download CSV", data=csv_data, file_name='converted.csv', mime='text/csv')
    
    except Exception as e:
        st.error(f'Error: {e}')

