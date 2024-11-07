import streamlit as st


home_page = st.Page(
    page='views/home_view.py',
    title='Home',
    default=True
)

pdf_merge_page = st.Page(
    page='views/pdf_merge_view.py',
    title='Merge PDFs'
)

pdf_split_page = st.Page(
    page='views/pdf_split_view.py',
    title='Split PDF'
)

pdf_from_image_page = st.Page(
    page='views/pdf_from_image_view.py',
    title='PDF from images'
)

pdf_from_pptx_page = st.Page(
    page='views/pdf_from_pptx_view.py',
    title='PDF from pptx'
)

utf8_page = st.Page(
    page='views/utf8_view.py',
    title='Encode CSV as UTF-8'
)

pg = st.navigation(pages={
    'Home': [home_page,],
    'PDF': [pdf_merge_page, pdf_split_page, pdf_from_image_page, pdf_from_pptx_page],
    'UTF-8': [utf8_page],
})

pg.run()
