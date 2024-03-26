import sys
from node import Node
from priority_queue import PriorityQueueAstar
import random
    
# contains all methods for Astar algorithm
class Astar:
    def __init__(self, starting_state):
        # array containing current state of the pancake stack
        self.starting_state = starting_state

        # size of the stack
        self.size = len(starting_state)

        #store states of visited nodes, not the nodes themselves
        self.visited = []

        # stores search tree, uses Astar version of prio queue
        self.frontier = PriorityQueueAstar(Node(starting_state, None))

        # is None until solution is found
        self.solution_exists = None

    def run(self):
        print("Starting State:", self.starting_state)
        done = False
        #loops until solution is found or there is no solution
        while not done:
            if self.frontier.is_empty():
                done = True
            else: 
                min = self.frontier.remove_min()
                self.visited.append(min.cur_state)

                if min.h_gap() == 0:
                    if min.cur_state[0] > min.cur_state[1]:
                        self.expandFrontier(min)
                    else:
                        self.solution_exists = min
                        done = True
                else:
                    self.expandFrontier(min)

    # adds each possible flip depth to the frontier if it doesn't exist there
    # already
    def expandFrontier(self, node):
        for depth in range(2, self.size+1):
            child = node.flipStack(depth)
            child.parent = node
            if (child.cur_state not in self.visited) and (not 
                                    self.frontier.contains(child)):
                self.frontier.add(child)
            elif self.frontier.contains(child):
                self.frontier.replace(child)

    # prints all flip states from starting state to solution
    def printOutput(self):
            all_states = []
            node = self.solution_exists
            while node != None:
                all_states.append(node)
                node = node.parent

            all_states.reverse()
            for step in range(1, len(all_states)):
                print("Flip", step, ":", all_states[step].cur_state)


if __name__ == "__main__":
    stack = [5, 9, 7, 10, 6, 8, 1, 3, 2, 4]
    random.shuffle(stack)
    astar = Astar(stack)
    astar.run()
    astar.printOutput()



    

