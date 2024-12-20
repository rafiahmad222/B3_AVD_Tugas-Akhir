import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Memuat dataset
file_path = r'C:\Users\rafii\Downloads\AVD Akhir\cleaned_teleponseluler.csv'
data = pd.read_csv(file_path)

# Melihat beberapa baris awal dan informasi umum tentang dataset
data_head = data.head()
data_info = data.info()
data_summary = data.describe(include='all')

data_head, data_summary

# Membersihkan dataset

# Menghapus baris yang tampaknya menjadi header tambahan (misalnya baris dengan '2021.00' dll.)
cleaned_data = data[data['38 Provinsi'].notna()]

# Menghapus baris dengan nilai NaN di semua kolom
cleaned_data = cleaned_data.dropna(how='all')

# Mengubah nama kolom untuk lebih mudah diakses
cleaned_data.columns = ['Provinsi', 'Perkotaan_2021', 'Perkotaan_2022', 'Perkotaan_2023',
                        'Pedesaan_2021', 'Pedesaan_2022', 'Pedesaan_2023']

# Mengonversi kolom numerik ke tipe float
numeric_columns = ['Perkotaan_2021', 'Perkotaan_2022', 'Perkotaan_2023',
                   'Pedesaan_2021', 'Pedesaan_2022', 'Pedesaan_2023']
cleaned_data[numeric_columns] = cleaned_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Menghapus baris yang masih memiliki nilai kosong (jika ada)
cleaned_data = cleaned_data.dropna()

# Menampilkan data yang telah dibersihkan
cleaned_data_head = cleaned_data.head()
cleaned_data_info = cleaned_data.info()

cleaned_data_head, cleaned_data_info

# Menyimpan data yang sudah dibersihkan ke file CSV baru
cleaned_file_path = r'C:\Users\rafii\Downloads\AVD Akhir\cleaned_teleponseluler_v2.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

# Reloading the new dataset for analysis
dataset_v2 = pd.read_csv(cleaned_file_path)

# Displaying the first few rows of the dataset to confirm the structure
print(dataset_v2.head())

# Data untuk tahun 2021
X_2021 = dataset_v2[['Perkotaan_2021']]
y_2021 = dataset_v2['Pedesaan_2021']

# Regresi linier untuk tahun 2021
model_2021 = LinearRegression()
model_2021.fit(X_2021, y_2021)

# Data untuk tahun 2022
X_2022 = dataset_v2[['Perkotaan_2022']]
y_2022 = dataset_v2['Pedesaan_2022']

# Regresi linier untuk tahun 2022
model_2022 = LinearRegression()
model_2022.fit(X_2022, y_2022)

# Koefisien regresi, intercept, dan R² untuk kedua model
results_2021 = {
    "Slope": model_2021.coef_[0],
    "Intercept": model_2021.intercept_,
    "R_squared": model_2021.score(X_2021, y_2021)
}

results_2022 = {
    "Slope": model_2022.coef_[0],
    "Intercept": model_2022.intercept_,
    "R_squared": model_2022.score(X_2022, y_2022)
}

print(results_2021, results_2022)

# Visualisasi hasil regresi untuk tahun 2021
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_2021, y_2021, color='blue', label='Actual Data')
plt.plot(X_2021, model_2021.predict(X_2021), color='red', label='Regression Line')
plt.title('Linear Regression for 2021')
plt.xlabel('Perkotaan 2021')
plt.ylabel('Pedesaan 2021')
plt.legend()

# Visualisasi hasil regresi untuk tahun 2022
plt.subplot(1, 2, 2)
plt.scatter(X_2022, y_2022, color='green', label='Actual Data')
plt.plot(X_2022, model_2022.predict(X_2022), color='red', label='Regression Line')
plt.title('Linear Regression for 2022')
plt.xlabel('Perkotaan 2022')
plt.ylabel('Pedesaan 2022')
plt.legend()

plt.tight_layout()
plt.show()