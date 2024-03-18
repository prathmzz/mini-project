#new line added
import tkinter as tk
from PIL import Image, ImageTk

def open_volunteering():
    # Function to open the volunteering section
    print("Opening Animal Volunteering Section")

def open_adoption():
    # Function to open the pet adoption section
    print("Opening Pet Adoption Section")

def open_donation():
    # Function to open the donation section
    print("Opening Donation Section")

def open_rescue():
    # Function to open the rescue section
    print("Opening Rescue Section")

# Create main window
root = tk.Tk()
root.title("Animal Welfare Homepage")

# Set background color
root.configure(bg='#E5E5E5')

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to be slightly less than full screen
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
root.geometry(f"{window_width}x{window_height}")

# Create a frame for the top section containing navigation bar, login, and signup buttons
top_frame = tk.Frame(root, bg='#4CAF50', width=window_width, height=100)
top_frame.pack(side=tk.TOP, fill=tk.X)

# Create navigation bar
navbar = tk.Frame(top_frame, bg='#4CAF50', height=50)
navbar.pack(side=tk.LEFT, padx=10, pady=5)

# Create project name label in navbar
project_label = tk.Label(navbar, text="Animal Connect", bg='#4CAF50', fg='white', font=('Helvetica', 14))
project_label.pack(side=tk.LEFT, padx=10, pady=5)

# Create buttons for each section in navbar
volunteering_button = tk.Button(navbar, text="Volunteer", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=open_volunteering)
adoption_button = tk.Button(navbar, text="Animal Adoption", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=open_adoption)
donation_button = tk.Button(navbar, text="Donation", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=open_donation)
rescue_button = tk.Button(navbar, text="Rescue", bg='#4CAF50', fg='white', font=('Helvetica', 12), command=open_rescue)

volunteering_button.pack(side=tk.LEFT, padx=10, pady=5)
adoption_button.pack(side=tk.LEFT, padx=10, pady=5)
donation_button.pack(side=tk.LEFT, padx=10, pady=5)
rescue_button.pack(side=tk.LEFT, padx=10, pady=5)

# Create login and signup buttons
login_button = tk.Button(top_frame, text="Login", bg='#4CAF50', fg='white', font=('Helvetica', 12))
signup_button = tk.Button(top_frame, text="Signup", bg='#4CAF50', fg='white', font=('Helvetica', 12))
signup_button.pack(side=tk.RIGHT, padx=10, pady=5)
login_button.pack(side=tk.RIGHT, padx=10, pady=5)

# Load background image
image = Image.open("img.jpg")
image = image.resize((window_width, window_height - 100))  # Subtracting the height of the top frame
background_image = ImageTk.PhotoImage(image)

# Create a label with background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=100, relwidth=1, relheight=1)  # Placing below the top frame

# Create label for welcome text with larger font size
welcome_label = tk.Label(root, text="Welcome to Animal Connect", font=("Helvetica", 36), bg="black", fg="white")
welcome_label.place(relx=0.05, rely=0.3, anchor=tk.W)  # Placing on the left side

# Create "Let's Get Started" button
get_started_button = tk.Button(root, text="Let's Get Started", bg='#4CAF50', fg='white', font=('Helvetica', 12))
get_started_button.place(relx=0.05, rely=0.4, anchor=tk.W)  # Placing below the welcome text

# Run the GUI
root.mainloop()
