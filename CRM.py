from customtkinter import CTk, CTkButton, CTkFrame, CTkCanvas, CTkLabel, CTkFont, CTkCheckBox,CTkImage, CTkScrollbar, CTkComboBox, CTkTextbox, CTkScrollableFrame
from tkinter import *
from PIL import Image



Font_revenue = ("Arial", 30)
class Crm:
    def __init__(self):
        self.window = CTk()
        self.window.title("Bulldog Auto & Turf")
        self.window.resizable(True, True)
        self.window.attributes("-fullscreen", True)
        self.revenue = 15424
        self.expenses = 7246
        if self.window.winfo_screenheight() < 800:
            self.Font_tuple = ("Helvetica", 30, "bold")
        else:
            self.Font_tuple = ("Helvetica", 55, "bold")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        logo = PhotoImage(file="Pictures/logo.png")
        background = PhotoImage(file="Pictures/background.png")
        background = background.zoom(2,2)
        self.bg = Label(self.window, image=background)
        self.bg.grid(column=0, row=0, columnspan=4, rowspan=4)
        self.canvas_date = CTkFrame(self.window, border_color="black", border_width=3, corner_radius=0, fg_color="White")
        self.canvas_date.grid(row=0, column=0, sticky="NW", pady=(15, 0), padx=(15, 15))
        self.date_text = CTkLabel(self.canvas_date, text="5/10/2023\nWednesday", font=Font_revenue, fg_color="White", text_color="black")
        self.date_text.pack(padx=10, pady=10)
        self.canvas_logo = CTkFrame(self.window, border_color="White", fg_color="black", border_width=5, corner_radius=0)
        self.canvas_logo.grid(row=0, column=1)
        self.canvas_revenue = CTkFrame(self.window, border_color="black", fg_color="#8E8C7F", border_width=10, corner_radius=0)
        self.canvas_revenue.grid(row=1, column=1)
        self.canvas_alerts = CTkFrame(self.window, border_color="red", fg_color="black", border_width=3, corner_radius=0)
        self.canvas_alerts.grid(row=0, column=2, pady=(0, 2), rowspan=2, sticky="nsew")
        self.canvas_buttons = CTkFrame(self.window, border_color="gray", corner_radius=0, border_width=0, fg_color="black")
        self.canvas_buttons.grid(row=2, column=0, columnspan=3, sticky="nsew")

        self.logo = Label(self.canvas_logo, image=logo)
        self.logo.pack(expand=True)

        #  Revenue Canvas Calculations and check buttons

        self.revenue_text = CTkLabel(self.canvas_revenue, text="Last week's revenue:", text_color="black", font=Font_revenue)
        self.revenue_text.grid(column=1, pady=(50, 5), padx=(5,0))
        self.expenses_text = CTkLabel(self.canvas_revenue, text="Last week's expenses:",text_color="black", font=Font_revenue)
        self.expenses_text.grid(column=1, row=1, pady=(5, 5), padx=(23,0))
        self.expenses_text = CTkLabel(self.canvas_revenue, text="Last week's net income:",text_color="black", font=Font_revenue)
        self.expenses_text.grid(column=1, row=2, pady=(5, 75), padx=(38,0))

        self.revenue_number = CTkLabel(self.canvas_revenue, text=f"${self.revenue}" ,text_color="green", font=Font_revenue)
        self.revenue_number.grid(column=2, row=0, pady=(50, 5), padx=(0, 15))
        self.expenses_number = CTkLabel(self.canvas_revenue, text=f"${self.expenses}" ,text_color="red", font=Font_revenue)
        self.expenses_number.grid(column=2, row=1, pady=(5, 5), padx=(0, 15))
        self.expenses_number = CTkLabel(self.canvas_revenue, text=f"${self.revenue - self.expenses}",text_color="green", font=Font_revenue)
        self.expenses_number.grid(column=2, row=2, pady=(5, 75), padx=(0, 15))

        # Bottom Main function Buttons

        self.employee_button = CTkButton(self.canvas_buttons, text="Employees", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.employee_button.grid(column=0, row=0, padx=(150, 15), pady=(50, 0))

        self.expenses_button = CTkButton(self.canvas_buttons, text="Expenses", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.expenses_button.grid(column=1, row=0, padx=(15, 15), pady=(50, 0))

        self.receipt_button = CTkButton(self.canvas_buttons, text="Receipt", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.receipt_button.grid(column=2, row=0, padx=(15, 150), pady=(50, 0))

        self.orders_button = CTkButton(self.canvas_buttons, text="Orders", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.orders_button.grid(column=0, row=1, padx=(150, 15), pady=(50, 0))

        self.revenue_button = CTkButton(self.canvas_buttons, text="Revenue", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.revenue_button.grid(column=1, row=1, padx=(15, 15), pady=(50, 0))

        self.stock_button = CTkButton(self.canvas_buttons, text="Stock", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.stock_button.grid(column=2, row=1, padx=(15, 150), pady=(50, 0))

        self.prices_button = CTkButton(self.canvas_buttons, text="Prices", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.prices_button.grid(column=0, row=2, padx=(150, 15), pady=(50, 10))

        self.customers_button = CTkButton(self.canvas_buttons, text="Customers", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.customers_button.grid(column=1, row=2, padx=(15, 15), pady=(50, 10))

        self.alert_button = CTkButton(self.canvas_buttons, text="Alerts", fg_color="white", font=self.Font_tuple, text_color="black", width=300)
        self.alert_button.grid(column=2, row=2, padx=(15, 150), pady=(50, 10))

        self.canvas_buttons.columnconfigure(0, weight=1)
        self.canvas_buttons.rowconfigure(0, weight=1)
        self.canvas_buttons.columnconfigure(1, weight=1)
        self.canvas_buttons.columnconfigure(2, weight=1)
        self.canvas_buttons.rowconfigure(1, weight=1)
        self.canvas_buttons.rowconfigure(2, weight=1)

        self.alerts_text = CTkLabel(self.canvas_alerts, text="Only 1 #30567 Crossbrace left in stock", text_color="white", font=("Arial", 20), wraplength=250)
        self.alerts_text.pack(padx=15, pady=(25,0))
        self.alerts1_text = CTkLabel(self.canvas_alerts, text="Only 2 #64357 Fuel Filter left in stock", text_color="white", font=("Arial", 20), wraplength=250)
        self.alerts1_text.pack(padx=15, pady=(25,0))

        self.window.mainloop()