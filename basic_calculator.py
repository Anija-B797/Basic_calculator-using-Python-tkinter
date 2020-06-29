from tkinter import *
from tkinter.messagebox import *

font = ("verdana", 22)


#functions

def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)


def all_clear():
    textField.delete(0,END)



def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b["text"]
    print(text)

    if text =="x":
        textField.insert(END,"*")
        return

    if text=="=":
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..",e)
            showerror("Error",e)
        return



    textField.insert(END, text)



window = Tk()
window.geometry("418x370")
window.resizable(0, 0)
window.title("calculator")

textField = Entry(window, font=font, justify=RIGHT, )
textField.pack(side=TOP, fill="both", pady=10, )

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="ridge", activebackground="orange",
                     activeforeground="white")
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind("<Button-1>", click_btn_function)

zeroBtn = Button(buttonFrame, text="0", font=font, width=5, relief="ridge", activebackground="orange",
                 activeforeground="white")
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text=".", font=font, width=5, relief="ridge", activebackground="orange",
                activeforeground="white")
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text="=", font=font, width=5, relief="ridge", activebackground="orange",
                  activeforeground="white")
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text="+", font=font, width=5, relief="ridge", activebackground="orange",
                 activeforeground="white")
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text="-", font=font, width=5, relief="ridge", activebackground="orange",
                  activeforeground="white")
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text="x", font=font, width=5, relief="ridge", activebackground="orange",
                 activeforeground="white")
multBtn.grid(row=2, column=3)

divBtn = Button(buttonFrame, text="/", font=font, width=5, relief="ridge", activebackground="orange",
                activeforeground="white")
divBtn.grid(row=3, column=3, )

clearBtn = Button(buttonFrame, text="<--", font=font, width=11, relief="ridge", activebackground="orange",
                  activeforeground="white", command = clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text="AC", font=font, width=11, relief="ridge", activebackground="orange",
                  activeforeground="white", command = all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)


#binding all btns
plusBtn.bind("<Button-1>", click_btn_function)
minusBtn.bind("<Button-1>", click_btn_function)
multBtn.bind("<Button-1>", click_btn_function)
divBtn.bind("<Button-1>", click_btn_function)
zeroBtn.bind("<Button-1>", click_btn_function)
dotBtn.bind("<Button-1>", click_btn_function)
equalBtn.bind("<Button-1>", click_btn_function)





window.mainloop()
