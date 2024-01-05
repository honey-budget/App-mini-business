import tkinter as tk

def button_click():
    # เมื่อปุ่มถูกคลิกให้นับจำนวนครั้งขึ้น 1
    click_count_var.set(click_count_var.get() + 1)

    # แสดงจำนวนครั้งใน Label
    click_count_label.config(text=f'Click Count: {click_count_var.get()}')

# สร้างหน้าต่าง Tkinter
root = tk.Tk()
root.title('Button Click Counter')

# ตัวแปรเก็บจำนวนครั้ง
click_count_var = tk.IntVar()

# ปุ่มที่ใช้ในการกด
click_button = tk.Button(root, text='Click me!', command=button_click)
click_button.pack(pady=10)

# Label ที่แสดงจำนวนครั้ง
click_count_label = tk.Label(root, text='Click Count: 0')
click_count_label.pack(pady=10)

# แสดงหน้าต่าง Tkinter
root.mainloop()
