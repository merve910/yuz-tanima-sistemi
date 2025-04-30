import csv
from datetime import datetime
import os

LOG_FILE = "logs/access_log.csv"

# Klasör yoksa oluştur
os.makedirs("logs", exist_ok=True)

# Dosya yoksa başlıkla oluştur
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Tarih-Saat", "Kullanıcı"])

def log_access(user_name):
    """Kişi bilgisini tarih-saat ile CSV'ye yazar."""
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_name])
    print(f"Giriş kaydedildi: {user_name}")