import streamlit as st
import pandas as pd

df = pd.read_csv('spotify.csv')

df.set_index('Track', inplace=True)
st.line_chart(df[df['Stream']> 1000000000]['Stream'])

df
