# 2. uzdevums
f = open("cities.txt", "x", encoding= "utf-8")
f.write("Tukums, Jelgava, Mārupe")
f.close()

# 4. uzdevums
teksts=input("Mīļākā dziesma:")
tekst=input("Kas izpilda:")
f=open("music.txt", "w")
f.write(teksts)
f.write(tekst)
f.close()






