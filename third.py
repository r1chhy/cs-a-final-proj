# Dak CASH menu
# Dak function oy HISTORY
#Consider dak back menu or not


import sqlite3
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, StringVar, OptionMenu
import string
import sys
from pathlib import Path
from tkinter import Text, WORD, BOTH, END 
import datetime
import subprocess
import os
from second import main as second_main

# Paths setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/Sam/Desktop/Final project/Testing/build/assets3/frame0")

# Global variables
window = None
active_user = None 

def relative_to_assets(path: str) -> Path:
    
    return ASSETS_PATH / Path(path)


def view_history(username):
    history_window = Tk()
    history_window.title(f"Owner and Dog Data History for {username}")
    history_window.geometry("900x600")

    text_area = Text(history_window, wrap=WORD)
    text_area.pack(expand=True, fill=BOTH)

    try:
        # Owner Data
        conn_owner = sqlite3.connect('owner.db')
        cursor_owner = conn_owner.cursor()
        cursor_owner.execute("SELECT * FROM info WHERE username = ? ORDER BY timestamp DESC", (username,))
        owner_rows = cursor_owner.fetchall()

        # Dog Data
        conn_dog = sqlite3.connect("dogs.db")
        cursor_dog = conn_dog.cursor()

        # Check if the table exists
        cursor_dog.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='info'")
        table_exists = cursor_dog.fetchone() is not None

        if table_exists:
            cursor_dog.execute("SELECT * FROM info WHERE username = ? ORDER BY timestamp DESC", (username,))
            dog_rows = cursor_dog.fetchall()
        else:
            dog_rows = []

        if not owner_rows and not dog_rows:
            text_area.insert(END, "No history found for this user.")
        else:
            # Display Owner Data
            text_area.insert(END, "\n---- OWNER DATA ----\n\n")
            for row in owner_rows:
                text_area.insert(END, f"Timestamp: {row[6]}, ID: {row[0]}, Name: {row[2]}, Contact: {row[3]}, Service: {row[4]}, Payment: {row[5]}\n\n")

            # Display Dog Data (only if table exists and there's data)
            if dog_rows:
                text_area.insert(END, "\n---- DOG DATA ----\n\n")
                for row in dog_rows:
                    text_area.insert(END, f"Timestamp: {row[5]},Owner: {row[1]}, Dog ID: {row[0]}, Dog Name: {row[2]}, Breed: {row[3]}, Color: {row[4]}, \n\n") 

    except sqlite3.Error as e:
        text_area.insert(END, f"Error retrieving data: {e}")

    finally:
        if conn_owner:
            conn_owner.close()
        if conn_dog:
            conn_dog.close()

    history_window.mainloop()


# Function to create the database and table
def create_database():
    conn = sqlite3.connect('owner.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            service TEXT NOT NULL,
            payment TEXT NOT NULL,
            timestamp TEXT NOT NULL  
        )
    ''')
    conn.commit()
    conn.close()

    # Function to insert owner data into the info table
def insert_owner(username, name, contact, service, payment):
    conn = sqlite3.connect('owner.db')
    cursor = conn.cursor()

    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        INSERT INTO info (username, name, contact, service, payment, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, name, contact, service, payment, timestamp))

    conn.commit()
    conn.close()

# Validation and data submission function
def submit_button(entry_1, entry_4, service_var, payment_var, username):
    value = entry_1.get()
    value1 = entry_4.get()
    value2 = service_var.get()
    value3 = payment_var.get()

    is_name_valid = all(char in string.ascii_letters + string.whitespace for char in value)
    is_contact_valid = False
    contact_error_message = ""

    is_contact_valid = value1.isdigit()


    if value1.startswith('+855'):
        is_contact_valid = len(value1) == 13 and value1[3:].isdigit()  
        contact_error_message = "Contact must start with +855 and be 13 digits long (no spaces or symbols)."
    elif value1.startswith('0'):
        is_contact_valid = len(value1) == 10 and value1[1:].isdigit()
        contact_error_message = "Contact must start with 0 and be 10 digits long (no spaces or symbols)."
    else:
        is_contact_valid = False 
        contact_error_message = "Contact must start with +855 or 0 (no spaces or symbols)."



    #Error handling input
        
    error_messages = []

    if not is_name_valid:
        error_messages.append("Name must contain only letters and spaces.")
    if not is_contact_valid:
        error_messages.append(contact_error_message)
    if not value.strip() or not value1.strip() or not value2.strip() or not value3.strip():
        error_messages.append("Data fields cannot be empty.")

    if service_var.get() == "- Select -":  # Check if service is selected
        error_messages.append("Please select a service.")

    if error_messages:
        messagebox.showerror("Error", "\n".join(error_messages))
    else:
        insert_owner(username, value, value1, value2, value3)
        messagebox.showinfo("Success", "Data has been successfully inserted!")

        # Clear entry fields after successful submission
        entry_1.delete(0, 'end')  
        entry_4.delete(0, 'end')

previous_page_file = os.path.join(OUTPUT_PATH.parent, "build", "second.py")

python_executable = sys.executable  # This is usually the path to python.exe or python

# Logout function
def logout():
    global active_user, window
    active_user = None  # Reset the active user

    # Destroy the current window to go back to the login page
    if window:
        window.destroy()

    # Assuming you have a separate login file, you'd call its main function here
    import main  # Import your login script 
    main.main()



# Main function to set up the GUI
def main(username):
    global active_user, entry_1, entry_4, service_var, payment_var, window
    active_user = username

    window = Tk()  # Create the main window
    window.geometry("1290x730")
    window.configure(bg="#FFFFFF")

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
        outline=""
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        682.0,
        65.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        911.753662109375,
        61.71705144124826,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        442.92048710731206,
        58.1761474609375,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        316.0,
        366.0,
        image=image_image_4
    )

    # Name entry
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        166.5,
        295.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFF6CB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=46.5,
        y=271.0,
        width=240.0,
        height=47.0
    )

    # Payment entry
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        471.0,
        388.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFF6CB",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=358.0,
        y=364.0,
        width=240.0,
        height=47.0
    )

    # Service entry
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        471.0,
        295.5,
        image=entry_image_3
    )
    # Payment dropdown (OptionMenu)
    payment_options = ["Cash"]  # Only one option: Cash
    payment_var = StringVar(value=payment_options[0])  # Default to Cash

    longest_option_payment = max(payment_options, key=len)
    dropdown_width_payment = len(longest_option_payment) + 15

    option_menu_payment = OptionMenu(window, payment_var, *payment_options)
    option_menu_payment.place(x=360, y=375)
    option_menu_payment.config(width=dropdown_width_payment)


    


    # longest_option = max(service_options, key=len)
    #dropdown_width = len(longest_option) + 10
    
    
    # Service dropdown (OptionMenu) Entry_2
    service_options = ["- Select -", "Training", "Pet Salon", "Day Care"]  # Add "- Select -"
    service_var = StringVar(value=service_options[0])  # Default to "- Select -"

    longest_option = max(service_options, key=len)
    dropdown_width = len(longest_option) + 10

    option_menu = OptionMenu(window, service_var, *service_options)
    option_menu.config(width=dropdown_width)  # Adjust width as needed
    option_menu.place(x=360, y=285)  # Position the dropdown

    canvas.create_text(
        147.0,
        198.0,
        anchor="nw",
        text="Please fill in the information",
        fill="#3F6A78",
        font=("SairaSemiCondensed Bold", 30 * -1)
    )

    canvas.create_text(
        174.0,
        556.0,
        anchor="nw",
        text="View your History here",
        fill="#3F6A78",
        font=("SairaSemiCondensed Bold", 30 * -1)
    )

    canvas.create_text(
        37.0,
        238.0,
        anchor="nw",
        text=f"Your name: {username}",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    canvas.create_text(
        43.0,
        331.0,
        anchor="nw",
        text="Contact (Phone only):",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    canvas.create_text(
        348.0,
        238.0,
        anchor="nw",
        text="Service:",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    # Submit button
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit_button(entry_1, entry_4, service_var, payment_var, username),
        relief="flat"
    )
    button_1.place(
        x=224.0,
        y=443.0,
        width=183.0,
        height=52.0
    )
    

    button_image_logout = PhotoImage(
        file=relative_to_assets("button_logout.png"))
    button_logout = Button(
        image=button_image_logout,
        borderwidth=0,
        highlightthickness=0,
        command=logout,
        relief="flat"
    )
    button_logout.place(
        x=910.0,
        y=682.0,
        width=257.0,
        height=50.0
    )


    canvas.create_text(
        348.0,
        335.0,
        anchor="nw",
        text="Payment:",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    # Contact entry
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        167.0,
        391.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFF6CB",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=47.0,
        y=367.0,
        width=240.0,
        height=47.0
    )

    canvas.create_text(
        407.00000199206806,
        115.0,
        anchor="nw",
        text="Welcome to your most trusted Pet Shop services!\nPaw care loves your babies",
        fill="#3F6A78",
        font=("SansitaSwashedRoman Bold", 25 * -1)
    )

    canvas.create_rectangle(
        778.0,
        547.0,
        1320.0,
        649.0,
        fill="#FFF6CB",
        outline=""
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        783.9999326222814,
        599.0,
        image=image_image_5
    )

    canvas.create_text(
        855.0,
        585.0,
        anchor="nw",
        text="Safe, fun, and affordable daycare for your pets. \nRates start at $30 per day. Happy pets guaranteed!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_text(
        855.0,
        548.999999975947,
        anchor="nw",
        text="DayCare",
        fill="#000000",
        font=("SansitaSwashedRoman Regular", 25 * -1)
    )

    canvas.create_rectangle(
        778.0,
        260.0,
        1320.0,
        362.0,
        fill="#FFF6CB",
        outline=""
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        781.0000719928621,
        311.0,
        image=image_image_6
    )

    canvas.create_text(
        851.0,
        265.99999997647,
        anchor="nw",
        text="Training ",
        fill="#000000",
        font=("Share Regular", 25 * -1)
    )

    canvas.create_text(
        851.0,
        305.0,
        anchor="nw",
        text="Affordable, expert training with positive reinforcement. \nPackages start at $100. Ensure your dog's happiness!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_rectangle(
        778.0,
        404.0,
        1320.0,
        506.0,
        fill="#FFF6CB",
        outline=""
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        778.0000874680927,
        454.0,
        image=image_image_7
    )

    canvas.create_text(
        851.0,
        441.0,
        anchor="nw",
        text="Pet grooming that is both professional and affordable. \nStarting at $50 are the packages. \nBe certain that your pet feels and looks fantastic!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_text(
        851.0,
        407.9999999741169,
        anchor="nw",
        text="Pet Salon",
        fill="#000000",
        font=("SansitaSwashedRoman Regular", 25 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        1039.9999916362558,
        189.0,
        image=image_image_8
    )

    canvas.create_text(
        960.0,
        174.868408152666,
        anchor="nw",
        text="Our services",
        fill="#100C0C",
        font=("Sansita Swashed Bold", 25 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: view_history(username),
        relief="flat"
    )
    button_2.place(
        x=168.0,
        y=615.0,
        width=296.0,
        height=76.0
    )

    window.resizable(False, False)
    window.mainloop()

# Run the main function if the script is executed
if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Please enter your username: ")
    create_database()  # Create the database before running the main application
    main(username)
