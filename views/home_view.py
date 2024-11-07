import streamlit as st

from assets.images import get_image

st.title('Utilities App')
st.write('---')
with st.container(border=True):
    tab1, tab2, tab3 = st.tabs(['PDF', 'Encryption', 'To Come'])
    with tab1:
        st.header('PDF - Merge & Split')
        st.image(get_image('https://pics.freeicons.io/uploads/icons/png/15519179861536080156-64.png'))
        col1, col2, col3 = st.columns([0.5, 2, 5.5], vertical_alignment='center')
        with col1:
            st.image(get_image('https://pics.freeicons.io/uploads/icons/png/5809905011543238858-32.png'))
            st.image(get_image('https://pics.freeicons.io/uploads/icons/png/5809905011543238858-32.png'))
            st.image(get_image('https://pics.freeicons.io/uploads/icons/png/5809905011543238858-32.png'))
        with col2:
            st.page_link('views/pdf_merge_view.py')
            st.page_link('views/pdf_split_view.py')
            st.page_link('views/pdf_from_image_view.py')
    with tab2:
        st.header('Decoding / Encoding')
        st.image(get_image('https://pics.freeicons.io/uploads/icons/png/12013790981678978252-64.png'))
        col1, col2, col3 = st.columns([0.5, 2, 5.5], vertical_alignment='center')
        with col1:
            st.image(get_image('https://pics.freeicons.io/uploads/icons/png/5809905011543238858-32.png'))
        with col2:
            st.page_link('views/utf8_view.py')
    with tab3:
        st.header('Under Construction')
        st.image(get_image('https://pics.freeicons.io/uploads/icons/png/7989827331599996561-64.png'))

