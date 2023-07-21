class Category:
  ledger=[]

  def __init__(self,category): #category : type of purchase, ledger =
    self.category = category
    
  
  
  def deposit(self,amt,descp = ''):
    self.amt = amt #amount of item
    self.descp = descp #description of item
    ledger.append({'amount':self.amt,'description':self.descp})
    
  def withdrawal(self,wamt,wdescp=''):
    self.wamt = wamt  #amount withdrawn
    self.wdescp= wdescp  
    if(check_funds(self)):
      ledger.append({'amount': -1*self.wmt,'description':self.descp})
      return True
    else: 
      return False

  def get_balance(self):
    for i in ledger:
      self.balance += ledger['amount']
