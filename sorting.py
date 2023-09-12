def Sorting(price):
    n = len(price)
    for i in range (n-1):
        swap = False
        for j in range (n-i-1):
            if price[j] > price[j+1]:
                swap = True
                price[j], price[j+1] = price[j+1], price[j]

        if swap == False :
            print(price)

price = [20,200,50,30]
Sorting(price)

