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
    struct_l = []
    type_l = ['5s', 'H', 'b', 'H', 'i', 'Q', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H', 'b', 'I', 'b', 'd', 'B', 'H', 'H',
              'I', 'B', 'f', 'h', 'f', 'H', 'I', 'i', 'Q', 'f', 'Q']
    """
    int8 -> b(1)
    uint8 -> B(1)
    int8 -> h(2)
    uint8 -> H(2)
    int8 -> i(4)
    uint8 -> I(4)
    int8 -> q(8)
    uint8 -> Q(8)
    char[] -> s(1)
    double -> d(8)
    float -> f(4)
    """
    for i in type_l:
        struct_l.append(calcsize(i))
    for i in struct_l:
        bin_l.append(bin_s[c:c + i])
        c += i
    for i in range(len(type_l)):
        final_l.append(unpack('>{}'.format(type_l[i]), bin_l[i])[0])
    return final_l


s = parser(s_in)

struct_D = Struct('D', 5)
struct_C_1 = Struct('C', 7)
struct_C_2 = Struct('C', 7)
struct_B = Struct('B', 8)
struct_A = Struct('A', 6)

struct_D.fill([s[24], s[25], [unpack('>f', s_in[s[27]  + i * 4:s[27] + 4 * (i + 1)])[0] for i in range(s[26])], s[28], s[29]])
struct_C_1.fill([s[6], s[7], s[8], s[9], s[10], s[11], s[12]])
struct_C_2.fill([s[13], s[14], s[15], s[16], s[17], s[18], s[19]])
struct_B.fill([s[0], s[1], s[2], s[3], s[4], s[5], [struct_C_1.build(), struct_C_2.build()],
               [unpack('>d', s_in[s[21] + i * 8:s[21] + 8 * (i + 1)])[0] for i in range(s[20])]])
struct_A.fill([struct_B.build(), s[22], s[23], struct_D.build(), s[30], s[31]])

output = json.dumps(struct_A.build(), indent=8)

lbl = Label(window, text=output, font=("Arial Bold", 11), padx=10, pady=5, justify=LEFT)
lbl.grid(column=0, row=0)
window.mainloop()
