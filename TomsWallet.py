from TyroneTransactions import Transaction

"""should we include not only a list of pending transactions
but of all previous confirmed transactions
probably"""#FIXME
class Wallet():
    def __init__(self, ownerID):
        self.ownerID = ownerID
        self.balance = 10
        self.pendingTransactions = []

    def create_new_transaction(self, sender, reciever, amount):
        """returns new transaction, returns None if there was a problem"""
        #FIXME: figure out how to validate sender and reciever being real
        if sender == self.ownerID:
            pendingBalance = self.balance
            for trans in self.pendingTransactions:
                pendingBalance -= trans.amount
            print(pendingBalance)
            if amount > pendingBalance:
                return
            newTransaction = Transaction(sender, reciever, amount)
            self.pendingTransactions.append(newTransaction)
            return newTransaction
            """add transaction to pending list until the transaction
            is featured in the block chain"""
        elif reciever == self.ownerID:
            pass
            """How does this work? What if you don't recieve the
            broadcast of the transaction
            sweep through blockchains you have or (recieve and trust)
            and see if you are marked as a reciever in any transaction"""
            #FIXME: what if you trust a fraudulent block and think you have more coins than you really do
        else:
            print("What? see documentation: https://i.ytimg.com/vi/r94vuvwUSkY/maxresdefault.jpg")
            return
            #FIXME: should probably throw an error here


        #list of pending transactions (id, amount, amISending)
        def reconcile_with_blockchain():
            pass
            """don't subtract from my bitcoin until the pending transaction
            #is seen in a new block on the chain"""

        """use list of pending transactions to limit the new transactions
        that I am creating"""