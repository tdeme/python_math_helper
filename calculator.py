import tkinter as tk


#Defining the font and color values
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        #Setup window
        self.window = tk.Tk()
        self.window.geometry("400x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        #Initialize variables to hold the current expression and total expression
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        
        #Create a dictionary to hold the digits and their grid values
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), ".":(4,2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "+": "+", "-": "-"}
        self.buttons_frame = self.create_buttons_frame()            

        #Create the buttons
        self.buttons_frame.rowconfigure(0,weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
            
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()


    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
        bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)

        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
        bg=LIGHT_GREY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)

        label.pack(expand=True, fill="both")

        return total_label, label


    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame


    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()


    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
            borderwidth=0, command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)


    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)

            button.grid(row=i,column=4, sticky=tk.NSEW)
            i+=1


    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)

        button.grid(row=0,column=1, columnspan=3, sticky=tk.NSEW)

    
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)

        button.grid(row=4,column=3, columnspan=2, sticky=tk.NSEW)


    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame


    def update_total_label(self):
        self.total_label.config(text=self.total_expression)


    def update_label(self):
        self.label.config(text=self.current_expression)


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()