import itertools

# given
LOCKS = ((39, 6, 75, 88, 15, 57), (9, 2, 58, 68, 48, 64), (29, 55, 16, 67, 8, 91), (40, 54, 66, 22, 32, 25), (49, 1, 17, 41, 14, 30), (44, 63, 10, 83, 46, 3))

# get all possible lock permutations
permutations = list(itertools.product(*LOCKS))

# find solutions
solutions = [perm for perm in permutations if sum(perm) == 419]

# print answer
print(solutions)
