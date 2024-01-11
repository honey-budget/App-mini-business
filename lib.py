try:
    from tkinter import *
    import time
except ImportError as e:
    print(f'{e}')
    
'''
    creating function to verify in a label 
'''

def validate_input(label,value ,page):
    if value == '':
        label_alert = Label(page, text=f'something wrong in label of {label}', background='#FFFF00')
        label_alert.pack()
        page.after(1000, lambda: label_alert.destroy())
        return False
    return True

def remove():
    pass

