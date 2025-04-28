# Projek-analisa-data-final-
Projek analisa data full revisi 

# :bar_chart: Dashboard Analisis Kualitas Udara (PM2.5)

Sebuah aplikasi Streamlit sederhana untuk menganalisis kualitas udara berdasarkan kadar PM2.5 dari berbagai lokasi di Beijing.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://affriyanto-dashboardprojekanalisadata.streamlit.app/)

---

### 📂 Fitur

- Analisis deskriptif data PM2.5 harian dan bulanan
- Visualisasi interaktif menggunakan Plotly
- Pemfilteran berdasarkan stasiun pemantauan
- Klasifikasi kualitas udara (baik, sedang, buruk)

---

### 🚀 Jalankan di Lokal

1. Clone repo ini:
   ```bash
   git clone https://github.com/affriyanto/dashboardprojekanalisadata.git
   cd dashboardprojekanalisadata
   ```

2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

---

### 📊 Dataset

Dataset yang digunakan adalah kumpulan data kualitas udara (PM2.5) dari beberapa lokasi di Beijing dalam kurun waktu 2013–2017. File tersedia di repo ini dalam format `.csv`.

---

### 📦 Struktur Folder

```
.
├── app.py                  # File utama Streamlit
├── requirements.txt        # Daftar library yang dibutuhkan
├── data/                   # Folder dataset
│   └── PRSA_data.csv
├── README.md               # Dokumentasi proyek
```

---

### 📎 Catatan Tambahan

- Pastikan file dataset berada di folder yang sama atau sesuaikan path-nya di `app.py`.
- Aplikasi ini cocok untuk menunjukkan dampak polusi udara di berbagai musim/lokasi.
