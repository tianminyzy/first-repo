class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
    return self.balance
  def withdraw(self,amount):
      self.balance -= amount
      return self.balance
  def display_balance(self):
      print(self.balance)
taki = BankAccount('taki',"kun",11,"student",1108,99)
taki.deposit(96)
taki.withdraw(20)
taki.display_balance()


