import streamlit as st

from pdf_functions import pdf_from_pptx

st.title('PDF - Make PDF from images')
st.write('---')

pptx_file = st.file_uploader('Upload PowerPoint Presentation for PDF', type=['pptx', ])

if pptx_file:
    pdf_stream = pdf_from_pptx(pptx_file)

    st.write('---')

    next_step = st.button('Make PDF')
    if next_step:
        # Provide a download button for the merged PDF
        st.download_button(
            label="Download PDF",
            data=pdf_stream,
            file_name="pptx.pdf",
            mime="application/pdf"
        )
