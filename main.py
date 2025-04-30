from add_user import add_user
from face_recognizer import recognize_face
from log_writer import log_access

def main():
    while True:
        print("\n--- Yüz Tanıma Sistemi ---")
        print("1. Yeni Kullanıcı Kaydı")
        print("2. Yüz Tanıma ve Giriş Kontrolü")
        print("3. Çıkış")

        choice = input("Bir seçenek girin (1/2/3): ")

        if choice == '1':
            name = input("Kullanıcının adını girin: ")
            if name.strip() == "":
                print("İsim boş olamaz.")
                continue
            add_user(name)

        elif choice == '2':
            result = recognize_face()
            log_access(result)

        elif choice == '3':
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
