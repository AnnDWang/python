# 找零最少的硬币

# 判断金额是否匹配，金额不匹配，
# 想要的是最低一个一分钱加上原始金额减去一分钱所需的硬币数量
# 或者一个5美分加上原始金额减去5美分所需的硬币数量
# 或者一个10美分加上原始金额减去10美分所需的硬币数量
def recMC(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins

# print(recMC([1,5,10,25],63))

# 减少工作量的关键是记住一些过去的结果，这样可以避免重新计算我们已经知道的结果
# 这样我们可以避免重新计算我们已经知道的结果
# 一个简单的解决方案是将最小数量的硬币的结果存储在表中
# 然后在计算新的最小值之前，我们首先检查表
# 看看结果是否已知
# 如果表中已有结果，我们使用表中的值，而不是重新计算
def recDC(coinValueList,change,knownResult):
    minCoins=change
    if change in coinValueList:
        knownResult[change]=1
        return 1
    elif knownResult[change]>0:
        return knownResult[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recDC(coinValueList,change-i,knownResult)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResult[change]=minCoins
    return minCoins

# print(recDC([1,5,10,25],63,[0]*64))

def dpMakeChange1(coinValueList,change,minCoins):
    for cents in range(change+1):
        coinCount=cents
        for j in [c for c in coinValueList if c<cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
        minCoins[cents]=coinCount
    return minCoins

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount=cents
        newCoin=1
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

def main():
    amnt=64
    clist=[1,5,10,21,25]
    coinsUsed=[0]*(amnt+1)
    coinCount=[0]*(amnt+1)

    print('making change for',amnt,'requires')
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),'coins')
    print('they are:')
    printCoins(coinsUsed,amnt)
    print('the used list is as follows: ')
    print(coinsUsed)

main()
