from tkinter import *
root = Tk()
x = 0
y = 0
ans = 0
root.title("calculator")

def positon(self):
    self.position = positon

numbers = """[1] [2] [3]
             [4] [5] [6]
             [7] [8] [9]"""


def addition():
    ans = x + y
    print("addition", ans)

def subtraction():
    ans = x - y
    print("subtraction", ans)

def multiplication():
    ans = x * y
    print("multiplication", ans)

def division():
    ans = x / y
    print("division", ans)

numbers= Button(root, text="[1]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[2]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[3]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[4]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[5]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[6]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[7]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[8]",command=numbers,).pack(pady=20)
numbers= Button(root, text="[9]",command=numbers,).pack(pady=20)




addition = Button(root, text="+",command="add").pack(pady=20)

substraction = Button(root, text= "-",command="sub").pack(pady=20)

multiplication = Button(root, text="*",command="mul").pack(pady=20)

division = Button(root, text="/",command="div").pack(pady=20)

Ans = Button(root, text="Ans",command="ans").pack(pady=20)

root.mainloop()