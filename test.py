import streamlit as st

st.write('''## Welcome to Lost and Found!''')

st.write('''#### Please select an option from the sidebar to get started.''')

st.sidebar.write('''## Options''')

option = st.sidebar.selectbox(
    'What would you like to do?',
    ('Home', 'Lost', 'Found', 'About Us')
)

if option == 'Home':
    st.selectbox("what category does your item fall under?", ("Electronics", "Clothing", "Accessories", "Other"))
