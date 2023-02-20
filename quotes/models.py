from django.db import models

# Create your models here.
# https://www.techwithtim.net/tutorials/django/sqlite3-database/
# https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/
# https://pythonistaplanet.com/django-database-tutorial/
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
# https://www.techwithtim.net/tutorials/django/sqlite3-database/


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length = 10)
    #time = models.DateField()
    #Stock_Name = models.CharField(max_length = 10)
   # _1y_Target_Est = models.DecimalField(max_digits = 10, decimal_places = 2)
    #_52_Week_Range = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Avg_Volume = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Beta_5Y_Monthly = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Bid = models.CharField(max_length = 10)
    #Days_Range = models.CharField(max_length = 10)
    #EPS_TTM = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Earnings_Date = models.CharField(max_length = 10)
    #Ex_Dividend_Date = models.CharField(max_length = 10)
    #Forward_Dividend_Yield = models.CharField(max_length = 10)
    #Market_Cap = models.DecimalField(max_digits = 15, decimal_places = 2)
    #Open = models.DecimalField(max_digits = 10, decimal_places = 2)
    #PE_Ratio_TTM = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Previous_Close = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Quote_Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    #Volume = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.ticker

class Stock_timeline(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    quote = models.CharField(max_length = 10)
    Date = models.DateField()
    Open = models.CharField(max_length = 10)
    High = models.CharField(max_length = 10)
    Low = models.CharField(max_length = 10)
    Close = models.CharField(max_length = 10)
    Adj_Close = models.CharField(max_length = 10)
    Volume = models.CharField(max_length = 10)

    def __str__(self):
        return self.ticker






