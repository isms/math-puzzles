""" One hundred people board a 100-seat airplane. The first one has lost his
boarding pass, so he sits in a random seat. Each subsequent passenger sits
in his own seat if it's available or takes a random unoccupied seat if it's
not.

What's the probability that the 100th passenger finds his seat occupied? """

import random
import datetime
import sys

def create_empty_plane():
    """ create empty plane """
    new_plane = {}
    for i in range(1,101):
        new_plane[i] = 0
    return new_plane

def list_empty_seats(plane):
    """ return all open seats """
    return [i for i in plane.keys() if plane[i] == 0]

def pick_seat(plane, passenger):
    """ if own seat open, take it; otherwise sit in random empty seat """
    if(plane[passenger] > 0):
        pick_random_seat(plane, passenger)
    else:
        plane[passenger] = passenger

def pick_random_seat(plane, passenger):
    """ seat the passenger in an empty seat """
    empty_seats = list_empty_seats(plane)
    random_seat = random.choice(empty_seats)
    plane[random_seat] = passenger
    
def run_simulation():
    """ go through and seat a passenger """
    plane = create_empty_plane() # create new plane
    pick_random_seat(plane, 1) # first passenger sits in random seat
    # for passengers 2 through 100, sit in own seat or random seat
    for passenger in range(2,101):
        pick_seat(plane, passenger)
    return plane
    
def run_simulations(num_simulations):
    """ go through a certain numer of simulations """
    # track time started
    time_start = datetime.datetime.now()    
    # initialize counter for successes
    success = 0
    for i in range(num_simulations):
        plane = run_simulation()
        if(plane[100] == 100):
            success += 1
    # track time ended
    time_stop = datetime.datetime.now()
    proportion = float(success)/num_simulations
    return proportion
    
if (__name__ == "__main__"):
    argv = sys.argv
    num_build = 0
    try:
        num_samples = int(argv[1])
        num_simulations = int(argv[2])
    except:
        print("Usage: python airplane.py [# samples] [# simulations each]")
        sys.exit(1)
    outfile = open('output.txt', 'w')
    time_start = datetime.datetime.now()
    results = []
    for sample in range(num_samples):
        result = run_simulations(num_simulations)
        print("Sample %d: %f" % (sample, result))
        outfile.write(str(result)+'\n')
    time_stop = datetime.datetime.now()
    outfile.close()
    print('Ran %d samples of %d simulations each, runtime: %s' % 
        (num_samples, num_simulations, time_stop-time_start))
    
