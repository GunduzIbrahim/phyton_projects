import random

kullanici_skor = 0
bilgisayar_skor = 0

while True:
    kullanici_secimi = str(input("Lutfen seciminizi yapiniz..: (TAS, KAGIT, MAKAS)"))
    if kullanici_secimi.isalpha():
        
        kullanici_secimi = kullanici_secimi.upper().strip()
        secim_listesi = ["TAS", "KAGIT", "MAKAS"]
        bilgisyar_secimi = random.choice(secim_listesi) # secim_listesi isimli listeden rastgele bir eleman sectirip bilgisayar_secimi degiskenine atiyoruz.

        # secimleri ekrana yazdiriyoruz.
        print(f"Sizin seciminiz : {kullanici_secimi}")
        print(f"Bilgisyarin secimi : {bilgisyar_secimi}")


        # bu satirdan sonra 38. satira kadar kullanicinin secimi ile bilgisyar icin rastgele uretilen secim arasinda degerlendirmeler yapiyoruz.
        if kullanici_secimi == bilgisyar_secimi: # secimler ayni olursa
            print(f"Bilgisayar ile ayni secimi yaptiniz.. {kullanici_secimi}")
        elif kullanici_secimi == "TAS": # kullanici tas'i secerse ve bilgisayar makas'i secerse
            if bilgisyar_secimi == "MAKAS":
                print("Tebrikler TAS, MAKAS'ı kirar..!")
                kullanici_skor += 1
            else: 
                print(f"Uzgunum {bilgisyar_secimi}, TAŞ'ı sarar..!")
                bilgisayar_skor += 1
        elif kullanici_secimi == "KAGIT": # kullanici kagit'i secerse ve bilgisayar tas'i secerse
            if bilgisyar_secimi == "TAS":
                print("Tebrikler KAĞIT, TAŞ'ı sarar..!")
                kullanici_skor += 1
            else:
                print(f"Uzgunum {bilgisyar_secimi}, KAĞIT'ı keser..!")
                bilgisayar_skor += 1 
        elif kullanici_secimi == "MAKAS": # kullanici makas'i secerse ve bilgisayar kagit'i secerse
            if bilgisyar_secimi == "KAGIT":
                print("Tebrikler MAKAS, KAĞIT'ı keser..!")
                kullanici_skor += 1
            else:
                print(f"Uzgunum {bilgisyar_secimi}, MAKAS'ı kırar..!")
                bilgisayar_skor +=1
    else:
        print("Lutfen sadece harf girisi yapiniz..") 
              
    cevap = input("Tekrar oynamak ister misiniz? (E/H)") # oyunun devam edip etmeyecegi ile ilgili karar bekliyoruz.
    if cevap.upper() != "E": # cevap buyuk harf ile bile verilse .lower() metodu ile cevap harfini kucuk harfe ceviriyoruz.
         break
    

# oyunun sonucunu ve skoru ekrana yazdiriyoruz
print("Oyun sonucu : ")
print(f"Kullanici  : {kullanici_skor}")
print(f"Bilgisayar : {bilgisayar_skor}")

if kullanici_skor > bilgisayar_skor:
    print("!!!...TEBRIKLER KAZANDINIZ...!!!")
elif kullanici_skor == bilgisayar_skor:
    print("...OYUN BERABERE...")
else:
    print("..UZGUNUM KAYBETTINIZ..")   


