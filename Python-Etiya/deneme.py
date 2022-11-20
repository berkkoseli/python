file=open("sample.txt","w")

sayi=input(print("Çalışan sayısını giriniz."))
k=[]

for i in range(sayi):
    isim=input()
    soyisim=input()
    maas=input()
    k.append(f"{isim} {soyisim} - {maas}")

for i in range(sayi):
    file.writelines(i)
