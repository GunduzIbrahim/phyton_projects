defkullanici= "Ibrahim"
defparola="1234"

while(True):
    kullanici=input("Kullanici adi : ")
    parola=input("Parola : ")
    if ((kullanici == defkullanici) and (parola == defparola)):
        print("Hosgeldiniz..", kullanici)
        break
    elif ((kullanici != defkullanici) and (parola == defparola)):
        print("Kulanici adi yanlis girildi..")
        
    elif ((kullanici == defkullanici) and (parola != defparola)):
        print("Sifre yanlis girildi..")
        print("Sifrenizi degistirmek ister misiniz? (E/H) : ")
        cevap = input()
        if (cevap == "E"):
            print("Yeni parolayi giriniz..:")
            yeniparola = input("Yeni parola : ")
            defparola = yeniparola
            print("Lutfen bekleyiniz..")
            print("Parola basariyla degistirildi..")
    else:
        print("Tekrar deneyiniz..")



        