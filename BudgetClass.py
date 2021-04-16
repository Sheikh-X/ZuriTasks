class Budget():  
    def __init__(self):        
        self.categories={'food':0,
            'entertainment':0,
            'clothing':0,
            'others' : 0 }

    def deposit(self, deposit_amount, category):
        self.categories[category.lower()] = self.categories[category.lower()] + deposit_amount

    def withdraw(self,withdraw_amount,category):
        self.categories[category.lower()]=self.categories[category.lower()]-withdraw_amount

    def balance(self,category):
        bal=self.categories[category.lower()]
        print(f"Your balance for {category} is {bal}")


    def transfer(self,category,amount,category2):
        self.categories[category.lower()]=self.categories[category.lower()] -amount
        self.categories[category2.lower()]=self.categories[category2.lower()] +amount



def main():
    cat_map = {
        1: 'food',
        2: 'entertainment',
        3: 'clothing',
        4: 'others'
    }
    new_budget = Budget()     #instance of the class Budget
    print(" *****You can create a new budget here***** \n")
    budget_name = str(input("Enter name of new budget :  "))
  
    selection=(int(input("Select budget category: (1) Food \n (2) Clothing \n (3) Entertainment \n (4)Others \n")))
    option_values=[1,2,3,4]
    if selection not in option_values:
        print("Invalid Category Selected, Please try again")
        main()
   

    option=int(input(f"What would you like to do to the {cat_map[selection]} Category? :(1) Deposit \n (2) Withdraw \n (3) Check balance \n (4) Transfer funds \n"))
    if option == 1:
        a=int(input("Enter the amount you would like to deposit: \n"))
        new_budget.deposit(a,cat_map[selection])
        print("Deposit successful, your new budget balances are: ")
        print(new_budget.categories)
    if option ==2:
        b = int(input("How much would you like to withdraw? : \n"))
        new_budget.withdraw(b,cat_map[selection])
        print("Withdrawal successful, your new budget balances are: ")
        print(new_budget.categories)
    if option==3:
        new_budget.balance(cat_map[selection])
        print("Your budget balances are: ")
        print(new_budget.categories)

    if option==4:
        isValidOption=False
        while isValidOption==False:
            transfer_from=int(input("Transfer from :(1) Food \n (2) Clothing \n (3) Entertainment \n (4)Others \n"))
            if transfer_from not in option_values:
                print("Invalid Option, Please try again")
                # isValidOption=False
            else:
                transfer_to=int(input("Transfer to: (1) Food \n (2) Clothing \n (3) Entertainment \n (4)Others \n"))
                if transfer_to not in option_values or transfer_from == transfer_to:
                    print("Invalid Option, Please try again")
                else:
                    isValidOption=True
                    transfer_amount=int(input(f"How much would you like to transfer from the {cat_map[transfer_from]} to the {cat_map[transfer_to]}? \n"))
                    new_budget.transfer(cat_map[transfer_from],transfer_amount,cat_map[transfer_to])
                    print(new_budget.categories)

main()