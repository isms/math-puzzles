'''
One hundred people board a 100-seat airplane. The first one has lost his
boarding pass, so he sits in a random seat. Each subsequent passenger sits
in his own seat if it's available or takes a random unoccupied seat if it's
not.

What's the probability that the 100th passenger finds his seat occupied?
'''

import random
import datetime
import sys

# create empty plane
def create_empty_plane():
    new_plane = {}
    for i in range(1,101):
        new_plane[i] = 0
    return new_plane

# return all open seats
def list_empty_seats(plane):
    return [i for i in plane.keys() if plane[i] == 0]

# if own seat open, take it; otherwise sit in random empty seat
def pick_seat(plane, passenger):
    if(plane[passenger] > 0):
		pick_random_seat(plane, passenger)
    else:
		plane[passenger] = passenger

def pick_random_seat(plane, passenger):
    empty_seats = list_empty_seats(plane)
    random_seat = random.choice(empty_seats)
    plane[random_seat] = passenger
    
def run_simulation():
    plane = create_empty_plane() # create new plane
    pick_random_seat(plane, 1) # first passenger sits in random seat
    # for passengers 2 through 100, sit in own seat or random seat
    for passenger in range(2,101):
        pick_seat(plane, passenger)
    return plane
    
def run_simulations(num_simulations):
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
    # print('Ran %d simulations, runtime: %s' % (num_simulations, time_stop-time_start))
    # print('Passenger 100 sat in own seat: {0}/{1} {2:f}'.format(success, num_simulations, proportion))
    return proportion
    

def usage():
    print("Usage: python airplane.py [# samples] [# simulations each sample] ")

if (__name__ == "__main__"):
    argv = sys.argv
    num_build = 0
    
    try:
        num_samples = int(argv[1])
        num_simulations = int(argv[2])
    except:
        usage()
        sys.exit()
    
    outfile = open('output.txt', 'w')
    time_start = datetime.datetime.now()
    results = []
    for sample in range(num_samples):
        result = run_simulations(num_simulations)
        print("Sample %d: %f" % (sample, result))
        outfile.write(str(result)+'\n')
    
    time_stop = datetime.datetime.now()
    outfile.close()
        
    print('Ran %d samples of %d simulations each, runtime: %s' % (num_samples, num_simulations, time_stop-time_start))
    