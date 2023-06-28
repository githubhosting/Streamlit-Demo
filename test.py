import streamlit as st
import pandas as pd
import numpy as np

st.write('''## Welcome to Lost and Found!''')

st.write('''#### Please select an option from the sidebar to get started.''')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)
