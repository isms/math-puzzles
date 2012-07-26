# Puzzlor June 2012 - Lost at Sea

## Description
This is a script to solve the [June 2012 PuzzlOR problem](http://puzzlor.editme.com/lostatsea2) by "brute force" -- checking each possibility one by one.

Starting at each square, it will continue to find all possible path permutations until they are all of the desired length (in the problem, a length of 10 is given). At every step, it will cull the paths which contain duplicate squares, as this is not allowed in the problem description.

## Usage
The script takes one argument for how long the path should be. If no argument is given, it will default to the length `10` as given by the problem.

For example: `python puzzlor.py 5` will output all paths of length 5. It will write all results to standard out. Using `python puzzlor.py` with no argument will output all paths of length 10 (the same output as is saved in `out/`.

## Notes
A comma separated output file for the default length has been placed in `out/`.

Keep in mind that this script will duplicate each result. For every path of value *n*, the exact reverse of that path will also be listed, and will also have *n* as its value.
