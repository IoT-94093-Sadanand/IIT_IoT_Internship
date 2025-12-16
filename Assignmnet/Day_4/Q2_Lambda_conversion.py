dis = float(input("Enter a distance value: "))

kmToM = lambda km : km*1000
mToCm = lambda m : m*100
cmToMm = lambda cm : cm*10  
ftToinch  = lambda ft : ft * 12  
inchToCm = lambda inch : inch * 2.54 

def distanCeconverter(dis, ctype,func):
    result = func(dis)
    print(f"{dis}{ctype}={result}")

distanCeconverter(dis, "km to m", kmToM)
distanCeconverter(dis, "m to cm", mToCm)
distanCeconverter(dis, "cm to mm", cmToMm)
distanCeconverter(dis, "ft to inch", ftToinch)
distanCeconverter(dis, "inch to cm", inchToCm)

