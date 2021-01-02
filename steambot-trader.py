

import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm

class Steambot:
    def __init__(self):
        pass

    def get_price_data(self,ticker):
        self.price_data = si.get_data(key,start_date = '01/01/2009')

class Strategy:
    def __init__(self,starting_capital):
        self.starting_capital = starting_capital
        self.watch_list = []
        self.trades = []

    def get_returns(self):
        self.daily_returns = None
        self.monthly_returns = None
        pass

    def show_trades(self,start_date,end_date):
        pass

    def get_betas(self,watch_list):
        pass

    def get_bollinger_bands(self,watch_list):
        pass


class Trade:
    def __init__(self,ticker,shares,trade_price,trade_date):
        self.ticker = ticker
        self.shares = shares
        self.trade_price = trade_price
        self.trade_date = trade_date

class Stock:
    def __init__(self,ticker):
        self.ticker = ticker
        self.price_data = self.get_price_data()

    def get_price_data(self,ticker):
        self.price_data = si.get_data(key,start_date = '01/01/2009')

    def get_betas(self,universe):
        pass

    def get_bollinger_bands(self):
        pass

    def get_rsi(self):
        pass

    def get_ordered_pairs(self,watch_list):
        pass

    def get_returns(self):
        self.daily_returns = None
        self.monthly_returns = None
        pass

class Index:
    def __init__(self,ticker):
        self.price_data = self.get_price_data()
