# Langkah-Langkah Menjalankan Program
# 1. Memastikan Semua Perangkat Terpasang
Sebelum menjalankan kode, pastikan Anda memiliki pustaka Python berikut diinstal pada lingkungan Anda:
    pandas
    numpy
    matplotlib
    seaborn
    scikit-learn
# 2. Persiapan Dataset
Letakkan file dataset (cleaned_teleponseluler.csv) di lokasi yang ditentukan pada variabel file_path:
    file_path = r'C:\Users\rafii\Downloads\AVD Akhir\cleaned_teleponseluler.csv'
# 3. Memuat Dataset
Kode akan memuat dataset, menampilkan informasi awal, dan membersihkannya:
- Langkah awal: Menampilkan cuplikan data, ringkasan statistik, dan tipe kolom.
- Membersihkan data:
    Menghapus baris tidak relevan atau kosong.
    Mengubah nama kolom menjadi lebih mudah diakses.
    Mengonversi data numerik yang tidak konsisten.
# 4. 4. Menyimpan Dataset Bersih
Dataset yang sudah bersih akan disimpan kembali ke file CSV baru (cleaned_teleponseluler_v2.csv). Pastikan lokasi penyimpanan memiliki izin menulis.
# 5. Melakukan Regresi Linear 
a. Tahun 2021
1. Variabel independen adalah Perkotaan_2021, sedangkan variabel dependen adalah Pedesaan_2021.
2. Model ini menghasilkan:
- Slope (kemiringan): Menunjukkan perubahan Pedesaan untuk setiap perubahan unit pada Perkotaan.
- Intercept: Titik potong dengan sumbu Y.
- R² (Koefisien determinasi): Mengukur seberapa baik model menjelaskan variasi data.
b. Tahun 2022
Proses yang sama dilakukan untuk data tahun 2022 (Perkotaan_2022 dan Pedesaan_2022).
3. Model regresi linear dibangun menggunakan:
  model_2021 = LinearRegression()
  model_2021.fit(X_2021, y_2021)
# 6. Menganalisis Hasil
Setelah model regresi selesai:
- Koefisien (Slope & Intercept) serta nilai R² ditampilkan untuk analisis.
- Interpretasi:
- Nilai R² mendekati 1 menunjukkan hubungan yang kuat antara variabel independen dan dependen.
- Slope menggambarkan hubungan positif/negatif antara kedua variabel.
# 7. Membuat Visualisasi
Hasil regresi divisualisasikan menggunakan matplotlib:
- Plot data aktual sebagai titik (scatter plot).
- Tambahkan garis regresi untuk melihat kesesuaian model dengan data.
# 8. Menjalankan Kode
Jalankan kode di editor Python (misalnya, Jupyter Notebook, VS Code, atau PyCharm) atau di terminal menggunakan script .py. Pastikan untuk menyesuaikan jalur file dataset sesuai dengan lokasi Anda.
