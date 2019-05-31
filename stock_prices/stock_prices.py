#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = 0

    # this loops through the array of stock prices subtracting the initial price (price)
    # from those that come after (price_2)
    for index, price in enumerate(prices):
        for price_2 in prices[index+1:]:
            profit = price_2 - price

            if max_profit == 0 or profit > max_profit:
                max_profit = profit
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
