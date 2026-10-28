skaits = 0

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        if "CRITICAL" in rinda:
            skaits = skaits + 1

print("CRITICAL rindas:", skaits)
