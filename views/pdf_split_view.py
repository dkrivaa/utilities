import streamlit as st

from pdf_functions import split_file, get_page_count
from dialogs import one_page_dialog, download_dialog


def remove_split_files():
    if 'show_download_buttons' in st.session_state:
        st.session_state['show_download_buttons'] = False


if 'show_download_buttons' not in st.session_state:
    st.session_state['show_download_buttons'] = False

st.title('PDF - Split PDF file')
st.write('---')

original_file = st.file_uploader('Upload file to split', type=['PDF'], key='uploaded_file')
if original_file:
    st.session_state['original_file'] = original_file.read()
    with st.container(border=True):
        page_count = get_page_count(st.session_state['original_file'])
        if page_count == 1:
            one_page_dialog()
        elif page_count > 1:
            st.subheader('Number of output files')
            number_files = st.number_input(
                label='Number of output files',
                min_value=2,
                max_value=page_count,
                value=2,
                label_visibility='hidden',
            )
            st.write('---')
            # Dynamically generate 'from' and 'to' inputs for each output file
            st.subheader('Define page splits')
            page_ranges = []

            for i in range(number_files):
                col1, col2 = st.columns(2)
                from_page = col1.number_input(
                    label=f"File {i + 1} - From page",
                    min_value=1,
                    max_value=page_count,
                    value=(i * page_count // number_files) + 1,
                )
                to_page = col2.number_input(
                    label=f"File {i + 1} - To page",
                    min_value=1,
                    max_value=page_count,
                    value=((i + 1) * page_count // number_files),
                )
                page_ranges.append((from_page, to_page))

            split_step = st.button('Continue')

            if split_step:
                st.session_state['split_files'] = split_file(page_ranges)
                st.session_state['show_download_buttons'] = True

        if 'split_files' in st.session_state and st.session_state['show_download_buttons']:

            download_dialog()
            st.session_state['show_download_buttons'] = False


