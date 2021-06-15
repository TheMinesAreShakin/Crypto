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
        while self.calculate_hash()[0:6] != "420420":
            self.proof_of_work += 1

    def __str__(self):
        return "Index: {}\nPrevious Hash: {}\nPOW: {}\nTimestamp: {}\nTransaction List: {}\nNew Hash: {}\n".format(
            self.index, self.previousHash, self.proof_of_work,
            self.timestamp, self.transactionList, self.newHash
        )
        

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

    def construct_block():
        pass

    @staticmethod
    def check_validity():
        pass

    def new_data():
        pass

    def latest_block():
        pass



for i in range(0, 20):
    starttime = time.time()
    b = Block(0, "0", ["abc", "bcd"], 0)
    b.construct_proof_of_work()
    endtime = time.time()
    print("block constructed")
    with open("testOutput42069.txt", "a") as outfile:
        outfile.write(str(b))
        outfile.write("Duration: {}\n\n\n".format(endtime-starttime))
