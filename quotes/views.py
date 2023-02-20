from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np

# Create your views here.

def home(request):
    import requests
    import json

    ticker_list = tuple(Stock.objects.values_list('ticker', flat = True))
    api = {}
    if len(ticker_list)>0:
        try:
            ticker_attribute = si.get_quote_table(str(ticker_list[0]), dict_result=False).attribute.tolist

            for ticker in ticker_list:
                api[str(ticker)] = si.get_quote_table(str(ticker), dict_result=False).value.tolist
        except Exception as e:
            api = "Error"
        return render(request, 'home.html',{'api': api , 'ticker_attribute': ticker_attribute })
    else:
        return render(request, 'home.html',{'api': "Portfolio is Empty" })

def about(request):
    return render(request, 'about.html' , {})

def search(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        #pk_6ef09bbbcf8c4046b022672798acc880
        #api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_6ef09bbbcf8c4046b022672798acc880")

        try:
            temp = si.get_quote_table(ticker, dict_result=False).set_index('attribute')
            api= pd.DataFrame(data=temp)

        except Exception as e:
            api = "Error"
        return render(request, 'search.html',{'api': api, 'ticker': ticker })
    else:
        return render(request, 'search.html',{'ticker': "Enter a ticker symbol" })

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('home')
    else:
        return redirect('home')


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect('home')

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html' , {'ticker': ticker})