import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x657")
        self.window.resizable(1,1)
        self.window.title("Calculator")

        self.full_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.full_label, self.label = self.create_label()
        self.buttons_frame = self.create_buttons_frame ()

        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,3)
        }
        self.operations =  {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}

        self.create_digit_buttons()
        self.create_button_operation()
        self.create_clearall_button()
        self.create_equals_button()
        self.create_delete_button()
        self.create_clear_button()
        self.create_plus_minus_button()
        self.bind_keys()
        
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.equals())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
        
        
    def create_plus_minus_button(self):
        button =  tk.Button(self.buttons_frame,text="+/-",bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command=self.plus_minus)
        button.grid(row=4,column=1,sticky=tk.NSEW)


    def create_clear_button(self):
         button =  tk.Button(self.buttons_frame,text="CE",bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command = self.clear_current_button)
         button.grid(row=0,column=1,sticky=tk.NSEW)

    def equals(self):
        self.full_expression += self.current_expression
        self.update_full_expression() 
        try:
            self.current_expression = str(eval(self.full_expression))
            self.full_expression = ""
            self.update_current_expression()
        except Exception as e:
            self.current_expression = "Error"
            self.update_current_expression()
            self.update_full_expression()


    def create_equals_button(self):
         button =  tk.Button(self.buttons_frame,text="=",bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command=self.equals)
         button.grid(row=4,column=4,sticky=tk.NSEW)

    def delete(self):
        if self.current_expression != "Error":
            self.current_expression = self.current_expression[:-1]
        self.update_current_expression()

    def create_delete_button(self):
        button =  tk.Button(self.buttons_frame,text="DEL",bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command=self.delete)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    def clear_current_button(self):
        self.current_expression = ""
        self.update_current_expression()

    def clear_all_button(self):
        self.current_expression = ""
        self.full_expression = ""
        self.update_current_expression()
        self.update_full_expression()

    def create_clearall_button(self):
         button =  tk.Button(self.buttons_frame,text="C",bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command = self.clear_all_button)
         button.grid(row=0,column=2,sticky=tk.NSEW)

    def append_operator(self,operator):
        self.current_expression += operator
        self.full_expression += self.current_expression
        self.current_expression = ""
        self.update_full_expression()
        self.update_current_expression()

    def create_button_operation(self):
        i = 0
        for operator,symbol in self.operations.items():
            button =  tk.Button(self.buttons_frame,text=symbol,bg="white",fg="#25265E",font=("Arial",10),borderwidth=0,command = lambda x=operator:self.append_operator(x) )
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i += 1


    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,text=str(digit),bg="white",fg="#25265E",borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    
    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_current_expression()  

    
    def create_label(self):
        full_expression_label = tk.Label(self.display_frame, text=self.full_expression,anchor=tk.E,bg="#F5F5F5",fg="#25265E",padx=24,font=("Arial",16))
        full_expression_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression,anchor=tk.E,bg="#F5F5F5",fg="#25265E",padx=24,font=("Arial",40))
        label.pack(expand=True, fill="both")

        return full_expression_label,label   


    def create_display_frame(self):
        frame = tk.Frame(self.window, height=500, bg = "#F5F5F5",borderwidth=0)
        frame.pack(expand=True, fill="both")
        return frame



    def create_buttons_frame(self):
       button = tk.Button(self.window,)
       button.pack(expand=True,fill="both")
       return button

    
    def update_full_expression(self):
        expression = self.full_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.full_label.config(text=expression)


    def update_current_expression(self):
        self.label.config(text=self.current_expression[:11])



    def run(self):
        self.window.mainloop()  


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
