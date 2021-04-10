from struct import *
from tkinter import *
import json
import tests
from struct_tmp import Struct

window = Tk()
window.geometry("800x1000")

s = tests.tests_input['f31']['a']
print(s)


def parser(bin_s):
    bin_l = []
    c = 4
    struct_l = [5, 2, 1, 2, 4, 8, 2, 1, 4, 1, 8, 1, 4, 2, 1, 4, 1, 8, 1, 4, 4, 4, 1, 4, 2, 4, 4, 4, 4, 4, 5, 4]
    for i in struct_l:
        bin_l.append(bin_s[c:c + i])
        c += i
    return bin_l


def repack(f, b):
    o = str(unpack(f, b)[0])
    return o

"""
struct_A = Struct('A', 7)
struct_A.fill([1, 2, 3, 4, 5, 6, 7])
print(struct_A.build())
"""
s=parser(s)
print(s)

struct_C = dict(C1={}, C2={}, C3={}, C4={}, C5={}, C6={}, C7={})

struct_D = dict(D1={}, D2={}, D3={}, D4={}, D5={})

struct_B = dict(B1=str(repack('>5s', s[0])), B2=str(repack('>H', s[1])), B3=str(repack('b', s[2])),
                B4=str(repack('>H', s[3])), B5=str(repack('>i', s[4])), B6=str(repack('>Q', s[5])),
                B7=[struct_C, struct_C], B8={})
struct_A = dict(A1=struct_B, A2={}, A3={}, A4=struct_D, A5={}, A6={})



output = json.dumps(struct_A, indent=8)


lbl = Label(window, text=output, font=("Arial Bold", 14), padx=10, pady=5, justify=LEFT)
lbl.grid(column=0, row=0)
window.mainloop()


