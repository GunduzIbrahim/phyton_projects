faktoriyel = 1

while True:
    sayi = int(input("Lutfen negatif olmayan bir sayi giriniz : "))
    if sayi<0:
        print("Negtif sayi girdiniz..")
    else:
        for i in range(1,sayi+1):
            faktoriyel*=i
        
        print("Faktoriyel :",faktoriyel)
        break
