from tkinter import Tk, Label, Button, Entry, Frame, IntVar, END, W, E, Canvas
# from merge_sort import mergeSort
import random
import time

array_of_heights = []
array_of_rectangles = []
ending_location = 0
first_half_length = 0
second_half_length = 0
base_case=False
start_location=0
class SortVisualization: 
    def __init__(self, master):
        global array_of_heights
        self.master = master
        self.canvas_layout = Canvas(master, width=400, height=300)
        self.buttonframe = Frame(master, width=100, height=300)
        self.canvas_layout.pack(side="left", fill="both", expand=True)
        self.buttonframe.pack(side="right",fill="both", expand=False)
        self.sort_button = Button(self.buttonframe, text="Sort", command=lambda: self.mergeSort(array_of_heights))
        self.randomize_button = Button(self.buttonframe, text="Randomize", command=lambda: self.randomize_canvas())

        self.sort_button.grid(row=0, column=1, sticky=E)
        self.randomize_button.grid(row=1, column=1, sticky=E)

        self.buttonframe.grid_rowconfigure(100, weight=1)
        self.buttonframe.grid_columnconfigure(2, weight=1)   

    def append_to_array(self, num):
        global array_of_heights
        array_of_heights.append(num)

    def update_array(self, data, end):
        global array_of_heights
        for item in data:
            array_of_heights.remove(item)
        array_of_heights = data + array_of_heights
        
        self.canvas_layout.delete("all")
        self.draw_rectangles(array_of_heights, len(data))

    def draw_rectangles(self, height_arr, sleep_until):
        iterator = 0
        for item in height_arr:
            self.canvas_layout.create_rectangle(iterator, item, iterator+5, 300, fill="blue")
            iterator+=10
            self.master.update()
            time.sleep(.01)
    
    def randomize_canvas(self):
        global array_of_heights
        global array_of_rectangles
        array_of_heights = []
        array_of_rectangles = []
        self.canvas_layout.delete("all")
        height_range = [*range(0,310,10)]
        incrementer = 0
        box_height = []
        while height_range:
            tmp_item = random.choice(height_range)
            box_height.append(tmp_item)
            height_range.remove(tmp_item)
        for height_int in box_height:
            rect = self.canvas_layout.create_rectangle(incrementer, height_int, incrementer+5, 300, fill="blue")
            array_of_rectangles.append(rect)
            incrementer+=10
            self.append_to_array(height_int)
            print("Array_of_rectangles: {}".format(array_of_rectangles))
            x0, y0, y1, y2 = self.canvas_layout.coords(array_of_rectangles[0])
            print("x0: {}, y0: {}, x1: {}, y1: {}".format(x0, y0, y1, y2))
    
    def determine_length(self, data):
        global first_half_length
        global second_half_length
        first_half_length = data[:len(data)//2]
        second_half_length = data[len(data)//2:]

    def mergeSort(self, data=[]):
        global first_half_length
        global second_half_length
        global base_case
        if first_half_length == 0 and second_half_length == 0:
            self.determine_length(data)
        
        if len(data) == 1:
            base_case=True
            return data
        first_half = data[:len(data)//2]
        second_half = data[len(data)//2:]
        print("data: {}".format(data))
        print("first_half: {}".format(first_half))
        first_half = self.mergeSort(first_half)
        if base_case and len(first_half) >= 3:
            self.update_array(first_half, len(first_half))
        base_case=False
        second_half = self.mergeSort(second_half)
        if base_case and len(second_half) >= 3:
            self.update_array(second_half, len(second_half))
        
        return self.merge(first_half, second_half)

    def merge(self, arr_one=[], arr_two=[]):
        global base_case
        arr_tmp = []
        
        while arr_one and arr_two:
            if arr_one[0] < arr_two[0] :
                arr_tmp.append(arr_two[0])
                arr_two.pop(0)  
            else:
                arr_tmp.append(arr_one[0])
                arr_one.pop(0)

        while arr_one:
            arr_tmp.append(arr_one[0])
            arr_one.pop(0)

        while arr_two:
            arr_tmp.append(arr_two[0])
            arr_two.pop(0)
        
        if base_case:
            self.update_array(arr_tmp, len(arr_tmp))

        return arr_tmp


root = Tk()
root.geometry("500x400")
my_gui = SortVisualization(root)
root.mainloop()