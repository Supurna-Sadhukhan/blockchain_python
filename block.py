class Block:
    def __init__(self):
        self.index = 0
        self.previousHash = ""
        self.hash = ""
        self.nonce = 0
        self.transactions = []

    def key(self):
        return f"{repr(self.transactions)}{str(self.index)}{str(self.previousHash)}{str(self.nonce)}"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        return f"Previous Hash:{self.previousHash}, Nonce:{self.nonce}, Number of Transactions:{len(self.transactions)}"
