##! Döngüleri araştırmanız,
#! Kullanıcının girdiği sayı kadar vize-final sınavları girilebilmesi beklenmektedir. 
# Kullanıcı kaç dersten geçip kaç dersten kaldığına görebilmeli


n = int(input("kullanıcı sayısını giriniz: "))

for i in range(1,n+1):
    vizeGrade = float(input())
    finalGrade = float(input())
    ortalama = float(vizeGrade*0.4 + finalGrade*0.6 )
    if(ortalama<50):
    print(f'{vizeGrade}  {finalGrade}  {ortalama}')

vizeGrade = 0.0
finalGrade=0.0

print("Dersinizin kaç tane vizesi var?")
v=int(input())
print("Dersinizin kaç tane finali var?")
k=int(input())

for i in range(v):
    vizeGrade+=float(input())

vizeGrade=vizeGrade/v




vizeGrade = float(input())
finalGrade = float(input())
ortalama = int(vizeGrade*0.4 + finalGrade*0.6)

print(ortalama)

if (ortalama<=49):
    print("FF")
elif (ortalama<=60):
    print("DD")
elif (ortalama<=70):
    print("CC")
elif (ortalama<=80):
    print("BB")
else:
    print("AA")