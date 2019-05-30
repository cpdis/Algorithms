#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # define the possible options
    rps_list = ['rock', 'paper', 'scissors']

    # define the list of possible outcomes
    outcomes = []

    # return [] for the case where n=0
    if n == 0:
        return [[]]

    # define a helper function to recursively add each outcome to outcomes
    def find_outcomes(outcome, index):
        for i in range(len(rps_list)):
            outcome.append(rps_list[i])

            if index == n:
                # if index is equal to n then add the outcome to outcomes
                outcomes.append(outcome[:])
            else:
                # else recursively run the method again with an increased index
                find_outcomes(outcome, index + 1)

            # remove the last element from the outcome array
            outcome.pop()

    # get things started
    find_outcomes([], 1)

    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
