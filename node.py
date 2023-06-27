#class of node
#with the help of this class, we can create a node that saves:
#state: show On which side of the river are the people and the boat? .
#state type: state structure is a Python dictionary. the key of dict is the short name of the people and boat ,
#and the value of dict is show the location of the people and boat. 0 is on the left side of the river and 1 is on the right side of the river.
#depth: show the depth of the node in the DLS search tree.
#depth type: is an integer 
#path: save a list of nodes that have been seen during the path to reach this node.
#path type: a python list. and contains nodes.
class node:
    #state is a dictionary.
    def __init__(self,state,depth,path):
        self.state = state
        self.depth = depth
        self.path = path
