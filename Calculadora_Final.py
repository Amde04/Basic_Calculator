import tkinter as tk
import ast
import operator

result_shown =False


#Functions for the operations 
def insert_value(value):
    global result_shown

    if result_shown:
        Text_operations.configure(state="normal")
        Text_operations.delete("1.0", tk.END)
        Text_operations.insert(tk.END, str(value))
        Text_operations.configure(state="disabled")

        Text_result.configure(state="normal")
        Text_result.delete("1.0", tk.END)
        Text_result.configure(state="disabled")
        result_shown = False

    else:
        Text_operations.configure(state="normal")
        Text_operations.insert(tk.END, str(value))
        Text_operations.configure(state="disabled")


def clear_operations():
    Text_result.configure(state="normal")
    Text_result.delete("1.0", tk.END)
    Text_result.configure(state="disabled")
    Text_operations.configure(state="normal")
    Text_operations.delete("1.0", tk.END)
    Text_operations.configure(state="disabled")

def operations(expresion):
    allowed_operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg
    }

    def evaluation_node(node):
        if isinstance(node, ast.BinOp):
            left = evaluation_node(node.left)
            rigth = evaluation_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operations:
                return allowed_operations[op_type](left, rigth)
            else:
                raise ValueError("Operador no encontrado")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluation_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operations:
                return allowed_operations[op_type](operand)
            else:
                raise ValueError("Error")
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Constant):
            return node.value
        else:
            raise ValueError("Error")
    parsed_expresion = ast.parse(expresion, mode="eval")
    return evaluation_node(parsed_expresion.body)



def calculate_result():
    global result_shown

    try:
        operation = Text_operations.get("1.0", tk.END).strip()
        result = operations(operation)
        Text_result.configure(state="normal")
        Text_result.delete("1.0", tk.END)
        Text_result.insert(tk.END, str(result))
        Text_result.configure(state="disabled")
        result_shown = True 

    except:
        Text_result.configure(state="normal")
        Text_result.delete("1.0", tk.END)
        Text_result.insert(tk.END, "Error")
        Text_result.configure(state="disabled")
        result_shown = True 


#Principal window of the GUI 
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("320x400+1200+350")
window.configure(bg="black")
window.resizable(False,False) # It cant chage the size of the GUI 

#Declarations of texts 
Text_result = tk.Text(window)
Text_result.place(x=10,y=100, width=180, height=80)
Text_operations = tk.Text(window)
Text_operations.place(x=10,y=5, width=300, height=80)


#Declarations of buttons and operators
button_0 = tk.Button(window, text="0", command=lambda: insert_value(0))
button_1 = tk.Button(window, text="1", command=lambda: insert_value(1))
button_2 = tk.Button(window, text="2", command=lambda: insert_value(2))
button_3 = tk.Button(window, text="3", command=lambda: insert_value(3))
button_4 = tk.Button(window, text="4", command=lambda: insert_value(4))
button_5 = tk.Button(window, text="5", command=lambda: insert_value(5))
button_6 = tk.Button(window, text="6", command=lambda: insert_value(6))
button_7 = tk.Button(window, text="7", command=lambda: insert_value(7))
button_8 = tk.Button(window, text="8", command=lambda: insert_value(8))
button_9 = tk.Button(window, text="9", command=lambda: insert_value(9))
button_point = tk.Button(window, text=".", command=lambda: insert_value("."))
button_result = tk.Button(window, text="=")
button_delete = tk.Button(window, text="Clear")
#Operators 
button_plus = tk.Button(window, text="+", command=lambda: insert_value("+"))
button_rest = tk.Button(window, text="-", command=lambda: insert_value("-"))
button_division = tk.Button(window, text="/", command=lambda: insert_value("/"))
button_multiplication = tk.Button(window, text="*", command=lambda: insert_value("*"))


button_delete.configure(command=clear_operations)
button_result.configure(command=calculate_result)

#Colors 
for color in [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, 
              button_delete, button_division, button_multiplication, button_plus, button_rest, button_point, button_result]:
    color.configure(bg="gray")


#Positions of the colors 
button_0.place(x=10,y=350,width=50,height=40)
button_point.place(x=80, y=350,width=50,height=40)
button_delete.place(x=150, y =350, width=50,height=40)
button_1.place(x=10,y=300, width=50, height=40)
button_2.place(x=80,y=300, width=50, height=40)
button_3.place(x=150,y=300,width=50,height=40)
button_4.place(x=10,y=250, width=50, height=40)
button_5.place(x=80, y=250, width=50,height=40)
button_6.place(x=150, y=250, width=50, height=40)
button_7.place(x=10, y=200, width=50, height=40 )
button_8.place(x=80, y=200, width=50, height=40)
button_9.place(x=150,y=200, width=50, height=40)
button_plus.place(x=210, y=250, width=100, height=40)
button_rest.place(x=210, y=200, width=100, height=40)
button_division.place(x=210, y=150, width=100, height=40)
button_multiplication.place(x=210, y=100, width=100, height=40)
button_result.place(x=210,y=300,width=100,height=90)


#Main loop
window.mainloop()