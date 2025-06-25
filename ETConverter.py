import pandas as pd # type: ignore
from datetime import datetime, timedelta

# Excel dosyasını oku
df = pd.read_excel('veriler.xlsx')

# Epoch sütunu adı
epoch_col = 'epoch_time'

# Epoch'tan tarih oluştur (varsa)
df['tarih'] = pd.to_datetime(df[epoch_col], unit='ms', errors='coerce')

# Bugünün tarihi
bugun = pd.Timestamp.now()

# 2 gün önceki tarih
iki_gun_once = bugun - timedelta(days=2)

# Filtre koşulu: tarih boş olanlar veya 2 günden eski olanlar
filtreli_df = df[(df['tarih'].isna()) | (df['tarih'] < iki_gun_once)].copy()

# Excel'deki gerçek satır numarasını bul (başlık 1. satırda)
filtreli_df['satir_numarasi'] = filtreli_df.index + 2

# Sonuçları yeni bir Excel dosyasına yaz
filtreli_df.to_excel('veriler_donusturulmus.xlsx', index=False)

print("Filtrelenmiş veriler 'veriler_donusturulmus.xlsx' dosyasına yazıldı.")
