import streamlit as st
from utf8_functions import detect_encoding, encode_utf8


st.title('UTF-8 - Detect and change to UTF-8')
st.write('---')

uploaded_file = st.file_uploader('Upload CSV file to check', type=['csv'], )

# Detect original encoding
if uploaded_file:
    # st.session_state['uploaded_file'] = uploaded_file.read()
    encoding = detect_encoding(uploaded_file)
    st.write(f'The original encoding of the uploaded file: **:blue[{encoding}]**')

    if encoding != 'utf-8':
        change_encoding = st.button('Change encoding to UTF-8')

        if change_encoding:
            file_stream = encode_utf8(uploaded_file, encoding)

            if file_stream:
                # Provide a download button for the merged PDF
                st.download_button(
                    label="Download utf-8 encoded csv",
                    data=file_stream,
                    file_name="output_utf8.csv",
                    mime="text/csv"
                )

