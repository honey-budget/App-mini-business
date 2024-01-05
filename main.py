from tkinter import *

def items():
    #RESULT = WEIGHT * PRICE_PER_WEIGHT   
    '''
    # old version     
    title_info =Label(main, text=f'{NAME}', font='Helvetica 18 bold')
    info = Label(main, text=f'Weight :{WEIGHT:.2f} kg       Price : {PRICE_PER_WEIGHT:.2f} Baht/kg        Total : {RESULT:.2f} Baht')

    # place that labels

    title_info.grid(column=0, row=1)
    info.grid(column=1, row=1, padx=100, pady=10)
    
    '''
    # input data
    TITLE = title_entry.get()
    WEIGHT = float(entry_weight.get())
    PRICE_PER_WEIGHT = float(entry_price.get())

    TOTAL =WEIGHT * PRICE_PER_WEIGHT
    result =f'Title : {TITLE}, Weight : {WEIGHT:.2f}, PRICE : {PRICE_PER_WEIGHT:.2f} Total : {TOTAL:.2f}'
    label_total = Label(main, text=result)
    label_total.pack()



main = Tk()


label_title = Label(main, text='Name :')
title_entry = Entry(main, bd=2)
label_weight = Label(main, text='Weight:')
entry_weight = Entry(main, bd=2)
label_price = Label(main, text='Price:')
entry_price = Entry(main, bd=2)

# pack anything right here
label_title.pack()
title_entry.pack()
label_weight.pack()
entry_weight.pack()
label_price.pack()
entry_price.pack()


btn_add_items = Button(main, text='Add', command=items).pack()



#name = str(input("Name : "))
#weight = float(input("Weight : "))
#price_per_weight = float(input("price : "))
#show = items(name, weight, price_per_weight)


main.mainloop()
