class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(balance)

    def __str__(self):
        return f"BankAccount(Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: ₹ {self.balance:.2f})"

    def __repr__(self):
        return f"BankAccount('{self.account_number}', '{self.holder_name}', '{self.balance:.2f}')"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return (self.account_number == other.account_number and
                    self.holder_name == other.holder_name and
                    self.balance == other.balance)
        return False
    
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(
                account_number=f"{self.account_number}&{other.account_number}",
                holder_name=f"{self.holder_name} & {other.holder_name}",
                balance=self.balance + other.balance
            )
        elif isinstance(other, (int, float)):
            return BankAccount(self.account_number, self.holder_name, self.balance + other)
        return NotImplemented        

if __name__ == "__main__":
    acc1 = BankAccount("12345", "Amit", 5000)
    acc2 = BankAccount("67890", "Rahul", 3000)

    print(acc1)  # __str__
    print(repr(acc2)) # __repr__
    print(acc1 + acc2) 
    print(acc1 + 1000)