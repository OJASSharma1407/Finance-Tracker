from django.db import models
from django.utils import timezone
from user_auth.models import Reg_user

# Create your models here.


class Transaction(models.Model):
    TRANSACTIONS_TYPE = [
        ('Income','Income'),
        ('Expense','Expense',)
    ]

    TRANSACTION_CATAGORY = [
        ('Subscription','Subscription'),
        ('Groceries','Groceries'),
        ('Transportation','Transportation'),
        ('Entertainment','Entertainment'),
        ('Rent','Rent'),
        ('Salary', 'Salary'),
        ('Freelancing', 'Freelancing'),
        ('Investment', 'Investment'),
    ]
    user = models.ForeignKey(Reg_user,on_delete=models.CASCADE,related_name='transactions',null=True)
    amount = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    catagory = models.CharField(max_length=15,choices=TRANSACTION_CATAGORY)
    transaction_type = models.CharField(max_length=7,choices=TRANSACTIONS_TYPE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):

        return f"{self.transaction_type} ₹{self.amount} on {self.date.date()}"
    

class Dashboard(models.Model):

    user = models.OneToOneField(Reg_user,on_delete=models.CASCADE)
    balance = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    income = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    expense = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"{self.user.username}'s Dashboard"
