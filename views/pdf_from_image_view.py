import streamlit as st

from pdf_functions import pdf_from_image

st.title('PDF - Make PDF from images')
st.write('---')

image_files = st.file_uploader('Upload images for PDF', type=['jpg', 'jpeg', 'gif', ], accept_multiple_files=True)

if image_files:
    pdf_stream = pdf_from_image(image_files)

    st.write('---')

    next_step = st.button('Make PDF')
    if next_step:
        # Provide a download button for the merged PDF
        st.download_button(
            label="Download PDF",
            data=pdf_stream,
            file_name="image.pdf",
            mime="application/pdf"
        )
