# Puzzlor May 2012 - McEverywhere

## Description
This is a script to solve the [May 2012 PuzzlOR problem](http://puzzlor.editme.com/McEverywhere) by "brute force" -- checking each possibility one by one.

For each possibility, it will:

1.  Calculate the distances from each house to each restaurant.
2.  Find the minimum distance from each house to any restaurant (in effect finding the closest restaurant).
3.  Write to an output file the maximum of these minimum distances as a measure of how optimal the restaurant placement is (the smaller, the better), as well as a string representation of the 10x10 grid showing the restaurant placements that resulted in the max-min distance. 

## Usage
The script takes one argument for how many restaurants to build. For example: `python puzzlor.py 2` will try all 4950 combinations of places to build 2 restaurants. It will write all results to `output_2.txt`.

## Notes
Output files for *n* = 1, 2, and 3 have been placed in `out/`.

Some extraneous materials have been placed in `extra/`.
