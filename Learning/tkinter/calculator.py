import tkinter as tk

root = tk.Tk()
root.title("Calculator app") #Changing title

entry1 = tk.Entry(root,width=35,borderwidth=5)
entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def btadd(number):
    if entry1.get() == "Err":
        entry1.delete(0,tk.END)
    entry1.insert(tk.END,number)
def clear():
    entry1.delete(0,tk.END)
def get_first_opp(text,index):
    opp1 = ""
    end_char = -1
    for i in range(index-1,-1,-1):
        if text[i].isnumeric() or text[i] == ".":
            opp1 = text[i] + opp1
            end_char = i
        else:
            break
    return [opp1,end_char]
def get_second_opp(text,index):
    opp2 = ""
    end_char = -1
    for i in range(index+1,len(text)):
        if text[i].isnumeric() or text[i] == ".":
            opp2 += text[i]
            end_char = i
        else:
            break
    return [opp2,end_char]
def eval_operator(operator,text):
        index = text.find(operator)
        op1 = get_first_opp(text,index)
        op2 = get_second_opp(text,index)
        operator1 = op1[0]
        operator2 = op2[0]
        if operator1 and operator2:
            if operator == "+":
                result = float(operator1)+float(operator2)
            elif operator == "-":
                result = float(operator1)-float(operator2)
            elif operator == "*":
                result = float(operator1)*float(operator2)
            elif operator == "/":
                if float(operator2) == 0:
                    return "Undefined"
                result = float(operator1)/float(operator2)
            final = text[:op1[1]] + str(result) + text[op2[1]+1:]
            return final
def evaluate(text):
    while True:
        if "/" in text:
            text = eval_operator("/",text)
            if text == None:
                break
            continue
        if "*" in text:
            text = eval_operator("*",text)
            if text==None:
                break
            continue
        if "+" in text:
            text = eval_operator("+",text)
            if text==None:
                break
            continue
        if "-" in text:
            text = eval_operator("-",text)
            if text==None:
                break
            continue
        break
    entry1.delete(0,tk.END)
    entry1.insert(0,text)
#Define buttons
but1 = tk.Button(root,text="1",padx=40,pady=20,command=lambda: btadd(1))
but2 = tk.Button(root,text="2",padx=40,pady=20,command=lambda: btadd(2))
but3 = tk.Button(root,text="3",padx=40,pady=20,command=lambda: btadd(3))
but4 = tk.Button(root,text="4",padx=40,pady=20,command=lambda: btadd(4))
but5 = tk.Button(root,text="5",padx=40,pady=20,command=lambda: btadd(5))
but6 = tk.Button(root,text="6",padx=40,pady=20,command=lambda: btadd(6))
but7 = tk.Button(root,text="7",padx=40,pady=20,command=lambda: btadd(7))
but8 = tk.Button(root,text="8",padx=40,pady=20,command=lambda: btadd(8))
but9 = tk.Button(root,text="9",padx=40,pady=20,command=lambda: btadd(9))
but0 = tk.Button(root,text="0",padx=40,pady=20,command=lambda: btadd(0))
but_add = tk.Button(root,text="+",padx=39,pady=20,command=lambda: btadd("+"))
but_equal = tk.Button(root,text="=",padx=88,pady=20,command=lambda: evaluate(entry1.get()))
but_clear = tk.Button(root,text="Clear",padx=79,pady=20,command=clear)

but_subtract = tk.Button(root,text="-",padx=41,pady=20,command=lambda: btadd("-"))
but_multiply = tk.Button(root,text="*",padx=40,pady=20,command=lambda: btadd("*"))
but_divide = tk.Button(root,text="/",padx=40,pady=20,command=lambda: btadd("/"))


#Put the buttons on the screen
but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but0.grid(row=4,column=0)
but_add.grid(row=5,column=0)
but_clear.grid(row=4,column=1,columnspan=2)
but_equal.grid(row=5,column=1,columnspan=2)

but_subtract.grid(row=6,column=0)
but_multiply.grid(row=6,column=1)
but_divide.grid(row=6,column=2)
root.mainloop()