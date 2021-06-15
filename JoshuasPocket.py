from GarrettChain import Block, Blockchain
from TomsWallet import Wallet
import TyroneTransactions #FIXME did I actually use this?

class Pocket:
    nextPocketID = 0

    def __init__(self):
        self.pocketID = Pocket.nextPocketID
        Pocket.nextPocketID += 1#FIXME turn into get pocketID static method
        self.previousTransCollected = []
        self.myWallet = Wallet()
        self.myChain = Blockchain()
        self.myBlock = None

    def addTransaction(self, trans):
        self.previousTransCollected.append(trans)
        if len(self.previousTransCollected) >= 20:
            self.createBlock()

    def createBlock(self):
        passTransactionsList = self.previousTransCollected[0:20]
        newBlock = Block(
            self.myChain.get_next_index(),
            self.myChain.get_prev_hash(),
            passTransactionsList,
            self.pocketID)

        newBlock.construct_proof_of_work() #FIXME should this be in constructor??????
        self.myChain.appendBlock(newBlock)
        self.previousTransCollected = self.previousTransCollected[20:]#FIXME self.previousTransCollected - passTransactionsList

    def __str__(self):
        output = ""
        output += str(self.myChain)
        return output



pocketRocket = Pocket()
print(pocketRocket.pocketID)
p = Pocket()
print(p.pocketID)
for i in range(0, 100):
    p.addTransaction("{}".format(i))

print(p)