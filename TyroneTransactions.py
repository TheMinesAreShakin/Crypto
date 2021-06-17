import time

class Transaction:
    next_transaction_ID = -1

    def __init__(self, sender, reciever, amount):
        self.transID = Transaction.get_next_transaction_ID()
        self.sender = sender #FIXME: input validation
        self.reciever = reciever #FIXME: input validation
        self.amount = amount
        self.timestamp = time.time()

    @staticmethod
    def get_next_transaction_ID():
        Transaction.next_transaction_ID += 1
        return Transaction.next_transaction_ID

    def __str__(self):
        return "ID: {}\nSender: {}\nReciever: {}\nAmount: {}\nTimestamp: {}\n".format(
            self.transID,
            self.sender,
            self.reciever,
            self.amount,
            self.timestamp
        )