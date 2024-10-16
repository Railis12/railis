aa=["Janvāris", "Februāris", "Marta", "Aprīlis", "Maijs", "Jūnijs", "Jūlijs", "Augusts", "Septembris", "Oktobris", "Novembris", "Decembris"]
f = open("menesis10.txt", "w", encoding= "utf-8")
for i in aa:
    f.write(i + '\n')
    print(i)
f.close()



