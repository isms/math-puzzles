# Airplane Problem

## Description
This is a script to solve the airplane problem:

> One hundred people board a 100-seat airplane. The first one has lost his boarding pass, so he sits in a random seat. Each subsequent passenger sits in his own seat if it's available or takes a random unoccupied seat if it's not.
> 
> What's the probability that the 100th passenger finds his seat occupied?


For each simulation, it will:

1.  Set up a dictionary representing 100 empty seats on a plane.
2.  Have passenger 1 sit in a random seat. 
3.  Iterate through each of the remaining 99 passengers. If their seat is taken, they will choose a random empty seat.

For each sample of *n* simulations, the proportion of successes (times that passenger 100 sat in his own seat) will be output to a file. 

## Usage
The script takes two arguments: number of samples to run, and number of simulations per sample. For example: `python airplane.py 10000 100` will run 10,000 samples of 100 simulations each. It will write all results to `output.txt`.

## Notes
A sample output file (1,000,000 samples of 100 simulations each) has been placed in `out/`.
