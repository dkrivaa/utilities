import streamlit as st

from pdf_functions import merge_files

st.title('PDF - Merge PDF files')
st.write('---')

uploaded_files = st.file_uploader('Upload PDF files to merge', type=['PDF'], accept_multiple_files=True)

if uploaded_files:
    merge_button = st.button('Merge files')
    if merge_button:
        pdf_stream = merge_files(uploaded_files)

        # Provide a download button for the merged PDF
        st.download_button(
            label="Download Merged PDF",
            data=pdf_stream,
            file_name="merged_output.pdf",
            mime="application/pdf"
        )
