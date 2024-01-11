import tkinter as tk

def update_label():
    new_data = entry.get()
    label.config(text=f'Weight x Price: {new_data}')

def clear_label():
    label.config(text='Weight x Price: ')

# สร้างหน้าต่าง
root = tk.Tk()
root.title("Weight x Price Label")

# สร้าง Entry สำหรับรับข้อมูล
entry = tk.Entry(root)
entry.pack(pady=10)

# สร้าง Label เริ่มต้น
label = tk.Label(root, text='Weight x Price: ')
label.pack(pady=10)

# สร้าง Button สำหรับอัพเดทข้อมูล
update_button = tk.Button(root, text='Update', command=update_label)
update_button.pack(pady=5)

# สร้าง Button สำหรับลบข้อมูล
clear_button = tk.Button(root, text='Clear', command=clear_label)
clear_button.pack(pady=5)

# เริ่มการทำงานของโปรแกรม
root.mainloop()