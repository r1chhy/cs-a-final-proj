#PROBLEM with third page open
#Create History function



# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8s
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu,messagebox, StringVar, Frame
import sqlite3
import sys
import subprocess
import datetime

python_executable = sys.executable


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/Sam/Desktop/Final project/Testing/build/assets2/frame0")

#Connect to user
active_user = None
entry_1 = None
selected_breed = None
entry_3 = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_database():
    conn = sqlite3.connect("dogs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL, 
            dog_name TEXT,
            dog_breed TEXT,
            dog_color TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Added timestamp column
            FOREIGN KEY (username) REFERENCES users(username)  
        )
    ''')
    conn.commit() 

create_database()
def save_to_database():
    global active_user, entry_1, selected_breed, entry_3
    try:
        if not active_user:
            raise ValueError("No user defined")

        dog_name = entry_1.get("1.0", "end-1c").strip()
        dog_breed = selected_breed.get()
        dog_color = entry_3.get("1.0", "end-1c").strip()
        
        if not dog_name or dog_breed == 'Select Breed' or not dog_color:
            raise ValueError("Please fill in all fields")

        with sqlite3.connect("dogs.db") as conn:
            cursor = conn.cursor()

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
            cursor.execute('''
                INSERT INTO info (username, dog_name, dog_breed, dog_color, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (active_user, dog_name, dog_breed, dog_color, timestamp))
    

        entry_1.delete("1.0", "end-1c")
        selected_breed.set("Select Breed")  
        entry_3.delete("1.0", "end-1c")
        messagebox.showinfo("Success", f"Dog ({dog_name}) has been saved successfully for ({active_user})!")


        subprocess.Popen([python_executable, '/Users/Sam/Desktop/Final project/third.py', active_user])
        sys.exit()

    
    except ValueError as e:  # Catch validation errors
        messagebox.showerror("Error", str(e))
    except sqlite3.Error as e:  # Catch all SQLite errors
        messagebox.showerror("Error", f"Database error: {e}")

        
def logout():
    global active_user, window
    active_user = None  # Reset the active user

    # Destroy the current window to go back to the login page
    if window:
        window.destroy()

    # Assuming you have a separate login file, you'd call its main function here
    import main  # Import your login script 
    main.main()



def main(passed_username):
    global active_user, entry_1, selected_breed, entry_3, window
    active_user = passed_username



    window = Tk()
    window.geometry("1366x768")
    window.configure(bg = "#FFFFFF")

    

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        273.00000249315053,
        453.0,
        image=image_image_1
    )

    canvas.create_text(
        100.12636230466887,
        230.4276123046875,
        anchor="nw",
        text="Please fill in the information ",
        fill="#124C5F",
        font=("SairaSemiCondensed Bold", 30 * -1)
    )

    canvas.create_text(
        429.00000199206806,
        113.0,
        anchor="nw",
        text="Welcome to your most trusted Pet Shop services!\n                         Paw care loves your babies",
        fill="#3F6A78",
        font=("SansitaSwashedRoman Bold", 25 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        680,
        50.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        684.850576795172,
        62.2017822265625,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        446.09219901778897,
        54.51025390625,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        915.043806593118,
        59.8310546875,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        270,
        347,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#FFF7CE",
        fg="#000716",
        highlightthickness=0,
        font=("SairaSemiCondensed Bold", 18)
    )
    entry_1.place(
        x=130,
        y=325,
        width=272.2557990537025,
        height=45
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        264.3791161782574,
        448.1493154782802,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#FFF7CE",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=128.25121665140614,
        y=417.96533203125,
        width=272.2557990537025,
        height=58.36796689406037
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        263.9207421548199,
        552.6482168454677,
        image=entry_image_3
    )
    entry_3 = Text(
        bd=0,
        bg="#FFF7CE",
        fg="Black",
        highlightthickness=0,
        font=("SairaSemiCondensed Bold", 18)
    )
    entry_3.place(
        x=127.79284262796864,
        y=530.,
        width=272,
        height=47
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=183.7412109375,
        y=621.0,
        width=187.2570037841797,
        height=59.81967544555664
    )

    button_1.config(command=save_to_database) 
    
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
        118.9463885887526,
        291.5103759765625,
        anchor="nw",
        text="Dog’s name:",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    canvas.create_text(
        118.5076678856276,
        391.5093994140625,
        anchor="nw",
        text="Dog’s breed:",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    canvas.create_text(
        118.0514911278151,
        495.5084228515625,
        anchor="nw",
        text="Dog’s color:",
        fill="#000000",
        font=("SairaSemiCondensed Bold", 20 * -1)
    )

    canvas.create_text(
        590.0000513214618,
        651.0,
        anchor="nw",
        text="Find us at: @pawcarekh ",
        fill="#000000",
        font=("SansitaSwashedRoman Bold", 30 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place( 
        x=620.9999404565292,
        y=702.0,
        width=43.130003201851196,
        height=40.99999975786409
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=732.999978941275,
        y=702.0,
        width=45.12992645110626,
        height=40.999998602626874
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=826.9998804904499,
        y=698.0,
        width=50.18236772036198,
        height=47.000000160335276
    )

    canvas.create_rectangle(
        705.0,
        531.0,
        1247.0,
        633.0,
        fill="#FFF6CB",
        outline="")

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        710.9999326222814,
        583.0,
        image=image_image_6
    )

    canvas.create_text(
        782.0,
        569.0,
        anchor="nw",
        text="Safe, fun, and affordable daycare for your pets. \nRates start at $30 per day. Happy pets guaranteed!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_text(
        782.0,
        532.999999975947,
        anchor="nw",
        text="DayCare",
        fill="#000000",
        font=("SansitaSwashedRoman Regular", 25 * -1)
    )

    canvas.create_rectangle(
        705.0,
        244.0,
        1247.0,
        346.0,
        fill="#FFF6CB",
        outline="")

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        708.0000719928621,
        295.0,
        image=image_image_7
    )

    canvas.create_text(
        778.0,
        249.99999997647,
        anchor="nw",
        text="Training ",
        fill="#000000",
        font=("Share Regular", 25 * -1)
    )

    canvas.create_text(
        778.0,
        289.0,
        anchor="nw",
        text="Affordable, expert training with positive reinforcement. \nPackages start at $100. Ensure your dog's happiness!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_rectangle(
        705.0,
        388.0,
        1247.0,
        490.0,
        fill="#FFF6CB",
        outline="")

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        705.0000874680927,
        438.0,
        image=image_image_8
    )

    canvas.create_text(
        778.0,
        425.0,
        anchor="nw",
        text="Pet grooming that is both professional and affordable. \nStarting at $50 are the packages. \nBe certain that your pet feels and looks fantastic!",
        fill="#000000",
        font=("Sanchez Regular", 15 * -1)
    )

    canvas.create_text(
        778.0,
        391.9999999741169,
        anchor="nw",
        text="Pet Salon",
        fill="#000000",
        font=("SansitaSwashedRoman Regular", 25 * -1)
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        966.9999916362558,
        202.0,
        image=image_image_9
    )

    canvas.create_text(
        887.0,
        187.868408152666,
        anchor="nw",
        text="Our services",
        fill="#100C0C",
        font=("Sansita Swashed Bold", 25 * -1)
    )

    #Dog's Breeds
    dog_breeds = [
        "Labrador Retriever",
        "Golden Retriever",
        "German Shepherd",
        "French Bulldog",
        "Poodle",
        "Other"
    ]
    selected_breed = StringVar(value ="Select Breed")

    def on_breed_select(choice):
        selected_breed.set(choice) 

    breed_dropdown = OptionMenu(window, selected_breed, *dog_breeds, command=on_breed_select)
    breed_dropdown.config(
        bg="#FFF7CE",  # Match the entry background
        width=25,       # Adjust width as needed
        highlightthickness=0,
        fg="Black"
    )
    breed_dropdown["menu"].config(bg="#FFF7CE", fg='Black')  # Set dropdown background color
    breed_dropdown.place(x=128.251, y=417.965, height=58)  # Position below breed label




    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    create_database() 
    


