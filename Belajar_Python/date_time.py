# import library datetime

import datetime as dt
tahun = int(input("masukan tahun \t"))
bulan = int(input("masuan bulan \t"))
hari = int(input("masukan hari \t"))

kumpulans = dt.date(tahun,bulan,hari)

print(f"hari itu hari {kumpulans:%A}")
hari_ini = dt.date.today()
umur = hari_ini -kumpulans
umur_tahun = umur.days /365


print(umur_tahun)
print(umur)