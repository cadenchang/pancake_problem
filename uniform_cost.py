import sys
from node import Node
from priority_queue import PriorityQueueUCS
import random
    
# contains all methods for UCS algorithm
class UniformCostSearch:
    def __init__(self, starting_state):
        # array containing current state of the pancake stack
        self.starting_state = starting_state

        # size of the stack
        self.size = len(starting_state)

        # stores states of visited nodes not the actual nodes
        self.visited = []

        # stores search tree and uses UCS version of prio queue
        self.frontier = PriorityQueueUCS(Node(starting_state, None))

        # value equal to none until solution is found
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
                if self.isSolution(min):
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

    # returns true if given node state is a solution
    def isSolution(self, node):
        for i in range(len(node.cur_state)-1):
            if node.cur_state[i] > node.cur_state[i+1]:
                return False
        return True


if __name__ == "__main__":
    stack = [2, 1, 3, 4, 5, 6, 7]
    random.shuffle(stack)
    alg = UniformCostSearch(stack)
    alg.run()
    alg.printOutput()
    

