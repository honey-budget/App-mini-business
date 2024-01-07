try:
    from tkinter import *
    import time
except ImportError as e:
    print(f'{e}')


def items():

    # input data
    try:
        TITLE = title_entry.get()
        WEIGHT = float(entry_weight.get())
        PRICE_PER_WEIGHT = float(entry_price.get())
        TOTAL =WEIGHT * PRICE_PER_WEIGHT
    except ValueError as e:
        label_error = Label(main, text=f'{e}', background='#FF0000')
        label_error.pack()
        main.after(2000, lambda: label_error.destroy())
    if TITLE == '' or WEIGHT == '' or PRICE_PER_WEIGHT == '':
        label_alert_new_title = Label(main, text='Something wrong ', background='#FFFF00')
        label_alert_new_title.pack()
        main.after(1000, lambda: label_alert_new_title.destroy())
    else:

        result =f'Title : {TITLE}  Weight : {WEIGHT:.2f} kg PRICE : {PRICE_PER_WEIGHT:.2f} Baht/kg Total : {TOTAL:.2f} Baht'
        label_total = Label(main, text=result)
        label_total.pack()
        def change_items():
            if not btn_change_items_btn_click.get():
                btn_change_items_btn_click.set(True)
            try:
                change_label = Label(main, text=f'old name : {TITLE}')
                change_title = Entry(main,bd=2)
                change_weight = Entry(main, bd=2)
                change_price = Entry(main, bd=2)
                # pack()
                change_label.pack()
                change_title.pack()
                change_weight.pack()
                change_price.pack()
                
                def btn_save():
                    #generating new total / info
                    try:
                        NEW_TITLE = change_title.get()
                        NEW_WEIGHT = float(change_weight.get())
                        NEW_PRICE_WEIGHT = float(change_price.get())
                        NEW_TOTAL = NEW_WEIGHT * NEW_PRICE_WEIGHT

                    except ValueError as e:
                        change_label_error = Label(main, text=f'{e}', background='#FF0000')
                        change_label_error.pack()
                        main.after(1000, lambda: change_label_error.destroy())

                    if NEW_TITLE == '' or NEW_WEIGHT == '' or NEW_PRICE_WEIGHT == '':

                        label_alert_new_title = Label(main, text='Something wrong ', background='#FFFF00')
                        label_alert_new_title.pack()
                        main.after(1000, lambda: label_alert_new_title.destroy())

                    else:

                        NEW_RESULT = f'Title :{NEW_TITLE} Weight : {NEW_WEIGHT:.2f} kg PRICE : {NEW_PRICE_WEIGHT:.2f} Baht/kg Total :{NEW_TOTAL:.2f}' 
                        new_label_total = Label(main, text=NEW_RESULT)
                        new_label_total.pack()
                        # hidden-label-and-entry  
                        hidden_old_label_total = label_total.pack_forget()
                        hidden_change_label = change_label.pack_forget()
                        hidden_change_title = change_title.pack_forget()
                        hidden_change_weight = change_weight.pack_forget()
                        hidden_change_price = change_price.pack_forget()
                        # hidden-btn 

                        '''
                           #! req : after click a save button then show change-btn & remove-btn  
                        '''

                        hidden_remove_btn = btn_remove_items.pack_forget() 
                        hidden_change_items_btn =btn_change_items_btn.pack_forget()
                        hidden_save_btn = btn_save_new_items.pack_forget()

                # btn save
                btn_save_new_items = Button(main, text='save', command=btn_save)
                btn_save_new_items.pack()

            except ValueError as e:

                change_label_error = Label(main, text=f'{e}', background='#FF0000')
                change_label_error.pack()
                main.after(1000, lambda: change_label_error.destroy())


        #btn change
        btn_change_items_btn_click = BooleanVar()
        btn_change_items_btn_click.set(False)
        btn_change_items_btn = Button(main, text='Change', command=change_items)
        btn_change_items_btn.pack()

        def btn_remove():
            # Remove 
            hidden_old_label_total = label_total.pack_forget()
            hidden_remove_btn = btn_remove_items.pack_forget()
            hidden_change_items_btn =btn_change_items_btn.pack_forget()
        btn_remove_items = Button(main, text='Remove', command=btn_remove)
        btn_remove_items.pack()





main = Tk()


label_title = Label(main, text='Name :')
title_entry = Entry(main, bd=2)
label_weight = Label(main, text='Weight:')
entry_weight = Entry(main, bd=2)
label_price = Label(main, text='Price:')
entry_price = Entry(main, bd=2)


click_btn_Intvar = IntVar()
value_click = click_btn_Intvar.get()

# pack anything right here

label_title.pack()
title_entry.pack()
label_weight.pack()
entry_weight.pack()
label_price.pack()
entry_price.pack()


btn_add_items = Button(main, text='Add', command=items).pack()

main.mainloop()
