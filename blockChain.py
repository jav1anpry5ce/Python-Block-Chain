from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import json
from datetime import datetime

usersFile = open('users.json', 'r')
users  = json.loads(usersFile.read())

class Transaction(object):
    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.signature = ''
        self.key = ''

    def calculateHash(self):
        data = str(self.fromAddress) + str(self.toAddress) + str(self.amount)
        data = data.encode('utf-8')
        return SHA256.new(data)
    
    def signTransaction(self, key):
        if hex(key.n) != self.fromAddress:
            raise Exception("You cannot sign transcations for other wallets!")
        hashTX = self.calculateHash()
        singer = PKCS115_SigScheme(key)
        sig = singer.sign(hashTX)
        self.signature = sig
        self.key = key

    def isValid(self):
        if self.fromAddress == None: return True
        if not self.signature or len(self.signature) == 0:
            raise Exception("No signature in this transaction")
        singer = PKCS115_SigScheme(self.key.publickey())
        try:
            singer.verify(self.calculateHash(), self.signature)
            return True
        except:
            return False
        
    def __str__(self):
        return json.dumps({'From Address':self.fromAddress, 'To Address':self.toAddress, 'Amount':self.amount})

class Block(object):
    def __init__(self, timestamp, transactions, previousHash = ''):
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculateHash()
    
    def calculateHash(self):
        data = str(self.previousHash) + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        data = data.encode('utf-8')
        return SHA256.new(data).hexdigest()
    
    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != str('').zfill(difficulty):
            self.nonce += 1
            self.hash = self.calculateHash()
            #print(self.hash)
    
    def hasValidTransaction(self):
        for tx in self.transactions:
            if not tx.isValid():
                return False
        return True     
    def __str__(self):
        return json.dumps({'Previous Hash':self.previousHash, 'Nonce':self.nonce,  'Hash':self.hash}, indent=4)

class Blockchain(object):
    def __init__(self):
        self.chain = [self.createGenesisBlock(),]
        self.difficulty = 3
        self.pendingTransactions = []
        self.reward = 100

    def createGenesisBlock(self):
        return Block(datetime.strptime('2020-12-28 08:15:27.24', '%Y-%m-%d %H:%M:%S.%f'), [], "0")

    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def minePendingTransactions(self, rewardAddress):
        start = datetime.now()
        rewardTx = Transaction(None, rewardAddress, self.reward)
        self.pendingTransactions.append(rewardTx)

        block = Block(datetime.now(), self.pendingTransactions, self.getLastBlock().hash)

        block.mineBlock(self.difficulty)
        stop = datetime.now()
        time = stop - start
        print("Block successfully mined!")
        userFound = False
        for i in users:
            if rewardAddress in i['MiningAddress']:
                print("Mined by:", i['Name'])
                userFound = True
        if not userFound:
            print("Mined by:", rewardAddress)
        print("Transactions completed:", len(self.pendingTransactions))
        print("Time:", block.timestamp)
        print("Mined In:", time)
        print("Difficulity:", self.difficulty)
        print("Nonce:", block.nonce)
        print("Reward:", self.reward)
        print("Hash:", block.hash)
        print("Previous hash:", self.getLastBlock().hash)
        print("Is chain valid:", self.validateChain())
        self.chain.append(block)
        self.pendingTransactions = []

    def addTransaction(self, transaction):
        if transaction.fromAddress == None or transaction.toAddress == None:
            raise Exception("Transaction must include from and to address")
        if not transaction.isValid():
            raise Exception("Cannot add invalid transaction to chain!")
        self.pendingTransactions.append(transaction)

    def getBalance(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.fromAddress == address:
                    balance -= trans.amount
                if trans.toAddress == address:
                    balance += trans.amount
        return balance
    
    def validateChain(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]

            if not currentBlock.hasValidTransaction():
                return False
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.calculateHash():
                return False
        return True
    def __str__(self):
        for i in range(0,len(self.chain)):
             print(self.chain[i])
        return 'END OF CHAIN!'