from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/Sam/Desktop/Final project/Testing/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Database creation
def create_database():
    conn = sqlite3.connect('testing.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()

def handle_successful_login(username):
    global active_user
    active_user = username

window = Tk()
window.geometry("1290x700")
window.configure(bg="#FFFFFF")

#Background
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1366.0,
    107.0,
    fill="#FFF6CB",
    outline="Pink",
    width=5
)
#Image_1
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    682.0,
    65.0,
    image=image_image_1
)

#Image_2
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    911.753662109375,
    61.71705144124826,
    image=image_image_2
)

#Image_3
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    442.9205176248902,
    58.176124572753906,
    image=image_image_3
)

#Image_4
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    980.0,
    412.0,
    image=image_image_4
)

#Image_5
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    343.0,
    412.0,
    image=image_image_5
)

#Register_Confirm_password
canvas.create_text(
    787.0,
    475.0,
    anchor="nw",
    text="Confirm Password",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 25 * -1)
)


#Register_Password
canvas.create_text(
    787.0,
    375.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 25 * -1)
)

#Register_Username
canvas.create_text(
    787.0,
    278.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 25 * -1)
)

#Login_Password
canvas.create_text(
    150.0,
    378.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 25 * -1)
)

#Login_username
canvas.create_text(
    150.0,
    278.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 25 * -1)
)


#Rectangle
canvas.create_rectangle(
    150.0,
    165.0,
    494.0,
    239.0,
    fill="#F6F6F6",
    outline=""
)

# Login Usernam
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    293.0,
    342.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F6F6F6",
    fg="#000716",
    highlightthickness=0
)

entry_1.place(
    x=160.0,
    y=320.0,
    width=266.0,
    height=42.0
)

#Login password
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    298.0,
    436.0,
    image=entry_image_2,
)
entry_2 = Entry(
    bd=0,
    bg="#F6F6F6",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=165.0,
    y=414.0,
    width=266.0,
    height=42.0
)


canvas.create_text(
    276.0,
    166.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 40 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    959.0,
    207.0,
    image=image_image_6
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    930.0,
    342.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F6F6F6",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=797.0,
    y=320.0,
    width=266.0,
    height=42.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    935.0,
    436.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F6F6F6",
    fg="#000716",
    highlightthickness=0,
    show='*'  # Mask the input
)
entry_4.place(
    x=802.0,
    y=414.0,
    width=266.0,
    height=42.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    935.0,
    536.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F6F6F6",
    fg="#000716",
    highlightthickness=0,
    show='*'  # Mask the input
)
entry_5.place(
    x=802.0,
    y=514.0,
    width=266.0,
    
    height=42.0
)

# Registration Function
def register():
    username = entry_3.get().strip()
    password = entry_4.get()
    confirm_password = entry_5.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    try:
        conn = sqlite3.connect('testing.db')  # Connect to 'testing.db'
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE LOWER(username) = ?', (username.lower(),))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Error", "Username already exists")
        else:   
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful")

            #Clear when sent to database successfully
            entry_3.delete(0, 'end')
            entry_4.delete(0, 'end')
            entry_5.delete(0, 'end')

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()


#Register button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="flat"
)
#Register button location
button_1.place(
    x=844.0,
    y=596.0,
    width=251.0,
    height=47.0
)


#Login function
def login():
    global active_user
    username = entry_1.get()  # Use entry_1 for login username
    password = entry_2.get()  # Use entry_2 for login password
    conn = sqlite3.connect('testing.db')   # Connect to 'testing.db'
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()


    if user:
        messagebox.showinfo("Success", "Login Successful")
        #Bring user into gui1.py
        window.destroy()
        import second
        second.main(passed_username=username)

    else:
        messagebox.showerror("Error", "Invalid username or password")

#Icon Login Func
# tion
        
def toggle_password_visibility(entry, button):
    if entry.cget('show') == '*':
        entry.config(show='')
        button.config(image=view_image)  # Show password, display "hide" image  
    else:
        entry.config(show='*')
        button.config(image=view_image)

# Load eye images
view_image = PhotoImage(file=relative_to_assets("image_3_icon.png"))


toggle_button_login = Button(
    window,
    image=view_image,
    borderwidth=2,
    highlightthickness=0,
    relief="solid",
    command=lambda: toggle_password_visibility(entry_2, toggle_button_login))
toggle_button_login.place(x=430, y=420, width=30, height=30,)
    
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png")) 
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat",
)

#Login button location
button_2.place(
    x=200.0,
    y=596.0,
    width=251.0,
    height=47.0,
)

canvas.create_text(
    256.0,
    215.0,
    anchor="nw",
    text="If you have an account",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 15 * -1)
)

canvas.create_text(
    893.0,
    220.0,
    anchor="nw",
    text="If you are new HERE!!",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 15 * -1)
)

canvas.create_text(
    886.0,
    170.0,
    anchor="nw",
    text="Register",
    fill="#000000",
    font=("SairaSemiCondensed Bold", 40 * -1)
)


window.resizable(False, False)
window.mainloop()


