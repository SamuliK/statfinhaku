import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Tilastokeskuksen taulukkohaku",
)

st.title('Tilastokeskuksen taulukkohaku')

search_term = st.text_input('Anna hakusana(t):')

if search_term:
    modded_search = ' '.join(search_term.split())
    modded_search = search_term.replace(" ", " AND ")
    url = f'https://statfin.stat.fi/PXWeb/api/v1/fi/StatFin?query={modded_search}'
    response = requests.get(url)
    data = json.loads(response.text)
    
    #base_url = 'https://statfin.stat.fi/PXWeb/api/v1/fi/StatFin'
    base_url = "https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__"
    
    st.markdown("""
        <style>
            a {
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)
    
    for result in sorted(data, key=lambda x: x['title']):
        path = result['path'][1:]
        id = result['id']
        title = result['title']
        result_url = f'{base_url}{path}/{id}'
        st.markdown(f'[{title}]({result_url})', unsafe_allow_html=True)
