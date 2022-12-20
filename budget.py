class Category:
    def __init__(self, category):
        self.category = category
        self.curBalance = 0
        self.ledger = list()
    def __str__(self):
        ret  = self.category.center(30,'*')+'\n'
        tot = 0
        for trans in self.ledger:
            ret += (trans["description"]).ljust(23) if len(trans["description"])<=23 else trans["description"][:23]
            ret += "{:.2f}".format(trans["amount"]).rjust(7)+'\n'
            tot += trans["amount"]
        ret += "Total: "+str(tot)
        return ret

    def deposit(self, amt, desc=''):
        self.ledger.append({"amount":amt, "description": desc})
        self.curBalance = self.get_balance() + amt

    def withdraw(self, amt, desc=''):
        if self.check_funds(amt) :
            self.ledger.append({"amount": -amt, "description": desc})
            self.curBalance = self.get_balance() - amt
            return True
        return False

    def get_balance(self):
        return self.curBalance

    def transfer(self, amt, cat):
        st = "Transfer to "+cat.category
        if self.withdraw(amt, st):
            st = "Transfer from "+self.category
            cat.deposit(amt, st)
            return True
        else:
            return False

    def check_funds(self, amt):
        if self.get_balance()>=amt:
            return True
        else:
            return False
        
def create_spend_chart(categories):
    return "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "