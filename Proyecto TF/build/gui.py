from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\docho\OneDrive\Escritorio\Proyecto TF\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("410x820")
window.configure(bg="#F2F1EC")

canvas = Canvas(
    window,
    bg="#F2F1EC",
    height=876,
    width=410,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    130.0,
    467.0,
    image=image_image_1
)

canvas.create_text(
    47.0,
    236.0,
    anchor="nw",
    text="Nombre usuario:",
    fill="#000000",
    font=("Barlow Medium", 16 * -1)
)

canvas.create_text(
    47.0,
    336.0,
    anchor="nw",
    text="Contraseña:",
    fill="#000000",
    font=("Barlow Medium", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    207.0,
    287.0,
    image=image_image_2
)

entry_1 = Entry(
    bd=0,
    bg="#C2C1C1",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=63.0,
    y=275.0,
    width=287.0,
    height=23.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    207.0,
    386.0,
    image=image_image_3
)

entry_2 = Entry(
    bd=0,
    bg="#C2C1C1",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=62.0,
    y=374.0,
    width=287.0,
    height=23.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    310.0,
    467.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    77.0,
    86.0,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ingresar_sistema(),
    relief="flat"
)
button_1.place(
    x=42.0,
    y=510.0,
    width=330.0,
    height=64.0
)

# Images for the toggle buttons
unchecked_image = PhotoImage(file=relative_to_assets("image_6.png"))
checked_image = PhotoImage(file=relative_to_assets("image_7.png"))

# Initial states
is_checked_1 = True
is_checked_2 = False

# Function to toggle the buttons
def toggle_1():
    global is_checked_1, is_checked_2
    if not is_checked_1:
        is_checked_1 = True
        is_checked_2 = False
        toggle_button_1.config(image=checked_image)
        toggle_button_2.config(image=unchecked_image)

def toggle_2():
    global is_checked_1, is_checked_2
    if not is_checked_2:
        is_checked_2 = True
        is_checked_1 = False
        toggle_button_2.config(image=checked_image)
        toggle_button_1.config(image=unchecked_image)

# Creating the first toggle button, checked by default
toggle_button_1 = Button(
    window,
    image=checked_image,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_1,
    relief="flat"
)
toggle_button_1.place(
    x=50.0,
    y=450.0,
    width=36.0,
    height=36.0
)

# Creating the second toggle button, unchecked by default
toggle_button_2 = Button(
    window,
    image=unchecked_image,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_2,
    relief="flat"
    )
toggle_button_2.place(
    x=218.0,
    y=450.0,
    width=36.0,
    height=36.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    80.0,
    787.0,
    image=image_image_8
)

# Function to show a message box
def show_message(message):
    messagebox.showinfo("Información", message)

# Function to handle login
def ingresar_sistema():
    username = entry_1.get()
    password = entry_2.get()

    # Verifying if username and password are empty
    if not username or not password:
        show_message("Debe llenar todas las casillas.")
        return

    # Verifying if the username exists in the dictionary
    if username in userpasswords:
        # Verifying if the password matches the username
        if userpasswords[username] == password:
            if is_checked_1 and username.startswith("E"):
                show_message("Alumno ingresó a sistema con éxito (:")
            elif is_checked_2 and username.startswith("A"):
                show_message("Bienvenido Bibliotecario!")
            else:
                show_message("Usuario no encontrado.")
        else:
            show_message("Su contraseña es incorrecta.")
    else:
        show_message("Usuario no encontrado.")

# Binding the button to the function
button_1.config(command=ingresar_sistema)

# Usernames and passwords dictionary
userpasswords = {"A00": "344", "E01": "abc"}  # "username": "password"

# Binding the text to the click event
create_account_text = canvas.create_text(
    230.0,
    780.0,
    anchor="nw",
    text="Crear cuenta nueva",
    fill="#000000",
    font=("Barlow Medium", 16 * -1)
)

# Binding the text to the click event
canvas.tag_bind(create_account_text, "<Button-1>", lambda e: show_message("Se creará una cuenta nueva"))

window.resizable(False, False)
window.mainloop()
