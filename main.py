#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from tkinter import *
    import time
    import lib
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

        #label_error = Label(main, text=f'[0] {e}', background='#FF0000')
        #label_error.pack()
        #main.after(1000, lambda: label_error.destroy())

        print(f'[0]:{e}')
    try:
        if not lib.validate_input("title", TITLE, main) or not lib.validate_input("weight", WEIGHT, main) or not lib.validate_input("price/weight", PRICE_PER_WEIGHT, main):
            hidden_frsit_btn = frist_remove.pack_forget()
            small_label = Label(main, text=f'could you check the information on the labels pls', font=("Helvetica", 8), fg='#FF0000')
            small_label.pack()
            main.after(1500, lambda: small_label.destroy())
    
    except UnboundLocalError as e:

        label_error = Label(main, text=f'{e}', background='#FF0000')
        label_error.pack()
        main.after(1000, lambda: label_error.destroy())

    else:
        try:

            result =f'Title : {TITLE}  Weight : {WEIGHT:.2f} kg PRICE : {PRICE_PER_WEIGHT:.2f} Baht/kg Total : {TOTAL:.2f} Baht'
            label_total = Label(main, text=result)
            label_total.pack()

        except UnboundLocalError as e:

            label_error = Label(main, text=f'{e}', background='#FF0000')
            label_error.pack()
            main.after(1000, lambda: label_error.destroy())
        
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
                        TITLE = change_title.get()
                        WEIGHT = float(change_weight.get())
                        PRICE_PER_WEIGHT = float(change_price.get())
                        TOTAL = WEIGHT * PRICE_PER_WEIGHT
                    except ValueError as e:
                        change_label_error = Label(main, text=f'[1]:{e}', background='#FF0000')
                        change_label_error.pack()
                        main.after(1000, lambda: change_label_error.destroy())

                    if not lib.validate_input("title", TITLE, main) or not lib.validate_input("weight", WEIGHT, main) or not lib.validate_input("price/weight", PRICE_PER_WEIGHT, main):

                        small_label = Label(main, text=f'could you check the information on the labels pls', font=("Helvetica", 8), fg='#FF0000')
                        small_label.pack()
                        main.after(1500, lambda: small_label)
                    else:
                        try:
                                
                            NEW_RESULT = f'Title :{TITLE} Weight : {WEIGHT:.2f} kg Price : {PRICE_PER_WEIGHT:.2f} Baht/kg Total :{TOTAL:.2f}' 
                            new_label_total = Label(main, text=NEW_RESULT)
                            new_label_total.config(text=NEW_RESULT)
                            new_label_total.pack()

                        except UnboundLocalError as e:
                            label_error = Label(main, text=f'{e}', background='#FF0000')
                            label_error.pack()
                            main.after(1000, lambda: label_error.destroy())
                         
                        # hidden-label-and-entry  
                        hidden_old_label_total = label_total.pack_forget()
                        hidden_change_label = change_label.pack_forget()
                        hidden_change_title = change_title.pack_forget()
                        hidden_change_weight = change_weight.pack_forget()
                        hidden_change_price = change_price.pack_forget()
                        # hidden-btn 

                        '''
                           #! req : after click save button then show change-btn & remove-btn  
                           #! req : when click save again, remove old result_total and old btn-save 
                        '''
                        
                        hidden_save_btn = btn_save_new_items.pack_forget()
                    # function in changing page
                    def btn_remove():
                        if not label_total :
                            alert_btn_remove = Label(main, text='No total').pack()
                            main.after(1000, lambda: alert_btn_remove.destroy())
                        else:
                            # Remove 
                            hidden_old_label_total = label_total.pack_forget()
                            hidden_remove_btn = btn_remove_items.pack_forget()
                            hidden_new_label_total = new_label_total.pack_forget()
                            hidden_change_items_btn =btn_change_items_btn.pack_forget()

                    # btn reomve in chaning mode
                    btn_remove_items = Button(main, text='Remove btn_remove_items', command=btn_remove) # btn-Remove (btn_remove_items)
                    btn_remove_items.pack()
                # btn save
                btn_save_new_items = Button(main, text='save', command=btn_save)
                btn_save_new_items.pack()



            except ValueError as e:

                change_label_error = Label(main, text=f'[2]:{e}', background='#FF0000')
                change_label_error.pack()
                main.after(1000, lambda: change_label_error.destroy())

        
        def frist_remove():
            hidden_label_total = label_total.pack_forget()
            hidden_frist_remove = btn_frist_reomve.pack_forget()
        
        # btn-remove on main
        btn_frist_reomve = Button(main, text="Remove btn_frist_remove", command=frist_remove)
        btn_frist_reomve.pack()
        #btn change
        btn_change_items_btn_click = BooleanVar()
        btn_change_items_btn_click.set(False)
        btn_change_items_btn = Button(main, text='Change', command=change_items)
        btn_change_items_btn.pack()
     




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
checkbox_data = Checkbutton(main, text='Import data', onvalue=1, offvalue=0)
checkbox_data.pack()
main.mainloop()
