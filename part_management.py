from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(),
                            retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


# Create window object
app = Tk()

# Updated window styling
app.title('Part Manager')
app.geometry('1000x500')
app.config(bg="#f7f8fa")  # Light grey-blue background

# Header
header = Label(app, text="Part Manager", font=('Arial', 20, 'bold'), bg="#4CAF50", fg="white", pady=10)
header.grid(row=0, column=0, columnspan=4, sticky="ew")

# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('Arial', 12, 'bold'), pady=10, bg="#f7f8fa", fg="#333")
part_label.grid(row=1, column=0, sticky=W, padx=20)
part_entry = Entry(app, textvariable=part_text, font=('Arial', 12), width=30, bg="#ffffff", relief=SOLID)
part_entry.grid(row=1, column=1, padx=20, pady=10)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('Arial', 12, 'bold'), pady=10, bg="#f7f8fa", fg="#333")
customer_label.grid(row=1, column=2, sticky=W, padx=20)
customer_entry = Entry(app, textvariable=customer_text, font=('Arial', 12), width=30, bg="#ffffff", relief=SOLID)
customer_entry.grid(row=1, column=3, padx=20, pady=10)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('Arial', 12, 'bold'), pady=10, bg="#f7f8fa", fg="#333")
retailer_label.grid(row=2, column=0, sticky=W, padx=20)
retailer_entry = Entry(app, textvariable=retailer_text, font=('Arial', 12), width=30, bg="#ffffff", relief=SOLID)
retailer_entry.grid(row=2, column=1, padx=20, pady=10)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('Arial', 12, 'bold'), pady=10, bg="#f7f8fa", fg="#333")
price_label.grid(row=2, column=2, sticky=W, padx=20)
price_entry = Entry(app, textvariable=price_text, font=('Arial', 12), width=30, bg="#ffffff", relief=SOLID)
price_entry.grid(row=2, column=3, padx=20, pady=10)

# Parts List (Listbox)
parts_list = Listbox(app, height=10, width=70, border=0, font=('Arial', 12), bg="#ffffff", relief=SOLID)
parts_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app, orient=VERTICAL)
scrollbar.grid(row=4, column=3, sticky='ns', padx=(0, 20))
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Button styling
button_style = {'font': ('Arial', 12, 'bold'), 'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45A049',
                'width': 18, 'height': 2, 'relief': RAISED}

add_btn = Button(app, text='Add Part', command=add_item, **button_style)
add_btn.grid(row=3, column=0, pady=10)

remove_btn = Button(app, text='Remove Part', command=remove_item, **button_style)
remove_btn.grid(row=3, column=1, pady=10)

update_btn = Button(app, text='Update Part', command=update_item, **button_style)
update_btn.grid(row=3, column=2, pady=10)

clear_btn = Button(app, text='Clear Input', command=clear_text, **button_style)
clear_btn.grid(row=3, column=3, pady=10)

# Populate data
populate_list()

# Start program
app.mainloop()
