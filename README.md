

Possible cost function (backward cost).
- number of flips to get back to the start state
Possible heuristic function (forward cost).
- h_gap: the number of gaps in the stack, a gap is two pancakes next to each 
- other whose values are not one away from each other

To run and compile, use the command:
python3 a_star.py or python3 uniform_cost.py

Both algorithms assumes solution is in ascending order:
Ex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Both algorithms use a random starting state determined by shuffling an array
with all the elements. To use a predetermined start state, edit the array on
line 70 of a_star.py and line 75 of uniform_cost.py to the desired start state.
Then comment out the random.shuffle on line 71 of a_star.py and line 76 of 
uniform_cost.py

Important Notes:
- running UCS algorithm on any array length larger than 7 takes extremely long
- both algorithms can handle duplicates in the stack but not gaps in pancake
sizes
