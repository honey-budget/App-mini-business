from tkinter import Tk, Label, StringVar, Frame, Button, scrolledtext

def add_items(NAME, WEIGHT, PRICE_PER_WEIGHT):
    RESULT = WEIGHT * PRICE_PER_WEIGHT
    
    add_items = Tk()
    add_items.geometry("800x400")
    add_items.title("Scrollable Items")

    frame = Frame(add_items, bd=2, relief="groove")
    frame.place(x=10, y=10, width=780, height=380)

    Label(frame, text=f'{NAME}', font='Helvetica 18 bold').place(x=10, y=10)
    
    Label(frame, text="Weight: ").place(x=10, y=50)
    Label(frame, text=f'{WEIGHT} kg').place(x=70, y=50)

    Label(frame, text="Price per kg: ").place(x=10, y=80)
    Label(frame, text=f'{PRICE_PER_WEIGHT} Baht').place(x=120, y=80)

    Label(frame, text="Total Price: ").place(x=10, y=110)
    Label(frame, text=f'{RESULT} Baht').place(x=120, y=110)

    # ScrolledText for scrolling
    scrolled_text = scrolledtext.ScrolledText(frame, wrap="word", width=30, height=8)
    scrolled_text.place(x=300, y=10)

    # Button for scrolling
    scroll_button = Button(frame, text="Scroll Down", command=lambda: scrolled_text.yview_scroll(1, "units"))
    scroll_button.place(x=400, y=300)

    add_items.mainloop()

# Example usage:
add_items("Product Name", 10, 5)
