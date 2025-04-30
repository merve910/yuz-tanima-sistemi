import cv2
import os

def add_user(user_name):
    """Yeni kullanıcıyı kaydeder."""
    os.makedirs("known_faces", exist_ok=True)
    save_path = f"known_faces/{user_name}.jpg"

    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Kamera açılamadı, bağlantıyı kontrol edin.")
        return

    print(f"{user_name}, lütfen kameraya bakın...")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Görüntü alınamadı.")
            break

        cv2.imshow("Yüz Kaydı (Kaydetmek için 's', iptal için 'q')", frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            cv2.imwrite(save_path, frame)
            print(f"{user_name} başarıyla kaydedildi! Dosya: {save_path}")
            break
        elif key & 0xFF == ord('q'):
            print("Kayıt iptal edildi.")
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        name = input("Kayıt edilecek kullanıcının adını girin (Çıkmak için 'q'): ")
        if name.lower() == 'q':
            print("Kayıt işlemi sonlandırıldı.")
            break
        elif name.strip() == "":
            print("İsim boş olamaz.")
            continue
        else:
            add_user(name)
