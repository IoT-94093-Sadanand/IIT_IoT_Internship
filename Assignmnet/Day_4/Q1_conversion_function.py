dis = float(input("Enter a distance value: "))

def kmToM(km):
    return km * 1000
def mToCm(m):
    return m * 100
def cmToMm(cm):
    return cm * 10
def ftToinch(ft):
    return ft * 12
def inchToCm(inch):
    return inch * 2.54
def distanCeconverter(dis, ctype,func):
    result = func(dis)
    print(f"{dis}{ctype}={result}")

distanCeconverter(dis, "km to m", kmToM)
distanCeconverter(dis, "m to cm", mToCm)
distanCeconverter(dis, "cm to mm", cmToMm)
distanCeconverter(dis, "ft to inch", ftToinch)
distanCeconverter(dis, "inch to cm", inchToCm) 

