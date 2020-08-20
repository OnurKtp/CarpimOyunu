from random import randint

""" Çarpma oyunu"""

print("-" * 50)
print("\t\tOYUN BAŞLIYOR")
print("-" * 50, "\n")

#Yukarıda oyun için giriş ekranı yaptım

def carpim(i, j, r):        #i,j,r parametreleri alan bir carpim fonksiyonu oluştur
    if r !="-1":
        result = str(i * j)    #eğer r parametresi "-1" değilse i ve j parametrelerini çarpıp stringe dönmüş değerini result değişkenine ata
        if result == r:
            print("\t\t****Doğruuuu****")
        else:
            print("\t!!! Yanlış yaptın. Doğru cevap %s " % result)
    else:
        secim()
#Eğer kullanıcının girdiği değer çarpımda atanan result değerine eşitse doğru, eşit değilse yanlış yazısını bas ekrana
#Eğer r -1'e eşit ise secim fonksiyonunu çağır.

def basla(rng1, rng2):      #rng1, rng2 parametreleri alan bir basla fonksiyonu oluştur
    if rng1 > 10:
        x = 10
    else:
        x = 5

    for i in range(0, x):
        for j in range(0, x):
            sayi1 = randint(rng1, rng2)
            sayi2 = randint(rng1, rng2)
            print("_" *50, "\n")
            print("\t%d x %d kaça eşittir? (Çıkış= -1)" % (sayi1, sayi2))
            sonuc = input("sonuc >> ")
            carpim(sayi1, sayi2, sonuc)

            if j == 4:
                print("\n *-- Bu bölüm bitti bir üst bölüme geçebilirsiniz --*\n")
                secim()


def secim():
    print("Hangi seviyeden başlamak istiyorsunuz? (Çıkış = -1) \n")
    print(" 1 - Kolay")
    print(" 2 - Orta")
    print(" 3 - Zor")
    print(" 4 - Çok Zor\n")

    svy = input(" >> ")

    if svy == "1":
        basla(1, 6)

    elif svy == "2":
        basla(6, 12)

    elif svy == "3":
        basla(12, 25)

    elif svy == "4":
        basla(25, 100)

    else:
        exit(0)

if __name__ == '__main__':
    secim()