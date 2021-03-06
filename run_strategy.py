import os, sys, argparse
import pandas as pd
import backtrader as bt
from backtrader import Cerebro
from backtrader.analyzers import (SQN, AnnualReturn, TimeReturn, SharpeRatio,
                                  TradeAnalyzer)
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold
from strategies.MultiData import MultiData
from script import argparser

args = argparser.parse_args()
cerebro = bt.Cerebro()

# Create the data
prices = pd.read_csv(args.data0, index_col='Date', parse_dates=True)
data1 = pd.read_csv(args.data1, index_col='Date', parse_dates=True)

# initialize the Cerebro engine
cerebro = Cerebro()
cerebro.broker.setcash(100000)

# add data feed
feed = bt.feeds.PandasData(dataname=prices)
cerebro.adddata(feed)

if (args.strategy == 'multi_data'):
# Add the 2nd data to cerebros
    data1 = bt.feeds.PandasData(dataname=data1)
    cerebro.adddata(data1)

strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold,
    "multi_data": MultiData
}

if not args.strategy in strategies:
    print("Invalid strategy, must select one of {}".format(strategies.keys()))
    sys.exit()

cerebro.addstrategy(strategy=strategies[args.strategy])

# Add the Analyzers

tframes = dict(
    days=bt.TimeFrame.Days,
    weeks=bt.TimeFrame.Weeks,
    months=bt.TimeFrame.Months,
    years=bt.TimeFrame.Years)

cerebro.addanalyzer(SQN)
cerebro.addobserver(bt.observers.DrawDown)  # visualize the drawdown evol

if args.legacyannual:
    cerebro.addanalyzer(AnnualReturn)
    cerebro.addanalyzer(SharpeRatio, legacyannual=True)
else:
    cerebro.addanalyzer(TimeReturn, timeframe=tframes[args.tframe])
    cerebro.addanalyzer(SharpeRatio, timeframe=tframes[args.tframe])

cerebro.addanalyzer(TradeAnalyzer)

cerebro.addwriter(bt.WriterFile, csv=args.writercsv, rounding=4)


""" Use cerebro.run(runonce=False) to run in step by step mode. This avoids the batch calculation """
#cerebro.run(runonce=False)
cerebro.run()
cerebro.plot()