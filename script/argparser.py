import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Strategy Analyzer')

    parser.add_argument('--data0', '-d0',
                        default='data/BAC.csv',
                        help='1st data into the system')

    parser.add_argument('--data1', '-d1',
                        default='data/WFC.csv',
                        help='2nd data into the system')

    parser.add_argument('--fromdate', '-f',
                        default='2003-01-01',
                        help='Starting date in YYYY-MM-DD format')

    parser.add_argument('--todate', '-t',
                        default='2005-12-31',
                        help='Starting date in YYYY-MM-DD format')

    parser.add_argument('--period', default=15, type=int,
                        help='Period to apply to the Simple Moving Average')

    parser.add_argument('--runnext', action='store_true',
                        help='Use next by next instead of runonce')

    parser.add_argument('--nopreload', action='store_true',
                        help='Do not preload the data')

    parser.add_argument('--oldsync', action='store_true',
                        help='Use old data synchronization method')

    parser.add_argument('--commperc', default=0.005, type=float,
                        help='Percentage commission (0.005 is 0.5%%')

    parser.add_argument('--stake', default=10, type=int,
                        help='Stake to apply in each operation')
    
    parser.add_argument('--strategy', '-s', default='buy_hold',
                        help='Which strategy to run')

    parser.add_argument('--writercsv', '-wcsv', action='store_true',
                        help='Tell the writer to produce a csv stream')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('--tframe', default='years', required=False,
                       choices=['days', 'weeks', 'months', 'years'],
                       help='TimeFrame for the returns/Sharpe calculations')

    group.add_argument('--legacyannual', action='store_true',
                       help='Use legacy annual return analyzer')

    parser.add_argument('--cash', default=100000, type=int,
                        help='Starting Cash')

    parser.add_argument('--comm', default=2, type=float,
                        help='Commission for operation')

    parser.add_argument('--mult', default=10, type=int,
                        help='Multiplier for futures')

    parser.add_argument('--margin', default=2000.0, type=float,
                        help='Margin for each future')

    parser.add_argument('--plot', '-p', action='store_true',
                        help='Plot the read data')

    parser.add_argument('--numfigs', '-n', default=1,
                        help='Plot using numfigs figures')
                        

    return parser.parse_args()