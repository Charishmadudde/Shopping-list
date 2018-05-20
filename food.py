import csv

with open('foodData.csv') as f:
    total = float(f.readline().split(',')[1].strip('$').strip())
    foodDict = {k: float(v.strip("$").strip()) for k, v in dict(csv.reader(f, delimiter=',')).items()}

foodPriceList = list(foodDict.values())

foodCombination = []

def findCombination(priceList, totalPrice, partialPriceList=[]):
    s = sum(partialPriceList)

    if s == totalPrice:
        for price in partialPriceList:
            for key, value in foodDict.items():
                if price == value:
                    foodCombination.append(key)

        print(", ".join(map(str, foodCombination)))

    if s >= totalPrice:
        return

    for i in range(len(priceList)):
        n = priceList[i]
        remainingPriceList = priceList[i+1:]
        findCombination(remainingPriceList, totalPrice, partialPriceList + [n])

findCombination(foodPriceList, total)

if not foodCombination:
    print("There is no combination of the dishes that is equal to the target price")
