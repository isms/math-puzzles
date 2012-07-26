import sys

# cross product of elements in A and elements in B
def cross(A, B):
    return [a+b for a in A for b in B]

# get a set of all possible squares ['A1','A2',...,'H8']
cols = 'ABCDEFGH'
rows = '12345678'
squares = cross(cols, rows)

''' set up the dictionary of values 'd' to let us look up the value in a square

    (e.g. d['A1'] == 2)
'''
values = '2201103313211430223300302433311322314222440213441122141231440043'
d = {}
for sq in squares:
	d[sq] = int(values[squares.index(sq)])

# return sum of all values in a path of any length (e.g. ['A1', A2', A3'])
def get_value(path):
    return sum([d[sq] for sq in path])

''' return the squares you are allowed to move to from any sq

    e.g.: find_peers('A1') == ['A2','B1']
'''
def find_peers(square):
    col = square[0] # letter
    row = square[1] # number

    peer_rows = ""    
    # same col, higher row
    if row != "8":
        higher_row = rows[rows.index(row) + 1]
        peer_rows += higher_row
    # same col, lower row
    if row != "1":
        lower_row = rows[rows.index(row) - 1]
        peer_rows += lower_row
    
    peer_cols = ""
    # same row, higher col
    if col != "H":
        higher_col = cols[cols.index(col) + 1]
        peer_cols += higher_col
    # same row, lower col
    if col != "A":
        lower_col = cols[cols.index(col) - 1]
        peer_cols += lower_col
        
    # return the cross product of valid rows and cols
    return cross(peer_cols, row) + cross(col, peer_rows)

# return True if a given path has no repeats, False if it does
def has_no_repeats(path):
    return len(set(path)) == len(path)
    
""" take a list of paths and return a list of all possible paths after moving

    e.g.: get_next([['A1']]) == [['A1','A2'],['A1','B1']]
"""
def get_next(paths):
    next_paths = []
    for path in paths:
        last_sq = path[len(path)-1]
        for peer in find_peers(last_sq):
            next_path = path + [peer]
            next_paths.append(next_path)
    # cull out paths with duplicates
    return [path for path in next_paths if has_no_repeats(path)]
    
""" given a starting square (e.g. 'A1'), return a list of all possible paths
    of the length argument
"""
def find_all_paths_from_square(start_sq, length):
    current = [[start_sq]]
    while(len(current[0]) < length):
        current = get_next(current)
    return current

def usage():
    print("Usage: python puzzlor.py [path length]")

if (__name__ == "__main__"):
    argv = sys.argv
    path_length = 0

    try:
        path_length = int(argv[1])
    except:
        path_length = 10
    
    # output all possible paths and corresponding values separated by commas
    for sq in squares:
        for line in find_all_paths_from_square(sq, path_length):
            print("%s,%d" % (','.join(line), get_value(line)))
