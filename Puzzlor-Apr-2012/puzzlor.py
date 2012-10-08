import numpy
import sys
import copy
import itertools
import datetime

# set character values
EMPTY_CHAR = '.'
HOUSE_CHAR = 'H'
MCEV_CHAR = 'M'

# defines what a feasible result is
THRESHOLD = 4

# GIVEN house locations from the problem description
#     format: (row, col), top left = (0, 0)
HOUSE_POINTS = [(0,3), (0,7), (0,8), (0,9),
                (1,3), (1,6),
                (2,7), (2,8),
                (3,1),
                (4,0),
                (5,1), (5,4), (5,5),
                (6,4), (6,8),
                (7,2), (7,4),
                (8,4), (8,8),
                (9,6)]

def create_grid():
    """ create new grid dictionary """
    grid = {(x, y): EMPTY_CHAR for x in range(0,10) for y in range(0,10)}
    return grid

def set_points_in_grid(grid, points, char):
    """ iterate through each tuple in the grid, setting the value of 
        that grid point key, if in the argument grid, to the given char
        Example: set_points_in_grid(empty_grid, HOUSE_POINTS,  HOUSE_CHAR) """
    for point in points:
        grid[point] = char

def dist(a, b):
    """ calculate Euclidean distance between two tuple points """
    # determine horizontal and vertical distances
    deltas = (b[0]-a[0], b[1]-a[1])
    # use convenient function to calculate hypotenuse
    return numpy.linalg.norm(deltas)

def print_grid_as_line(grid):
    """ takes a grid of points and just joins them, in order, to one string """
    chars = []
    for row in range(0,10):
        for col in range(0,10):
            chars.append(grid[(row,col)])
    return ''.join(chars)

def get_points_with_char(grid, char):
    """ return all point tuples where value is specified char """
    # don't calculate if none in grid
    if (char not in grid.values()):
        return []
    else:
        return [key for key in grid.keys() if grid[key] == char]

def calculate_min_distances(house_grid, mcev_grid):
    """ calculate minimum distances between houses and McEverywheres """
    if (HOUSE_CHAR not in house_grid.values() or
            MCEV_CHAR not in mcev_grid.values()):
        print("Need houses and McEverywheres in grid to calculate")
        return []
    houses = get_points_with_char(house_grid, HOUSE_CHAR)
    mcevs = get_points_with_char(mcev_grid, MCEV_CHAR)
    distances = []
    # calculate distance from each house to each McEverywhere 
    for house in houses:
        distances.append([dist(house, mcev) for mcev in mcevs])
    # we only care about the closest restaurant to each house, so take the min
    min_distances = [min(d) for d in distances]
    return min_distances

def get_building_possibilities(house_grid, build_grid, num_to_build):
    """ run through all buildable combinations, logging all results
        returns the set of feasible results """
    # set up output file
    outfile = open('output_%d.txt' % num_to_build, 'w')
    results = []
    # find empty places to build
    empties = get_points_with_char(build_grid, EMPTY_CHAR)
    # figure out all possible building combinations
    trials = itertools.combinations(empties, num_to_build)
    time_start = datetime.datetime.now()
    for trial in itertools.combinations(empties, num_to_build):
        # create a copy so we're not changing the actual grid
        grid_copy = copy.deepcopy(build_grid)
        set_points_in_grid(grid_copy, trial, MCEV_CHAR)
        max_min = max(calculate_min_distances(house_grid, grid_copy))
        # write to file
        outfile.write(str(max_min) + ' ' +
            print_grid_as_line(grid_copy) + '\n')
        # if we find a feasible solution, add to the set
        if(max_min <= THRESHOLD):
            results.append((trial, max_min))
    time_stop = datetime.datetime.now()
    outfile.close()
    print("Found %d results, runtime: %s" % (len(results), 
        time_stop-time_start))
    # return set of feasible results; not used elewhere
    return results
   
if (__name__ == "__main__"):
    argv = sys.argv
    num_build = 0
    try:
        num_build = int(argv[1])
    except:
        print("Usage: python puzzlor.py [# restaurants]")
        sys.exit(1)
    # set up houses
    house_grid = create_grid()
    set_points_in_grid(house_grid, HOUSE_POINTS, HOUSE_CHAR)
    # set up an empty grid for building; we are able to make some cells off
    # limits, but it is GIVEN in the problem description that you can build
    # anywhere, so there is no need to set points
    build_grid = create_grid()
    # find all possibilities
    results = get_building_possibilities(house_grid, build_grid, num_build)
