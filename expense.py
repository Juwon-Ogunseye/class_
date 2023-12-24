import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self,title,amount):
        self.id =str(uuid.uuid4())
        self.title =title
        self.amount =amount
        self.created_at =datetime.utcnow()
        self.updated_at =self.created_at
    def update(self, title=None,amount=None):
        if self.title is not None:
            self.title =title
        if self.amount is not None:
            self.amount = amount
        self.updated_at =datetime.utcnow()
        print(f'The Expense has been updated successfully')
    def to_dict(self):
        return {
            'id':self.id,
            'Title':self.title,
            'Amount':self.amount,
            'Created_at':self.created_at,
            'Updated_at':self.updated_at
        }
    def __repr__(self)->str:
        return(f'{self.title} {self.amount}')
# expense =Expense("Stationary",600.23)
# print(expense.to_dict())
class ExpenseDatabase:
    def __init__(self):
        self.expenseDB=[]#Creating a list

    def add_expense(self,expense):
        #function to add expense into the database
        self.expenseDB.append(expense)
        print(f'{expense} added successfully')

    def remove_expense(self,expense_id):
        #method to remove expense via its id
        self.expenseDB =[expense for expense in self.expenseDB if expense.id !=expense_id ]
        print(f'Expense with id:{expense_id}has been removed')
    def get_expense_by_id(self,expense_id):
        expense =[expense for expense in self.expenseDB if expense.id ==expense_id]
        if len(expense)==0:
            return None
        return expense[0]
    def get_expense_by_title(self,expense_title):
        return[expense for expense in self.expenseDB if expense.title ==expense_title]
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenseDB]
    
expense_1 =Expense("Keyboard",5000.65)
expense_3 =Expense("Monitors",9880.87)
edb =ExpenseDatabase()
edb.add_expense(expense_1)
edb.add_expense(expense_3)
for expense in edb.expenseDB:
    print(expense.to_dict())

# Update an expense
print("\n Expenses after Update:")
edb.expenseDB[0].update(amount=20000.00)

#Updated Expense Database
print('\n Updated Expense Database')
for expense in edb.expenseDB:
    print(expense.to_dict())

# Remove an expense
print("\nRemove an Expense")
edb.remove_expense(expense_3.id)

#Check the status of the database
print('Check status of database')
for expense in edb.expenseDB:
    print(expense.to_dict())






    
    

        
    
        