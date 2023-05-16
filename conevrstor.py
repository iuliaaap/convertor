import tkinter as tk

# CONVERTOR
def C_to_F(celsius):
    return (celsius * 9/5) + 32

def F_to_C(fahrenheit):
    return (fahrenheit - 32) * 5/9
def meters_to_inches(meters):
    return meters * 39.3701

def inches_to_meters(inches):
    return inches / 39.3701

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def hours_to_seconds(hours):
    return hours * 3600

def seconds_to_hours(seconds):
    return seconds / 3600

def pascals_to_bar(pascals):
    return pascals / 100000

def bar_to_pascals(bar):
    return bar * 100000

def mps_to_kmph(mps):
    return mps * 3.6

def kmph_to_mps(kmph):
    return kmph / 3.6

def lei_to_euro(lei):
    return lei / 4.92

def euro_to_lei(euro):
    return euro * 4.92

def conversie():
    if temp_var.get():
        temp_label1 = tk.Label(third_frame, text='grade Celsius', font=('Arial', 12), bg='#55A950')
        temp_label1.grid(row=10, column=0)

        temp_label2 = tk.Label(third_frame, text='grade Fahrenheit', font=('Arial', 12), bg='#55A950')
        temp_label2.grid(row=10, column=2)

        temp_value1 = tk.Entry(third_frame, font=('Arial', 12), bg='AAF4A6')
        temp_value1.grid(row=10, column=1)

        result.config(text=f'{C_to_F(temp_value1)}')
        result.grid(row=10, column=3)


    '''if L_var.get():

    if Masa_var.get():

    if dist_var.get():

    if timp_var.get():

    if pres_var.get():

    if viteza_var.get():

    if valuta_var.get():
    '''
root3 = tk.Tk()
root3.geometry("400x400")
root3.title('Convertor de unitati de masura')
root3.resizable(False, False)  # nu mai pot sa modific dimensiunile

third_frame = tk.Frame(root3, width=400, height=400, bg='#55A950')
third_frame.grid(row=0, column=0)

empty_label = tk.Label(third_frame, text='                ',font=('Arial', 14), bg='#55A950')
empty_label.grid(row=0, column=0)

ques_label = tk.Label(third_frame, text='Alegeți tipul de convertor', font=('Arial', 14), bg='#55A950')
ques_label.grid(row=0, column=1)

temp_var = tk.BooleanVar()
temp_checkbox = tk.Checkbutton(third_frame, text="Temperatură", font=('Arial', 14), bg='#55A950', variable=temp_var)
temp_checkbox.grid(row=1, column=1)

L_var = tk.BooleanVar()
L_checkbox = tk.Checkbutton(third_frame, text="Lungime",  font=('Arial', 14), bg='#55A950', variable=L_var)
L_checkbox.grid(row=2, column=1)

Masa_var = tk.BooleanVar()
masa_checkbox = tk.Checkbutton(third_frame, text="Masă",  font=('Arial', 14), bg='#55A950', variable=Masa_var)
masa_checkbox.grid(row=3, column=1)

dist_var = tk.BooleanVar()
dist_checkbox = tk.Checkbutton(third_frame, text="Distanță",  font=('Arial', 14), bg='#55A950', variable=dist_var)
dist_checkbox.grid(row=4, column=1)

timp_var = tk.BooleanVar()
timp_checkbox = tk.Checkbutton(third_frame, text="Timp", font=('Arial', 14), bg='#55A950', variable=timp_var)
timp_checkbox.grid(row=5, column=1)

pres_var = tk.BooleanVar()
pres_checkbox = tk.Checkbutton(third_frame, text="Presiune",  font=('Arial', 14), bg='#55A950', variable=pres_var)
pres_checkbox.grid(row=6, column=1)

viteza_var = tk.BooleanVar()
viteza_checkbox = tk.Checkbutton(third_frame, text="Viteză ", font=('Arial', 14), bg='#55A950', variable=viteza_var)
viteza_checkbox.grid(row=7, column=1)

valuta_var = tk.BooleanVar()
valuta_checkbox = tk.Checkbutton(third_frame, text="Valută",  font=('Arial', 14), bg='#55A950', variable=valuta_var)
valuta_checkbox.grid(row=8, column=1)

button_conv = tk.Button(third_frame, text='Opțiuni', command=conversie)
button_conv.grid(row=9, column=1)

result = tk.Label(third_frame, text="", bg='#BD9289')


third_frame.grid_propagate(False)

root3.mainloop()