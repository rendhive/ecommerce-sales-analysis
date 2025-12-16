# E-Commerce Sales Analysis

## Deskripsi

Project ini bertujuan untuk menganalisis dataset penjualan e-commerce guna menemukan **tren penjualan**, **produk terlaris**, serta **estimasi/prediksi pendapatan** berbasis data historis. Analisis difokuskan pada pembersihan data, eksplorasi data (EDA), visualisasi, dan penarikan **insight bisnis** yang dapat ditindaklanjuti.

Dataset yang digunakan: **Kaggle – E-Commerce Sales Dataset** (disimpan dalam format CSV).

---

## Tujuan Project

* Memahami pola penjualan dari waktu ke waktu (harian/bulanan).
* Mengidentifikasi produk dan kategori dengan performa terbaik.
* Mengukur kontribusi pendapatan per produk/kategori.
* Memberikan insight bisnis untuk strategi penjualan dan stok.

---

## Struktur Project

```
ecommerce-sales-analysis/
│
├── data/
│   └── ecommerce_sales.csv
├── notebooks/
│   └── ecommerce_analysis.ipynb
├── scripts/
│   └── data_cleaning.py
├── README.md
└── requirements.txt
```

**Penjelasan folder:**

* `data/` : Menyimpan dataset mentah (CSV).
* `notebooks/` : Analisis utama menggunakan Jupyter Notebook (EDA, visualisasi, insight).
* `scripts/` : Script Python untuk data cleaning dan preprocessing.
* `requirements.txt` : Daftar dependency Python yang digunakan.

---

## Langkah Analisis

1. **Load Data**

   * Membaca dataset CSV menggunakan Pandas.
   * Melakukan pengecekan struktur data (shape, columns, data types).

2. **Data Cleaning & Preprocessing**

   * Menangani missing values.
   * Konversi kolom tanggal ke format `datetime`.
   * Membersihkan data duplikat.
   * Membuat kolom turunan (misalnya: `month`, `year`, `total_sales`).

3. **Exploratory Data Analysis (EDA)**

   * Analisis distribusi penjualan.
   * Analisis tren penjualan bulanan.
   * Identifikasi produk dan kategori terlaris.

4. **Aggregasi & Pivot Table**

   * `groupby()` untuk total penjualan per produk/kategori.
   * Pivot table untuk membandingkan performa antar periode.

5. **Visualisasi Data**

   * Line chart: tren penjualan waktu ke waktu.
   * Bar chart: produk/kategori terlaris.
   * Insight visual untuk mendukung keputusan bisnis.

6. **Insight Bisnis**

   * Menarik kesimpulan dari hasil analisis.
   * Rekomendasi berbasis data.

---

## Contoh Insight

* **Produk Terlaris**: Beberapa produk menyumbang sebagian besar pendapatan (prinsip Pareto 80/20).
* **Tren Penjualan Bulanan**: Terjadi peningkatan penjualan pada bulan-bulan tertentu (indikasi seasonality).
* **Kategori Paling Menguntungkan**: Fokus stok dan promosi dapat diarahkan ke kategori dengan margin dan volume tertinggi.

> Insight divisualisasikan dalam bentuk grafik (bar chart & line chart) di notebook.

---

## Cara Menjalankan Project

1. Clone repository ini:

   ```bash
   git clone <repo-url>
   cd ecommerce-sales-analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Buka file:

   ```
   notebooks/ecommerce_analysis.ipynb
   ```

---

## Skills yang Ditunjukkan

* **Pandas & NumPy**: Data cleaning dan transformasi data.
* **Matplotlib & Seaborn**: Visualisasi data.
* **Pivot Table & GroupBy**: Analisis agregasi.
* **Business Insight**: Interpretasi data untuk pengambilan keputusan.

---

## Catatan

Project ini cocok sebagai **portfolio Data Analyst (Remote / Internasional)** karena menunjukkan kemampuan end-to-end: dari data mentah hingga insight bisnis yang relevan.

---

## File Tambahan (Disarankan)

Di bawah ini adalah **konten siap pakai** untuk file utama lain di project ini.

---

### `scripts/data_cleaning.py`

```python
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # drop duplicates
    df.drop_duplicates(inplace=True)

    # handle missing values
    df.dropna(how="all", inplace=True)

    # date parsing
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['year'] = df['order_date'].dt.year
        df['month'] = df['order_date'].dt.month

    # total sales
    if {'quantity', 'price'}.issubset(df.columns):
        df['total_sales'] = df['quantity'] * df['price']

    return df


if __name__ == '__main__':
    df = load_data('data/ecommerce_sales.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('data/ecommerce_sales_clean.csv', index=False)
```

---

### `notebooks/ecommerce_analysis.ipynb` (Outline Isi Notebook)

```python
# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Data
df = pd.read_csv('../data/ecommerce_sales.csv')
df.head()

# 3. Data Cleaning
from datetime import datetime

df.drop_duplicates(inplace=True)
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['month'] = df['order_date'].dt.to_period('M')
df['total_sales'] = df['quantity'] * df['price']

# 4. Tren Penjualan Bulanan
monthly_sales = df.groupby('month')['total_sales'].sum()
monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.show()

# 5. Produk Terlaris
top_products = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', title='Top 10 Products by Sales')
plt.show()

# 6. Insight
# - Produk tertentu mendominasi revenue
# - Ada pola musiman di penjualan
```

---

### `requirements.txt`

```
pandas
numpy
matplotlib
seaborn
jupyter
