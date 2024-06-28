import streamlit as st 
import pandas as pd 

# baca dataframe dari file csv 
df_house_clean = pd.read_csv('house_clean.csv')

def main() : 
    st.header('Halaman Streamlit Febrian Bahari Adi')
    st.subheader('This is SubHeader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Phytagorean Equation : ')
    st.latex('c^2 = a^2+b^2')
    st.write('Contoh dataframe')
    st.dataframe(df_house_clean)

if __name__ == '__main__' : 
    main()
