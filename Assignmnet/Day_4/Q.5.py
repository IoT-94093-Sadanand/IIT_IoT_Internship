tonn = float(input("Enter weight in tonns: "))

tonnTokg = lambda t: t * 1000
kgTog = lambda kg: kg * 1000
gTomg = lambda g: g * 1000
mgTolb = lambda mg: mg * 0.00000220462  

kg = tonnTokg(tonn)
g = kgTog(kg)
mg = gTomg(g)
lb = mgTolb(mg)

print(f"{tonn} tonns = {kg} kg")
print(f"{kg} kg = {g} g")
print(f"{g} g = {mg} mg")
print(f"{mg} mg = {lb} lbs")