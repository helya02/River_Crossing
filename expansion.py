# with help of this class, we can expand a node i.e. chech validation and goal,also, generate childres nodes of a node.

import node
import copy


class expansion:
    def __init__(self,node):
        self.node = node




    #test the validation of the entered state
    def IsValid(self,n):
        #n: type= node
        #according to the rules of the problem, IsValid function return a boolean value.
        # if n is valid return Valid!
        # and if n isn't valid return not Valid!
        
        boolean_True = "Valid!"
        boolean_False = "not Valid!"
        boolean = boolean_True
        state = n.state

        #check rules of the problem:
        if not (state.get("b") == state.get("p") or state.get("b") == state.get("f") or state.get("b") == state.get("m")):
            boolean = boolean_False

            
        if state.get("s1") == state.get("m") or state.get("s2") == state.get("m"):
            if not state.get("m") == state.get("f"):
                boolean = boolean_False
                
        if (state.get("r") == state.get("m") or state.get("r") == state.get("f") or
            state.get("r") == state.get("d1") or state.get("r") == state.get("d2") or
        state.get("r") == state.get("s1") or state.get("r") == state.get("s2")):
            if state.get("r") != state.get("p"):
                boolean = boolean_False

                
        if state.get("d1") == state.get("f") or state.get("d2") == state.get("f"):
            if not state.get("f") == state.get("m"):
                boolean = boolean_False

        return boolean


    #a function for select the goal state

    def IsGoal(self,n):
        #goal state: if all of people and boat be on the right side of the river i.e. on 1area.
        # n is a node. we will check state of this node.
        #return Is Goal if n is goal and return Is not Goal if it isn't goal.
        #return boll
        boolean = "Is Goal"
        for x in n.state.keys():
            if n.state[x] == "0":
                boolean = "Is not Goal"
                break
            
        return boolean



    def GenerateChildren(self,n):
        #generate the children of the node.
        #n: is a specific node.
        #return: a list of nodes. return children of a node.
        path = n.path
        children=[]
        state = n.state
        depth_new = n.depth + 1
        
        #check validation of n
        if self.IsValid(n) == "Valid!":
            child_new = node.node(state, depth_new, path)
            #check the driver of people i.e. police,mother,father.
            for person in ["p","m","f"]:
                #if driver and boat on the same side of the river
                if n.state["b"] == n.state[person]:
                    #tuggle side of the boat and driver
                    child_new.state["b"] = str(1- int(n.state.get("b")) )
                    child_new.state[person] = str(1- int(n.state.get(person)) )
                    
                    if (self.IsValid(child_new) == "Valid!") and not(list(child_new.state.items()) in children):
                        children.append(list(child_new.state.items()))
                    #check another person can be in boat and if is a valid state, tuggle this person too.
                    for x in n.state.keys():
                        if (not( x in [person,"b"])) and (n.state.get(x) != child_new.state.get(person)):
                            
                            child_new.state[x] = str(1- int(n.state.get(x)) )
                            
                            if (self.IsValid(child_new) == "Valid!" ) and not(list(child_new.state.items()) in children):
                                
                                children.append(list(child_new.state.items()))
                            child_new.state[x] = str(1- int(child_new.state[x]))
                        
                    child_new.state[person] = str(1- int(child_new.state[person]) )
                    child_new.state["b"] = str(1- int(child_new.state["b"]) )
                    

        #create list of nodes with the obtained states
        # and the path of each one. 
        list_of_nodes = []
    
        for i in children:
          s = dict(i)
          child = node.node(s,depth_new,path)
          path_node = []

          if child not in path:
              path.append(child)
              path_node = path.copy()
                    
              child.path = path_node

          path.pop(-1)
          list_of_nodes.append(child)
            
        return list_of_nodes

