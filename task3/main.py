import tests
import struct
import json
from tkinter import *

window = Tk()

struct_D = {'D1': {}, 'D2': {}, 'D3': {}, 'D4': {}, 'D5': {}}
struct_C = {'C1': {}, 'C2': {}, 'C3': {}, 'C4': {}, 'C5': {}, 'C6': {}, 'C7': {}}
struct_B = {'B1': {}, 'B2': {}, 'B3': {}, 'B4': {}, 'B5': {}, 'B6': {}, 'C7': {}, 'C8': {}}
struct_A = {'A1': {}, 'A2': {}, 'A3': {}, 'A4': {}, 'A5': {}, 'A6': {}}

lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()
