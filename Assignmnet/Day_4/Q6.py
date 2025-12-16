price = [105, 110, 108, 112, 115, 116, 114]

window = 3

rollingAvg = []
for i in range(len(price) - window + 1):
    avg = sum(price[i:i+ window]) / window
    rollingAvg.append(avg)

print("3-day rolling averages:", rollingAvg)