#!/usr/bin/python

import sys


def remove_high(value, denominations):
    index = 0

    for coin in denominations:
        if coin <= amount:
            index += 1

    return denominations[:index]


def making_change(amount, denominations):
    count = 0
    denominations = remove_high(amount, denominations)

    if amount < 2:
        return 1
    else:
        for denomination in denominations:
            print(
                f"Line 12: Count: {count}, Amount: {amount}, Demonination: {denomination}")
            if amount % denomination == 0:
                print(f"Amount: {amount} is   {denomination}")
                count += 1
            print(
                f"Line 16: Count: {count}, Amount: {amount}, Demonination: {denomination}")
            if amount > denomination and denomination > 1:
                print(
                    f"Line 19: Count: {count}, Amount: {amount}, Demonination: {denomination}")
                making_change(amount // denomination, denominations)
                count += 1
    return count


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
