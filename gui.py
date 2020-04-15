from tkinter import Tk, Label, Button, Entry, Frame, IntVar, END, W, E, Canvas
from merge_sort import mergeSort
import random
import time

array_of_heights = []
ending_location = 0
class SortVisualization: 
    def __init__(self, master):
        global array_of_heights
        self.master = master
        self.canvas_layout = Canvas(master, width=400, height=300)
        self.buttonframe = Frame(master, width=100, height=300)
        self.canvas_layout.pack(side="left", fill="both", expand=True)
        self.buttonframe.pack(side="right",fill="both", expand=False)
        self.sort_button = Button(self.buttonframe, text="Sort", command=lambda: self.sort(array_of_heights))
        self.randomize_button = Button(self.buttonframe, text="Randomize", command=lambda: self.randomize_canvas())

        self.sort_button.grid(row=0, column=1, sticky=E)
        self.randomize_button.grid(row=1, column=1, sticky=E)

        self.buttonframe.grid_rowconfigure(100, weight=1)
        self.buttonframe.grid_columnconfigure(2, weight=1)   

    def append_to_array(self, num):
        global array_of_heights
        array_of_heights.append(num)

    def draw_rectangles(self, height_arr):
        global ending_location
        for item in height_arr:
            self.canvas_layout.create_rectangle(ending_location, item, ending_location+5, 300, fill="blue")
            ending_location+=10
            time.sleep(5)
            print("We got here")
    
    def randomize_canvas(self):
        global array_of_heights
        array_of_heights = []
        self.canvas_layout.delete("all")
        height_range = [*range(0,310,10)]
        incrementer = 0
        box_height = []
        while height_range:
            tmp_item = random.choice(height_range)
            box_height.append(tmp_item)
            height_range.remove(tmp_item)
        for height_int in box_height:
            self.canvas_layout.create_rectangle(incrementer, height_int, incrementer+5, 300, fill="blue")
            incrementer+=10
            self.append_to_array(height_int)
        
    def sort(self, height_arr):
        self.canvas_layout.delete("all")
        incrementer = 0
        sorted_order = mergeSort(height_arr)
        for item in sorted_order:
            self.canvas_layout.create_rectangle(incrementer, item, incrementer+5, 300, fill="blue")
            incrementer+=10

    # def mergeSort(self, data=[]):
    #     if len(data) == 1:
    #         return data
    #     first_half = data[:len(data)//2]
    #     second_half = data[len(data)//2:]
    #     self.canvas_layout.delete("all")
    #     first_half = self.mergeSort(first_half)
    #     second_half = self.mergeSort(second_half)

    #     return self.merge(first_half, second_half)

    # def merge(self, arr_one=[], arr_two=[]):
    #     arr_tmp = []
        
    #     while arr_one and arr_two:
    #         if arr_one[0] < arr_two[0] :
    #             arr_tmp.append(arr_two[0])
    #             arr_two.pop(0)  
    #         else:
    #             arr_tmp.append(arr_one[0])
    #             arr_one.pop(0)

    #     while arr_one:
    #         arr_tmp.append(arr_one[0])
    #         arr_one.pop(0)

    #     while arr_two:
    #         arr_tmp.append(arr_two[0])
    #         arr_two.pop(0)
        
    #     if len(arr_tmp) == 2:    
    #         self.draw_rectangles(arr_tmp)
    #     return arr_tmp


root = Tk()
root.geometry("500x400")
my_gui = SortVisualization(root)
root.mainloop()