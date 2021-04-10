import json
from struct import *
from tkinter import *

import tests
from struct_tmp import Struct

window = Tk()
window.geometry("800x1000")

s_in = tests.tests_input['f31']['a']


def parser(bin_s):
    bin_l = []
    final_l = []
    c = 4
    struct_l = [5, 2, 1, 2, 4, 8, 2, 1, 4, 1, 8, 1, 2, 2, 1, 4, 1, 8, 1, 2, 2, 4, 1, 4, 2, 4, 4, 4, 4, 4, 5, 4]
    type_l = ['5s', 'H', 'b', 'H', 'i', 'Q', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H',
              'I']
    for i in struct_l:
        bin_l.append(bin_s[c:c + i])
        c += i
    for i in range(len(type_l)):
        final_l.append(unpack('>{}'.format(type_l[i]), bin_l[i])[0])
        print(i)
    return final_l


def repack(f, b):
    o = str(unpack(f, b)[0])
    return o


s = parser(s_in)
print(s)

struct_D = Struct('D', 5)
struct_C_1 = Struct('C', 7)
struct_C_2 = Struct('C', 7)
struct_B = Struct('B', 8)
struct_A = Struct('A', 6)

struct_D.fill([1, 2, 3, 4, 5])
struct_C_1.fill([s[6], s[7], s[8], s[9], s[10], s[11], s[12]])
struct_C_2.fill([s[13], s[14], s[15], s[16], s[17], s[18], s[19]])
struct_B.fill([s[0], s[1], s[2], s[3], s[4], s[5], [struct_C_1.build(), struct_C_2.build()],
               [unpack('>d', s_in[s[21] + i * 8:s[21] + 8 * (i + 1)])[0] for i in range(s[20])]])
struct_A.fill([struct_B.build(), 2, 3, struct_D.build(), 5, 6])

print(str(type(struct_A.build())))

"""
struct_C = dict(C1={}, C2={}, C3={}, C4={}, C5={}, C6={}, C7={})

struct_D = dict(D1={}, D2={}, D3={}, D4={}, D5={})

struct_B = dict(B1=str(repack('>5s', s[0])), B2=str(repack('>H', s[1])), B3=str(repack('b', s[2])),
                B4=str(repack('>H', s[3])), B5=str(repack('>i', s[4])), B6=str(repack('>Q', s[5])),
                B7=[struct_C, struct_C], B8={})
struct_A = dict(A1=struct_B, A2={}, A3={}, A4=struct_D, A5={}, A6={})
"""

output = json.dumps(struct_A.build(), indent=8)
# output = ("\n","\n",type(struct_A.build()))

lbl = Label(window, text=output, font=("Arial Bold", 13), padx=10, pady=5, justify=LEFT)
lbl.grid(column=0, row=0)
window.mainloop()
