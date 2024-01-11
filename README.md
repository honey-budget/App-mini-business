# commit symbol
/s : สำเร็จ (sucess) <br>
/f : ไม่สำเร็จ (failure)<br>
/p[n] : ลำดับส่วนที่ n (ในกรณีนี้อ้างอิงจาก Roadmaps)<br>
# Roadmaps
- ~~สร้าง และ หาผลลัพธ์ได้~~
- สามารถดึงข้อมูลจากเว็บไซต์ที่ต้องการได้ 
- มีระบบบันทึก ราคาต่อน้ำหนัก
- ~~สามารถ แก้ไขข้อมูลที่ยืนยันไปแล้วได้ (แบบย้อนกลับ/หรือเลือกส่วนที่ต้องการได้)~~
- เก็บข้อมูล และ ปริ้นใบราคา
- สามารถเก็บข้อมูลแล้วในรูปแบบ .csv และอื่นๆ เพื่อนำไปใช้งานในทาง Data science
# Bug & Debug
- มีปัญหาการ Change/Remove/Add โดยต้องการให้แก้ไขได้เรื่อย ๆ ซึ่ง btn (Change/Remove) ยังคงต้องมีอยู่เสมอด้านหลังของ Result_Total  [$] บรรทัดที่ 75 - 77 // ไม่แน่นอน
``` 
                        '''
                           #! req : after click a save button then show change-btn & remove-btn  
                        '''
                        hidden_remove_btn = btn_remove_items.pack_forget() 
                        hidden_change_items_btn =btn_change_items_btn.pack_forget()
                        hidden_save_btn = btn_save_new_items.pack_forget()
```
ในส่วนดังกล่าวจะเป็นการทำต่อไป ให้กด btn-save แล้วยังคงมี btn-remove และ btn-change อยู่เสมอ <br>

# Hint
-> สำหรับ Edit(Change)/Remove/Add มีแนวทางการจัดการโดยสร้าง function แยกออกจัดการ เช่น

``` 
   def edit(parameters):
      ...
         ...
   .
   .
   .
   def add(parameters):
      ...
         ...

``` 
