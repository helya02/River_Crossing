#class for graphic user inerface.
#with help of this class, we can show the state of nodes. and visualising the path of searching.


from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial
import random
import expansion


class gui:
    def __init__(self,TK):
        #TK is a root for tkinter window
        #set the GUI of the problem.
        self.TK = TK
        TK.geometry("200x500")
      
        TK.title('crossing the river')
        TK.config(bg="green")

        # area0: the left side of river
        self.area0 = Frame(TK, bg = "green")
        self.area0.grid(row=0 , column = 1, padx=20, pady=10)
        self.area0Label = Label(TK, text='0 Area').grid(row=1, column=1)
        # set the river
        self.river = Frame(TK,  width=20,  height=  400,  bg='blue').grid(row=0,  column=2,  padx=2,  pady=10)
        
        #area1: the right side of river
        self.area1 = Frame(TK, bg = "green")
        self.area1.grid(row = 0, column = 3, padx=20, pady=10)
        self.area1Label = Label(TK, text='1 Area').grid(row=1, column=3)
        
        
    def show(self, node_state, condition):
        #for show and visualization state of a node.
        #node_state: type = is a node object
        #condition: type = is an integer, 0 or 1. 0 for show the state and 1 for clear the state.
        #return: a graphic user interface that shows state of a node.
        
        area0array=[]
        area1array =[]
        if condition == 0:
            for x in node_state.state.keys():
                if node_state.state[x] == '0':
                    area0array.append(x)
                elif node_state.state[x] == '1':
                    area1array.append(x)

            area0arr = area0array
            area1arr = area1array

            for i in range(len(area0arr)):
                j = ((i+10)*30)-200
                p_in0 = Label(self.area0,text=area0arr[i], bg = "green")
                p_in0.place(x = 250+random.random() , y= j )
                p_in0.pack()
                
            for i in range(len(area1arr)):
                j = ((i+10)*30)-200
                p_in1 = Label(self.area1,text=area1arr[i], bg = "green")
                p_in1.place(x = 350+2 * random.random() , y= j)
                p_in1.pack()


            #call IsValid and IsGoal functions
            #show that this node is valid and in goal or not.
            #expansion class contains IsValid(parametr) and IsGoal(parametr) that chech validation of node and is goal or not.

            calls = expansion.expansion(node_state)
                
            vali_message = messagebox.showinfo("valid", calls.IsValid(node_state))
            goal_message = messagebox.showinfo("valid", calls.IsGoal(node_state))

            

                
        # clear the GUI.
        if condition != 0:
            area0arr = []
            area1arr = []
            for widget in self.area0.winfo_children():
                widget.destroy()
            for widget in self.area1.winfo_children():
                widget.destroy()
      


#show different states
    def ShowPath(self,nodes):
        # show the differnt state of nodes in a list.
        # show a state on GUI and after 1s clear the window and show another state of list.
        #nodes: type: a list of nodes.
        #return: show graphic user interface.
        for i in range(len(nodes)):
            self.show(nodes[i],0)
            self.TK.after(1000, self.show(nodes[i],1))
