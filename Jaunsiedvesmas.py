fails=open("teksts.txt", "r")
rindas_numurs = 1
for rinda in fails:
    print(f"{rindas_numurs}. {rinda.strip()}")
    rindas_numurs += 1
fails.close()
try:
    fails=open("teksts.txt", "r")
    fails.close()
except FileNotFoundError:
    print("Fails netika atrasts!")
    