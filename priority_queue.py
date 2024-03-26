import heapq
from dataclasses import dataclass, field
from typing import Any
from node import Node

# data lass used to prioritize the cost function, but wrap the entire node
# in the priority queue
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

#prioritizes nodes in the heap based on their astar cost 
class PriorityQueueAstar:
    #default constructor
    def __init__(self, root):
       self.heap = []
       item = PrioritizedItem(root.astar_cost(), root)
       heapq.heappush(self.heap, item)
    
    # adds given node to priority queue
    def add(self, node):
        item = PrioritizedItem(node.astar_cost(), node)
        heapq.heappush(self.heap, item)

    # removes node with min total cost function from heap
    def remove_min(self):
        item = heapq.heappop(self.heap)
        return item.item
    
    # returns true if the prio queue is empty
    def is_empty(self):
        return len(self.heap) == 0
    
    # updates state of given node in the queue
    def replace(self, node):
        for item in self.heap:
            elem = item.item
            if elem.cur_state == node.cur_state:
                if node.astar_cost() < elem.astar_cost():
                    self.heap[self.heap.index(item)].item = elem

    # returns true if given node [query] is in the prio queue
    def contains(self, query):
        for item in self.heap:
            node = item.item
            if node.cur_state == query.cur_state:
                return True
        return False

#prioritizes nodes in the heap based on their cost (back_cost)
class PriorityQueueUCS:
    # default constructor
    def __init__(self, root):
       self.heap = []
       item = PrioritizedItem(root.ucs_cost(), root)
       heapq.heappush(self.heap, item)
       
    # adds given node to priority queue
    def add(self, node):
        item = PrioritizedItem(node.ucs_cost(), node)
        heapq.heappush(self.heap, item)

    # removes node with min cost function from heap
    def remove_min(self):
        item = heapq.heappop(self.heap)
        return item.item
    
    # returns true if queue is empty
    def is_empty(self):
        return len(self.heap) == 0
    
    # updates state of given node in the queue 
    def replace(self, node):
        for item in self.heap:
            elem = item.item
            if elem.cur_state == node.cur_state:
                if node.ucs_cost() < elem.ucs_cost():
                    self.heap[self.heap.index(elem)] = elem

    # returns true if given node [query] is in the prio queue
    def contains(self, query):
        for item in self.heap:
            node = item.item
            if node.cur_state == query.cur_state:
                return True
        return False
