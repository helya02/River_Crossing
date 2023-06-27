#class of node
#with the help of this class, we can create a node that save:
#state: show On which side of the river are the people and the boat? .
#state type: state structure is a python dictioanary. the key of dict is short name of peopele and boat , and the value of dict is show the location of people and boat. 0 is on the left side of river and 1 is on the right side of the river.
#depth: show the depth of node in the DLS search tree.
#depth type: is an integer 
#path: save a list of nodes that have been seen during the path to reach this node.
#path type: a python list. and contains nodes.
class node:
    #state is a dictionary.
    def __init__(self,state,depth,path):
        self.state = state
        self.depth = depth
        self.path = path