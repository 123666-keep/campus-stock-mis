from pathlib import Path

import streamlit as st

st.set_page_config(page_title='该订多少 · 校园短保商品MIS', page_icon='🧺', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
[data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none}
[data-testid="stMainBlockContainer"] {max-width:100%;padding:0}
[data-testid="stMain"] {overflow:hidden}
iframe {display:block;border:0;width:100%;height:100dvh}
</style>''', unsafe_allow_html=True)
page = Path(__file__).resolve().parent / 'cloud' / 'web' / 'index.html'
if not page.is_file():
    st.error('缺少云端页面，请先运行 python cloud/build_cloud.py 并上传 cloud/web/index.html。')
    st.stop()
initial_hash = '#customer' if st.query_params.get('view') == 'customer' or st.query_params.get('demo') == 'demand' else '#dashboard'
initial_search = '?demo=demand' if st.query_params.get('demo') == 'demand' else ''
content = page.read_text(encoding='utf-8').replace('__MIS_INITIAL_HASH__', initial_hash).replace('__MIS_INITIAL_SEARCH__', initial_search)
st.iframe(content, height=980)
