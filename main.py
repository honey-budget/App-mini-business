from tkinter import *
def add_items(NAME, WEIGHT,PRICE_PER_WEIGHT):
    RESULT = WEIGHT * PRICE_PER_WEIGHT    
    add_items = Tk()
    
    add_items.geometry("800x400")

    Label(add_items, text=f'{NAME}', font='Helvetica 18 bold').place(
                                        x = 40,
                                        y = 30)
    
    Label(add_items, text="Weight : ").place(
                                        x = 60,
                                        y = 80
    )
    
    
    Label(add_items, text=f'{WEIGHT}').place(
                                        x = 110,
                                        y = 80
    )

    Label(add_items, text="kg").place(
                                        x = 160,
                                        y = 80
    )

    Label(add_items, text="Baht/kg").place(
                                        x = 300,
                                        y = 80 
    )

    Label(add_items, text=f'{PRICE_PER_WEIGHT}').place(
                                        x = 230,
                                        y = 80
    )
    
    Label(add_items, text="Baht").place(
                                        x = 480,
                                        y = 80 
    )


    Label(add_items, text=f'{RESULT}').place(
                                        x = 400,
                                        y = 80
    )
    add_items.mainloop()

name = str(input("Name : "))
weight = float(input("Weight : "))
price_per_weight = float(input("price : "))
show = add_items(name, weight, price_per_weight)



