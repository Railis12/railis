mašīna={
"BMW":1916,
"Citroen":1919,
"Skoda":1895,
"Audi":1909,
"Renault":1898,
}
for i in mašīna.values():
    print(mašīna.values())
for i in mašīna.keys():
    print(mašīna.keys())
if "Audi" in mašīna:
    print("ir")
else:
    print("nav")
y=mašīna.values()
for x, y in mašīna.items():
    if y<2010:
        print(x)
    

