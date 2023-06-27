#DLS class for implementation the Depth Limited Algorithm.
import expansion




class DLS:
    def __init__(self,start_node,limit_depth) :
        #start_node: type= node. the root of the search tree and start state(or node).
        #limit_depth: type= integer. the limited depth for DLS. if the depth algorithm is equal to this depth, the generation of childen nodes will stop. 
        self.start_node = start_node
        self.limit_depth = limit_depth

    def isin(self, n, E):
        # a function for check n as a node is in E as a list of nodes.
        # #return boolen 
        boolean = False
        for x in E:
            if x.state== n.state:
                boolean = True
                return boolean
                break
            return boolean
        

    def search(self):
        # impelemantation of the DLS algorithm.
        # use limit depth for stop and start node for start searching algorithm.
        # Un is Unexpanded nodes
        # Ex is expanded nodes
        # return a list of nodes that show the path of searching from the start node to the goal node.
        
        Un = [self.start_node]
        Ex = []

        while(len(Un)>0):

            n_head = Un.pop(0)
            functions = expansion.expansion(n_head)
            if functions.IsGoal(n_head) == "Is Goal":
                print("finish!")
                break

            if functions.IsValid(n_head) == "Valid!" and functions.IsGoal(n_head) == "Is not Goal":
                if not(self.isin(n_head,Ex)) :
                    Ex.append(n_head)
                    if n_head.depth < self.limit_depth:
                        ChList = functions.GenerateChildren(n_head)
                        # add list of childrens at the first of Un. i.e. use DFS algorithm.
                        for i in range(len(ChList)):
                            Un.insert(0, ChList[-i-1])

        return(n_head.path)

            
        print("not found!")
