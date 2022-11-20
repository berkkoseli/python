

k=[]

file=open("sample.txt","w")

try:

sayi=int(input("Çalışan sayısını giriniz."))


for i in range(sayi):
    isim=input()
    soyisim=input()
    maas=input()
    k.append(f"{isim} {soyisim} - {maas}")

for i in range(sayi):
    file.write(k[i])

file.close()