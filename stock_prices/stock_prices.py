#!/usr/bin/python

import argparse


def find_max_profit(prices):
    sell_index = 1
    trade_profit = prices[1] - prices[0]

    for buy_price in prices[:-1]:
        for sell_price in prices[sell_index:]:
            if sell_price - buy_price > trade_profit:
                trade_profit = sell_price - buy_price
        sell_index += 1

    return trade_profit


print(find_max_profit([101, 1]))


if __name__ == '__main__':
    #     # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
