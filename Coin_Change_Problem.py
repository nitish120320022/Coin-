import sys
import time

def menu():
    print("Coin Change by Greedy Algorithm\n")

def getNumOfCoins(coins,sum):
    if (sum==0):
        return 0
    else:
        result = sys.maxsize
        for coin in coins:
            if (coin<=sum):
                result = min(result, getNumOfCoins(coins,sum-coin)+1)
    return result

def greedy(exchange):
    T = 0
    F = 0
    Tw = 0
    H = 0
    while(exchange != 0):
        if(exchange>=1000):
            exchange = exchange-1000
            T = T+1
        elif(exchange>=500):
            exchange = exchange-500
            F = F+1
        elif(exchange>=200):
            exchange = exchange-200
            Tw = Tw+1
        else:
            exchange = exchange-100
            H = H+1 
    print(" coin 1000 :",T)
    print(" coin 500 :",F)
    print(" coin 200 :",Tw)
    print(" coin 100 :",H)

if __name__ == "__main__":
    menu()
    val = 1
    while val!='0':
        coins = [100,200,500,1000]
        stsum = input("Enter amount to change in coin: ")
        sum = int(stsum)
        begin = time.perf_counter()
        greedy(sum)
        end = time.perf_counter()
        print("Time execution : ",end-begin)
        menu()