
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard Analisis Polusi Udara - Stasiun Aotizhongxin')

# Load dataset
df = pd.read_csv('PRSA_Data_Aotizhongxin_20130301-20170228 affriyanto.csv')

# Preprocessing ringan
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df['year'] = df['datetime'].dt.year

# Sidebar interaktif
st.sidebar.header("Filter Data")
year_selected = st.sidebar.selectbox('Pilih Tahun', sorted(df['year'].unique()))

# Filter berdasarkan tahun
filtered_df = df[df['year'] == year_selected]

# Visualisasi 1: Tren PM2.5 sepanjang tahun terpilih
st.subheader(f"Tren PM2.5 di Tahun {year_selected}")
fig, ax = plt.subplots(figsize=(10,5))
filtered_df.groupby(filtered_df['datetime'].dt.month)['PM2.5'].mean().plot(marker='o', ax=ax)
ax.set_xlabel('Bulan')
ax.set_ylabel('PM2.5')
ax.set_title(f'Rata-rata PM2.5 per Bulan di Tahun {year_selected}')
st.pyplot(fig)

# Visualisasi 2: Hubungan Suhu dengan PM2.5
st.subheader(f"Hubungan Suhu dan PM2.5 di Tahun {year_selected}")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.scatterplot(data=filtered_df, x='TEMP', y='PM2.5', ax=ax2)
ax2.set_title(f'Hubungan Suhu dan PM2.5 - Tahun {year_selected}')
st.pyplot(fig2)
