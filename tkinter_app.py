from tkinter import *

def run_tkinter_app():
    from random import choice, shuffle, randint
    # import pyperclip

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    def generate_pass():
        pass_entry.delete(0, "end")
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols
        shuffle(password_list)

        password: str = "".join(password_list)
        pass_entry.insert(0, password)
        # pyperclip.copy(password)


    # ---------------------------- UI SETUP ------------------------------- #
    # Window
    window = Tk()
    window.title("Password Generator")
    window.config(padx=50, pady=50)

    # Canvas
    canvas = Canvas(width=200, height=200, background='white')
    myimg = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=myimg)
    canvas.grid(column=1, row=0)

    # Text
    pass_text = Label(text="Password:")
    pass_text.grid(column=0, row=3)

    # Entry
    pass_entry = Entry(width=40)
    pass_entry.insert(0, "Click the Generate Button")
    pass_entry.grid(column=1, row=3, columnspan=1, sticky="w")

    # Button
    generate_button = Button(text="Generate Password", width=15, highlightthickness=0, command=generate_pass)
    generate_button.grid(column=2, row=3, sticky="w")

    window.mainloop()


if __name__ == '__main__':
    run_tkinter_app()