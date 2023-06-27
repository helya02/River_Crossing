#-------------author: Helia Hashemi Aghdam--------------------.
#-------------River Crossing Problem-------------------------.
#-------------Use DLS algorithm for search-----------------------------.
#---------------------------------------------------.


#import neccessary files that include major functions for serch and graphic
import node #node: include node class with state, depth and path attribiutes.
import gui  #gui: include gui class with show and ShowPath finctions for show states.
import DLS  # DLS: include DLS class whith major function for searching and use DLS(Depth Limited Search) algorithm.
from tkinter import *
from tkinter import messagebox
import tkinter as tk



def main():
    #select a limited depth for DLS algorithm
    limit_depth = 17
    #set start node for statrt the search algorithm
    start= node.node({'p':'0','r':'0','m':'0',
                 'f':'0','d1':'0','d2':'0',
                 's1':'0','s2':'0', 'b':'0'},0,[])
    start.path.append(start)
    #start searching with DLS algorithm that is there in DLS class. and get a path from start node to goal node. i.e. everything is crossed.
    DLS_search = DLS.DLS(start,limit_depth)
    list_of_path = DLS_search.search()

    root = Tk()
    GUI = gui.gui(root)
    GUI.ShowPath(list_of_path)
    
if __name__ == "__main__":
    main()
