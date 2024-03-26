import copy

class Node:
    #default constructor
    def __init__(self, pancakes, parent):
        self.cur_state = pancakes
        self.parent = parent
        self.back_cost = 0

    #heuristic function for astar that returns num gaps in the stack
    def h_gap(self):
        result = 0
        #iterate through state to find all gaps
        for i in range(len(self.cur_state)-1):
            if not abs(self.cur_state[i] - self.cur_state[i+1]) <= 1:
                result+=1
        return result
    
    #total cost function for astar seach algorithm
    def astar_cost(self):
        return self.back_cost + self.h_gap()
    
    #cost function for uniform cost search algorithm
    def ucs_cost(self):
        return self.back_cost
    
    # returns a copy of self where its pancake stack is flipped at the [depth]
    # pancake
    def flipStack(self, depth):
        child = copy.deepcopy(self)
        flips = int(depth/2)
        for i in range(flips):
            temp = child.cur_state[i]
            child.cur_state[i] = child.cur_state[depth - i - 1]
            child.cur_state[depth - i - 1] = temp
        child.back_cost += 1
        return child