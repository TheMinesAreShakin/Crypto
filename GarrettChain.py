import hashlib
import time
import TyroneTransactions

#below is the right way to hash things dumbass
#print(hashlib.sha256(b"hello").hexdigest())

class Block:
    def __init__(self, index, previousHash, transactionList, minerID):
        """max num of transactions is 20"""
        if len(transactionList) > 20:
            transactionList = transactionList[:20]

        self.index = index
        self.minerID = minerID
        self.previousHash = previousHash
        self.transactionList = transactionList
        self.proof_of_work = 0
        self.timestamp = time.time()
        self.newHash = ""

    def calculate_hash(self): #FIXME to include proof of work stuff
        stringThing = "{}{}{}{}{}{}".format(
            self.index,
            self.minerID,
            self.previousHash,
            self.transactionList,
            self.proof_of_work,
            self.timestamp
        )

        self.newHash = hashlib.sha256(stringThing.encode()).hexdigest()
        return self.newHash

    def construct_proof_of_work(self):
        while self.calculate_hash()[0:2] != "69": #FIXME: correct length
            self.proof_of_work += 1

    def __str__(self):
        return "Index: {}\nPrevious Hash: {}\nPOW: {}\nTimestamp: {}\nTransaction List: {}\nNew Hash: {}\n".format(
            self.index, self.previousHash, self.proof_of_work,
            self.timestamp, self.transactionList, self.newHash
        )

    def get_hash(self):
        return self.newHash
        

class Blockchain:
    def __init__(self):
        self.blockList = []

    def construct_genisis(self, transList):
        """
        Create genisis block

        param: transList -> list of initial transactions

        effect: first block added to blockchain. (No hashing or proof of work done FIXME??)

        return: void
        """
        genBlock = Block(0, None, transList)
        self.blockList.append(genBlock)

    def get_next_index(self):
        return len(self.blockList)

    def get_prev_hash(self):
        prevHash = ""
        if len(self.blockList) == 0:
            prevHash = "https://bit.ly/3pTa4fO"
        else:
            prevHash = self.blockList[-1].get_hash()
        return prevHash

    def __str__(self):
        output = ""
        for block in self.blockList:
            output += str(block)
        return output

    def appendBlock(self, newBlock):
        self.blockList.append(newBlock)

    def construct_block():
        pass

    @staticmethod
    def check_validity():
        pass

    def new_data():
        pass

    def latest_block():
        pass


# b = Block(0, "0", ["abc", "bcd"], 0)
# b.construct_proof_of_work()
# print(b)