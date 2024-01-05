import tkinter as tk

def generate_label():
    # ดึงข้อมูลจาก Entry widgets
    title = title_entry.get()
    weight = float(weight_entry.get())
    price = float(price_entry.get())

    # คำนวณผลคูณของ Weight และ Price
    total = weight * price

    # สร้าง Label
    label_text = f'Title: {title}, Weight: {weight}, Price: {price}, Total: {total}'
    result_label = tk.Label(root, text=label_text)
    result_label.pack()

# สร้างหน้าต่าง Tkinter
root = tk.Tk()
root.title("Label Generator")

# สร้าง Entry widgets สำหรับรับข้อมูล
title_label = tk.Label(root, text="Title:")
title_label.pack()
title_entry = tk.Entry(root)
title_entry.pack()

weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

price_label = tk.Label(root, text="Price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

# สร้าง Button สำหรับสร้าง Label
generate_button = tk.Button(root, text="Generate Label", command=generate_label)
generate_button.pack()

# รัน Tkinter event loop
root.mainloop()