from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np
import requests
import json
import os

# Create your views here.
# https://theautomatic.net/yahoo_fin-documentation
# https://algotrading101.com/learn/yahoo-finance-api-guide/


def home(request):
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

    if request.method == 'POST':
        ticker = request.POST['ticker']

        try:
            temp = si.get_quote_table(ticker, dict_result=False).set_index('attribute')
            api= pd.DataFrame(data=temp)

        except Exception as e:
            api = "Error"
        return render(request, 'search.html',{'api': api, 'ticker': ticker  })
    else:
        return render(request, 'search.html',{'ticker': "Enter a ticker symbol" })

def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('home')
    else:
        return redirect('home')

def delete(request, stock_name):
    item = Stock.objects.filter(ticker = stock_name)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect('home')

def analysis(request, stock_name):
    from datetime import date

    today = date.today().strftime("%Y-%m-%d")

    temp = si.get_data(stock_name, start_date = "2023-01-01", end_date = today, index_as_date = False, interval = "1d")
    api = pd.DataFrame(data=temp).drop(['ticker'], axis=1)

    try:
        temp = si.get_data(stock_name, start_date = "2023-01-01", end_date = today, index_as_date = False, interval = "1d")
        api = pd.DataFrame(data=temp).drop(['ticker'], axis=1)

        chart_data = []
        for d,v in api.iterrows():
            dct ={}
            dct["date"] = v.date.strftime("%Y-%m-%d")
            dct["open"] = v.open
            dct["high"] = v.high
            dct["low"] = v.low
            dct["close"] = v.close
            dct["adjclose"] = v.adjclose
            dct["volume"] = v.volume
            if (pd.isnull([v.date.strftime("%Y-%m-%d"), v.open, v.high, v.low, v.close, v.adjclose, v.volume]).any()) == False:
                chart_data.append(dct)

        with open("/home/csargin/stocks/quotes/static/data.json", "w") as outfile:
            json.dump(chart_data, outfile , indent=7)
    except Exception as e:
        api = "Error"
    return render(request, 'analysis.html', {'api': api, 'ticker': stock_name , 'chart_data': chart_data })


# {% with v.docs|first as first_doc %}{{ first_doc.id }}{% endwith %}
