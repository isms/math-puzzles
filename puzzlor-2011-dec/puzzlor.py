import random
import sys

# given
A = (1, 1, 1, 1, 7, 7)
B = (4, 4, 4, 4, 4, 4)
C = (2, 2, 2, 2, 6, 6)
D = (3, 5, 3, 3, 5, 5)


def roll(S):
    """ return a result of rolling the given die """
    return random.sample(S, 1)[0]


def playgame():
    """ roll each die and return a dictionary of the results """
    return {roll(A): 'A', roll(B): 'B', roll(C): 'C', roll(D): 'D'}


def get_winner(outcome):
    """ return the winner as a string, e.g. 'A' """
    return outcome[max(outcome.keys())]


def tally_outcomes(outcomes):
    """ count up all the outcomes """
    tally = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for outcome in outcomes:
        tally[get_winner(outcome)] += 1
    return tally


def probabilities(tally, N):
    """ find the probabilities of each die """
    prob = {}
    for die, wins in tally.iteritems():
        prob[die] = float(wins) / N
    return prob


def run_simulation(N):
    """ play the game N times, return the outcomes dictionary """
    outcomes = []
    for i in range(N):
        outcomes.append(playgame())
    return outcomes


def get_all_outcomes():
    """ brute force all possible outcomes and return the probabilities """
    return [{a: 'A', b: 'B', c: 'C', d: 'D'} for a in A for b in B for c in C for d in D]


def print_results(outcomes):
    """ summarize a set of outcomes """
    N = len(outcomes)
    print("Number of games: " + str(N))
    tally = tally_outcomes(outcomes)
    print("Winners:")
    print(tally)
    print("Probabilities:")
    print(probabilities(tally, N))


if (__name__ == '__main__'):
    N = int(sys.argv[1])
    print("SIMULATION")
    print_results(run_simulation(N))
    print("BRUTE FORCE")
    print_results(get_all_outcomes())
