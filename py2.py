aa= {
"Jānis":9,
"Miks":4,
"Lasma":2,
"Alehandro":5,
"Rihards":10,
}
x=aa.keys()
print(x)
y=aa.values()
print(y)
z=aa.get("Alehandro")
print(z)
aa["Liāna"]=7
print(aa)
aa.pop("Liāna")
print(aa)
if "Miks" in aa:
    print("jā")
else:
    print("ne")