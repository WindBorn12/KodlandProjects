import random

karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
sifreuzunlugu = int(input("kac karakterli sifre olusturmak istiyorsunuz?"))
sifre = ""
for i in range(sifreuzunlugu):
    sifre += random.choice(karakterler)
    #yada
    #print(random.choice(karakterler), ends="")

print(sifre)