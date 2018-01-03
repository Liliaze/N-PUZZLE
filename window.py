#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk

class Window:
    
    def __init__(self, algoList, heuriList):
        self.window = tk.Tk()
        #self.create_frame()
    
    def create_grid(self, grid, size):
        for x in range(size):
            for y in range(size):
                tk.Label(self.top, text='%d' % (grid[x][y]), borderwidth=1).grid(row=x, column=y)
    
    def create_frame(self):
        self.top = tk.Frame(self.window, width=300, height=100, borderwidth=2)
        self.top.pack(side=tk.TOP)
        self.bottom = tk.Frame(self.window, width=300, height=100, borderwidth=2, background="red")
        self.bottom.pack(side=tk.BOTTOM)
    """
        self.frameList = {}
        self.frameList["top"] = tk.Frame(self.window, width=300, height=100, borderwidth=1)
        self.frameList["top"].pack(side=tk.TOP)
        self.frameList["algo"] = tk.LabelFrame(self.window, text="Choose Algo", width=200, height=100, pady=200, borderwidth=1)
        self.frameList["algo"].pack(side=tk.LEFT)
        self.frameList["heuri"] = tk.LabelFrame(self.window, text="Choose Heuristique", width=200, height=200, pady=200, padx= 305, borderwidth=1)
        self.frameList["heuri"].pack(side=tk.LEFT)
        self.frameList["grid"] = tk.LabelFrame(self.window, text="Grid", width=200, height=200, borderwidth=1)
        self.frameList["grid"].pack(side=tk.BOTTOM)
        self.frameList["bottom"] = tk.Frame(self.window, width=300, height=100, borderwidth=1)
        self.frameList["bottom"].pack(side=tk.BOTTOM)
    
    def create_widget(self):
        self.widget = {}
        welcome_msg = self.solver.sayHello()
        self.widget["welcome"] = tk.Label(self.frameList["top"], text=welcome_msg)
        self.widget["title"] = tk.Label(self.window, text="NPUZZLE")
        self.widget["start"] = tk.Button(self.window, text="Start", command=self.window.quit)
        self.widget["quit"] = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.widget["test"] = tk.Button(self.window, text="Test", command=self.window.quit)
    """
    def create_widget(self, algoList, heuristicList):
        self.algoList = self.create_listBox(algoList, self.bottom)
        self.algoList.pack()
        self.heuriList = self.create_listBox(heuristicList, self.bottom)
        self.heuriList.pack()
    
    def create_listBox(self, myList, frame):
        Listbox = tk.Listbox(frame)
        for text in myList:
            Listbox.insert(tk.END, text[0])
        return Listbox
    """    
    def add_dict(self, dico):
       for elem in dico.values():
           elem.pack()
"""
    def askConfigI(self):
        return self.askAlgoI(), self.askHeuriI()
    
    def askAlgoI(self):
        #return self.algoList.curselection()
        return 0
        
    def askHeuriI(self):
        #return heuriList.get(self.heuriList.curselection())
        return 0
    
    def start(self, size, gridFirst, gridGoal, algoList, heuriList):
        self.create_frame()
        self.create_grid(gridFirst, size)
        self.create_widget(algoList, heuriList)
        #self.add_dict(self.frameList)
        #self.add_dict(self.widget)
        self.window.mainloop()
    
    def quit(self):
        self.window.quit()