# Birinci Aşama 3.1
# ____________________________________________ #
import random
import hashlib
import time

def GirisYapma(dosya):
    kullanciadi = input("Kullanici adi: ")
    sifre = input("Sifre: ")
    sayac = 0
    g = []
    giris = kullanciadi + " " + sifre
    with open(dosya) as file:
        g.append( file.read().splitlines())
    for i in range(DosyadakiSatirSayisi):
        if giris == g[0][i]:
            sayac+=1
            print("Giris basarili...")
            break;
        else:
            sayac=sayac
    if sayac <= 0:
        print("Giris basarisiz..")
        GirisYapma(dosya)

def SaltliGirisYapma(dosya):
    kullanciadi = input("Kullanici adi: ")
    sifre = input("Sifre: ")
    salt = input("Salt: ")
    sayac = 0
    g = []
    giris = kullanciadi + " " + sifre +" "+salt
    with open(dosya) as file:
        g.append( file.read().splitlines())
    for i in range(DosyadakiSatirSayisi):
        if giris == g[0][i]:
            sayac+=1
            print("Giris basarili...")
            break;
        else:
            sayac=sayac
    if sayac <= 0:
        print("Giris basarisiz..")
        SaltliGirisYapma(dosya)

def rasgele():
    SayiDizisi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(DosyadakiSatirSayisi):
        random.shuffle(SayiDizisi)
        b = SayiDizisi[0:5]
        Kimlikler = ''.join(b)
        return Kimlikler

dosya1=open("Password.txt","r")
lines=dosya1.readlines()
dizi1=[]
for x in lines:
    dizi1.append(x.split(' ')[2:3])
dosya1.close()

DosyadakiSatirSayisi = (int(len(lines)))

KimlikBasi = "BIL008-2020"
KimliklerDizisi=[]
for i in range(DosyadakiSatirSayisi):
    KimliklerDizisi.append(KimlikBasi + rasgele())
print("KimliklerDizisi -> ",KimliklerDizisi)

SifrelerListesi=[]
for i in range(DosyadakiSatirSayisi):
    SifrelerListesi.append(dizi1[i][0])
print("SifrelerListesi -> ",SifrelerListesi)

dosya2 = open('Veritaban1.txt',"w")
for i in range(DosyadakiSatirSayisi):
    dosya2.write(KimliklerDizisi[i]+" "+SifrelerListesi[i])
f=open("Password.txt","r")
lines=f.readlines()
dosya2.close()



#__________________________________________________________________________________________________________________________________#



# İkinci Aşama 3.2

HASH5Listesi = []
for i in range(DosyadakiSatirSayisi):
    Sifrelenmis = hashlib.md5(SifrelerListesi[i].encode())
    HASH5Listesi.append(Sifrelenmis.hexdigest())
print("HASH5 Algoritması ile sifrelenmis sifreler -> ",HASH5Listesi)

dosya3 = open('Veritaban2.txt',"w")
for i in range(DosyadakiSatirSayisi):
    dosya3.write(KimliklerDizisi[i]+" "+HASH5Listesi[i]+"\n")
dosya3.close()



#__________________________________________________________________________________________________________________________________#

# Üçüncü Aşama 3.3

dosya4 = open('Veritaban3.txt',"w")
Salt = "9ahd37dn4hd82jdlf753"
XORSifre=[]
def StringXOR(string1,string2):
    kod = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string1,string2))
    XORSifre.append(kod)

sha224cevirme = []
sha224= []
for i in range(DosyadakiSatirSayisi):
    StringXOR(SifrelerListesi[i],Salt)
    sha244cevirme = hashlib.sha224(XORSifre[i].encode())  #
    sha224.append(sha244cevirme.hexdigest())
    dosya4.write(KimliklerDizisi[i] + " " + sha224[i] + "\n")
print("XORSifre -> ",XORSifre)
print("SHA244 -> ",sha224)
dosya4.close()

#__________________________________________________________________________________________________________________________________#

# Dördüncü Aşama 3.4

RastgeleSalt=[]
def rasgele20():
    karisik = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(DosyadakiSatirSayisi):
        random.shuffle(karisik)
        b = karisik[0:20]
        kimlikler20 = ''.join(b)
        RastgeleSalt.append(kimlikler20)
dosya5 = open('Veritaban4.txt',"w")
rasgele20()
sha256cevirme = []
sha256= []
for i in range(DosyadakiSatirSayisi):
    StringXOR(sha224[i], RastgeleSalt[0])
    sha256cevirme = hashlib.sha256(XORSifre[i].encode())
    sha256.append(sha256cevirme.hexdigest())
    dosya5.write(KimliklerDizisi[i] + " " + sha256[i] +" "+RastgeleSalt[0]+"\n")
print("SHA256 -> ", sha256)
dosya5.close()

#__________________________________________________________________________________________________________________________________#

# Beşinci Aşama 3.5

dosya6 = open('Veritaban5.txt',"w")
rasgele20()
sha384cevirme = []
sha384= []
for i in range(DosyadakiSatirSayisi):
    StringXOR(sha256[i], RastgeleSalt[i])
    sha384cevirme = hashlib.sha384(XORSifre[i].encode())
    sha384.append(sha384cevirme.hexdigest())
    dosya6.write(KimliklerDizisi[i] + " " + sha384[i] +" "+RastgeleSalt[i]+"\n")
print("SHA384 -> ", sha384)
dosya6.close()

#__________________________________________________________________________________________________________________________________#
while(1):
    print("\n\n---- GIRIS MENUSU ----")
    print("\t1 - Veritaban1.txt")
    print("\t2 - Veritaban2.txt")
    print("\t3 - Veritaban3.txt")
    print("\t4 - Veritaban4.txt")
    print("\t5 - Veritaban5.txt")
    print("\t6 -\t- CIKIS -")


    try:
        secim=int(input("Seciminizi giriniz :"))
        print("Seciminiz -> ",secim)

        if secim == 1:
            GirisYapma("Veritaban1.txt")
            break
        elif secim == 2:
            GirisYapma("Veritaban2.txt")
            break
        elif secim == 3:
            GirisYapma("Veritaban3.txt")
            break
        elif secim == 4:
            SaltliGirisYapma("Veritaban4.txt")
            break
        elif secim == 5:
            SaltliGirisYapma("Veritaban5.txt")
            break
        elif secim == 6:
            print("Programdan cikiliyor..")
            time.sleep(1)
            print("Programdan cikis yapildi.")
            break
        else:
            print("===============================================================")
            print("! WARNING ! ----> Hatali giris.. Boyle bir .txt dosyasi yok")
            print("===============================================================")

    except ValueError:
        print("===================================================")
        print("! WARNING ! ----> Lutfen harf degil, sayi girin!")
        print("===================================================")