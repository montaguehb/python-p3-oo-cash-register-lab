#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []

  def add_item(self, title, price, amount = 1):
    self.total += (price * amount)
    for n in range(amount):
      self.items.append(title)
    self.last_transaction = [price, amount]

  def apply_discount(self):
    try:
      if(self.discount != 0):
        self.total = int(self.total * (1 - self.discount/100))
        print(f"After the discount, the total comes to ${self.total}.")
      else:
        raise ValueError
    except ValueError:
      print("There is no discount to apply.") 
  
  def void_last_transaction(self):
    self.total -= (self.last_transaction[0] * self.last_transaction[1])
    for n in range(self.last_transaction[1]):
      self.items.pop()
# cash_register_with_discount = CashRegister(20)
# cash_register_with_discount.add_item("macbook air", 1000)
# cash_register_with_discount.apply_discount()  