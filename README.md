yüz Tanıma Sistemi 

Bu proje **PyCharm** ortamında geliştirilmiştir.  
IDE: PyCharm  
Dil: Python  
Kütüphaneler: OpenCV, face_recognition, numpy

 Özellikler

- Kullanıcı kaydı (kamera üzerinden fotoğraf alınarak)
- Yüz tanıma ve eşleştirme
- Giriş bilgilerini CSV dosyasına kaydetme
- Modüler yapı: her işlem ayrı bir `.py` dosyasında

 Dosya Yapısı

- `add_user.py` → Yeni kullanıcı kaydı
- `face_recognizer.py` → Yüz tanıma işlemi
- `log_writer.py` → Girişlerin CSV dosyasına yazılması
- `main.py` → Tüm modüllerin birleştirildiği ana dosya
