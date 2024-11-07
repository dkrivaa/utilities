import streamlit as st


# Dialog for pdf_split_view - if uploaded file is only one page
@st.dialog('Error')
def one_page_dialog():
    st.info('The uploaded file cannot be split (only 1 page). Please upload another file')
    next_step = st.button('Go back')
    if next_step:
        del st.session_state['uploaded_file']
        st.rerun()


# Dialog for pdf_split_view - to download the files split up from uploaded file
@st.dialog('Download Files')
def download_dialog():
    # Provide download buttons for each split file
    for pdf_stream, filename in st.session_state['split_files']:
        st.download_button(
            label=f"Download {filename}",
            data=pdf_stream,
            file_name=filename,
            mime="application/pdf"
        )