from tkinter import Tk, Entry, Button, Label

def multiply_entries():
    try:
        # ดึงค่าจาก entry และแปลงเป็นตัวเลข
        weight = float(entry_weight.get())
        price = float(entry_price.get())

        # คำนวณผลคูณ
        result = weight * price

        # แสดงผลลัพธ์
        result_label.config(text=f'Result: {result}')
    except ValueError:
        result_label.config(text='Please enter valid numbers')

# สร้างหน้าต่าง Tkinter
root = Tk()
root.title('Multiply Entries')

# Entry สำหรับ weight
label_weight = Label(root, text='Weight:')
label_weight.pack()
entry_weight = Entry(root)
entry_weight.pack()

# Entry สำหรับ price
label_price = Label(root, text='Price:')
label_price.pack()
entry_price = Entry(root)
entry_price.pack()

# Button สำหรับคำนวณ
calculate_button = Button(root, text='Calculate', command=multiply_entries)
calculate_button.pack()

# Label สำหรับแสดงผลลัพธ์
result_label = Label(root, text='Result: ')
result_label.pack()

# แสดงหน้าต่าง Tkinter
root.mainloop()
