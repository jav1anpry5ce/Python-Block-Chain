from blockChain import *

key1 = open('amitKey.pem', 'r')
key2 = open('javanKey.pem', 'r')
amitkey = RSA.importKey(key1.read())
javanKey = RSA.importKey(key2.read())

amitwallet = hex(amitkey.n)
javanwallet = hex(javanKey.n)

coin = Blockchain()

def sendJCoin(fromAddress, toAddress, amount, privateKey):
    if fromAddress == toAddress:
        print("Transaction from and to address can't be same!\nTransaction will be ignored!")
    elif coin.getBalance(fromAddress) - amount <= 0:
        print('Not enough JCoin for this transaction!\nTransaction will be ignored!')
    else:
        transaction = Transaction(fromAddress, toAddress, amount)
        transaction.signTransaction(privateKey)
        coin.addTransaction(transaction)

print('Starting the mine!')
coin.minePendingTransactions(amitwallet)

print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))


sendJCoin(amitwallet, javanwallet, 10, amitkey)


print('\n\nStarting the mine!')
coin.minePendingTransactions(amitwallet)

print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))

sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)
sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)
sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)

print('\n\nStarting the mine!')
coin.minePendingTransactions(javanwallet)


print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))

print('Starting the mine!')
coin.minePendingTransactions(amitwallet)

print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))


sendJCoin(amitwallet, javanwallet, 10, amitkey)


print('\n\nStarting the mine!')
coin.minePendingTransactions(amitwallet)

print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))

sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)
sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)
sendJCoin(javanwallet, amitwallet, 0.484154554454841584, javanKey)

print('\n\nStarting the mine!')
coin.minePendingTransactions(javanwallet)


print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))


print('Starting the mine!')
coin.minePendingTransactions(amitwallet)

print('Balance of Amit wallet:', coin.getBalance(amitwallet))
print('Balance of Javan wallet:', coin.getBalance(javanwallet))
