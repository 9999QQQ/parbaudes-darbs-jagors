skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
	skaitis[limenis]=skaitis.get(limenis,0)+1

print("Limenu kopsavilkums")
for limenis, skaitts_limenis in sorted(skaits.items(), key=lambda x: x[1],reverse=True):
    print(limenis,skaits_limenis)
