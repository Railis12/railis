# 1.uzdevums
gram={
    "Sprīdītis":"Anna Brigadere",
    "Karlsons, kas dzīvo uz jumta":"Astrīda Lindgrēna",
    "grāmata": "Cilvēks, kas smejas""Viktors Igo",
    "Zaudētās tiesības":"Aspāzija",
}
x = gram["grāmata"]
print(x)
# 2.uzdevums
cities = {
    "Rīga": 632000,
    "Liepāja": 69000,
    "Daugavpils": 82000
}
cities["Rīga"] = 631000
print (cities)
# 3. uzdevums
mas={
    "BMW":250,
    "Fiat":210,
    "Skoda":270,
}
mas["Tesla"] = 250
print (mas)
# 4. uzdevums
skol={
    "Jānis":7,
    "Lāsma":6,
    "Miks":8,
    "Reinis":4, 
}
if "Ilze" in skol:
    print(skol.values("Ilze"))
else:
    print("Ilze nav vardnīcā")
# 5. uzdevums
vard={
    "Piens":2,
    "Maize":1,
    "Kafija":3,
    "Lasis":5,
    "Kefīrs":6,
}
for i in vard.values():
    print(vard.values())
for i in vard.keys():
    print(vard.keys())
#6. uzdevums
vardi={
    "Ritvars":26,
    "Ainis":74,
    "Kristians":17,
}
vardi.pop("Ainis")
print(vardi)

