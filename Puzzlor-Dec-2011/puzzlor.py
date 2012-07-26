import random, sys

# given
A = (1, 1, 1, 1, 7, 7)
B = (4, 4, 4, 4, 4, 4)
C = (2, 2, 2, 2, 6, 6)
D = (3, 5, 3, 3, 5, 5)

def roll(S):
    return random.sample(S, 1)[0]

def playgame():
    return {roll(A):'A', roll(B):'B', roll(C):'C', roll(D):'D'}

def get_winner(outcome):
    return outcome[max(outcome.keys())]

def tally_outcomes(outcomes):
    tally = {'A':0, 'B':0, 'C':0,'D':0}
    for outcome in outcomes:
        tally[get_winner(outcome)] += 1
    return tally

def probabilities(tally, N):
    prob = {}
    for die, wins in tally.iteritems():
        prob[die] = float(wins) / N
    return prob

def run_simulation(N):
    outcomes = []
    for i in range(N):
        outcomes.append(playgame())
    return outcomes

# all possible outcomes
# all_outcomes = [{a:'A', b:'B', c:'C', d:'D'} for a in A for b in B for c in C for d in D]

if __name__ == '__main__':
    N = int(sys.argv[1])
    print("Number of simulations: " + str(N))
    tally = tally_outcomes(run_simulation(N))
    print("Winners:")
    print(tally)
    print("Probabilities:")
    print(probabilities(tally, N))

