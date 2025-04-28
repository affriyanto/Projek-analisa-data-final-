
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Dashboard Analisis Polusi Udara - Stasiun Aotizhongxin')

# Load dataset dengan error handling
try:
    df = pd.read_csv('PRSA_Data_Aotizhongxin_20130301-20170228 affriyanto.csv')
except FileNotFoundError:
    st.error('Dataset tidak ditemukan. Pastikan file CSV sudah di-upload dan nama file sudah benar.')
    st.stop()
except Exception as e:
    st.error(f'Terjadi kesalahan saat membaca dataset: {e}')
    st.stop()

# Preprocessing ringan
try:
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df['year'] = df['datetime'].dt.year
except Exception as e:
    st.error(f'Gagal memproses datetime: {e}')
    st.stop()

# Sidebar interaktif
st.sidebar.header("Filter Data")
try:
    year_selected = st.sidebar.selectbox('Pilih Tahun', sorted(df['year'].unique()))
    filtered_df = df[df['year'] == year_selected]
except Exception as e:
    st.error(f'Gagal membuat filter sidebar: {e}')
    st.stop()

# Visualisasi 1: Tren PM2.5 sepanjang tahun terpilih
st.subheader(f"Tren PM2.5 di Tahun {year_selected}")
try:
    fig, ax = plt.subplots(figsize=(10,5))
    filtered_df.groupby(filtered_df['datetime'].dt.month)['PM2.5'].mean().plot(marker='o', ax=ax)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('PM2.5')
    ax.set_title(f'Rata-rata PM2.5 per Bulan di Tahun {year_selected}')
    st.pyplot(fig)
except Exception as e:
    st.error(f'Gagal menampilkan tren PM2.5: {e}')

# Visualisasi 2: Hubungan Suhu dengan PM2.5
st.subheader(f"Hubungan Suhu dan PM2.5 di Tahun {year_selected}")
try:
    fig2, ax2 = plt.subplots(figsize=(8,5))
    sns.scatterplot(data=filtered_df, x='TEMP', y='PM2.5', ax=ax2)
    ax2.set_title(f'Hubungan Suhu dan PM2.5 - Tahun {year_selected}')
    st.pyplot(fig2)
except Exception as e:
    st.error(f'Gagal menampilkan hubungan suhu dan PM2.5: {e}')
