import cv2
import face_recognition
import numpy as np
import os
from PIL import Image


def recognize_face():
    KNOWN_FACES_DIR = "known_faces"
    known_faces = []
    known_names = []

    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.startswith('.') or filename.lower() == "desktop.ini" or not filename.lower().endswith(
                ('.jpg', '.jpeg', '.png')):
            print(f"Atlanıyor (geçersiz dosya): {filename}")
            continue  # Geçersiz dosyaları atla

        image_path = os.path.join(KNOWN_FACES_DIR, filename)

        try:
            with Image.open(image_path) as img:
                img.verify()  # Resmin geçerli olup olmadığını kontrol et
        except (IOError, SyntaxError):
            print(f"Geçersiz resim dosyası atlanıyor: {filename}")
            continue  # Geçersiz dosyayı geç

        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_faces.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])
        else:
            print(f"Uyarı: {filename} içinde yüz bulunamadı.")

    # Kamera ile yüz tanıma işlemi
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Kamera açılamadı.")
        return "Kamera hatası"

    name = "Erişim reddedildi"
    face_detected = False

    while not face_detected:
        ret, frame = video_capture.read()
        if not ret:
            print("Görüntü alınamadı.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            best_match_index = np.argmin(face_distances) if matches else None

            if best_match_index is not None and matches[best_match_index]:
                name = known_names[best_match_index]
                face_detected = True
            else:
                face_detected = True

        for (top, right, bottom, left) in face_locations:
            color = (0, 255, 0) if name != "Erişim reddedildi" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Yüz Tanıma", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            name = "İşlem iptal edildi"
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return name


if __name__ == "__main__":
    result = recognize_face()
    print("Tanımlanan kişi:", result)
