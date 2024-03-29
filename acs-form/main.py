'''
This is just a prototype. 
I see a lot of potential sa munting proyekto na ito.
Maybe one day makakagawa ako ng all-in-one desktop app para sa ACS. 
Members directory, event planner, note taking, etc.
'''
import tkinter as tk
from PIL import ImageTk, Image

# Styling Variables
titleColor = 'darkgreen'
backgroundColor = 'whitesmoke'
color = 'black'
activeBackgroundColor = 'darkgreen'
activeColor = 'whitesmoke'
paddingX = 20
paddingY = 10
prompt = ''

# Assets
img_logo = Image.open('img/acs-logo.png')
img_logo = img_logo.resize((150, 150), Image.LANCZOS)

# Functions
def prompt_success():
    lbl_prompt["text"] = 'Success!'

# Window
window = tk.Tk()
# window.attributes('-fullscreen', True) # Uncomment this line if you want fullscreen. Pangit nga lang HAHA

tkimg_logo = ImageTk.PhotoImage(img_logo)
window.iconphoto(True, tkimg_logo)
window.title('ACS Login')

# Widgets
frm_header = tk.Frame(bg=backgroundColor,
                      padx=paddingX,
                      pady=paddingY)

lbl_logo = tk.Label(master=frm_header,
                    bg=backgroundColor,
                    fg=titleColor,
                    pady=paddingY,
                    text='Logo Here', # Alt text
                    image=tkimg_logo)

lbl_title = tk.Label(master=frm_header,
                     bg=backgroundColor,
                     fg=titleColor,
                     font='que?', # What is this attribute for?
                     text='Association of Computer Scientists')

lbl_logo.pack(pady=paddingY)
lbl_title.pack(pady=paddingY)

frm_form = tk.Frame(bg=backgroundColor,
                    padx=paddingX,
                    pady=paddingY,
                    width=100)

lbl_email = tk.Label(master=frm_form,
                     bg=backgroundColor,
                     fg='black',
                     padx=paddingX/3,
                     text='Email Address:')

ent_email = tk.Entry(master=frm_form,
                     width=29, # fits 28 letters. my guess is that the remaining 1 text unit is allocated to padding/spaces around
                     borderwidth=2,
                     textvariable='Email Address') # Dunno yet kung para saan 'to

lbl_password = tk.Label(master=frm_form,
                        bg=backgroundColor,
                        fg='black',
                        padx=paddingX/3,
                        text='Password:')

ent_password = tk.Entry(master=frm_form,
                        width=29,
                        borderwidth=2,
                        show='*') 

btn_submit = tk.Button(master=frm_form,
                       bg=backgroundColor,
                       fg='black',
                       activebackground=activeBackgroundColor,
                       activeforeground=activeColor,
                       padx=paddingX/3,
                       pady=paddingY/3,
                       text='Submit',
                       command= prompt_success)

lbl_prompt = tk.Label(master=frm_form,
                      bg=backgroundColor,
                      fg=titleColor,
                      text='')
lbl_email.pack()
ent_email.pack()
lbl_password.pack()
ent_password.pack()
btn_submit.pack(pady=paddingY) # adds padding around the button
lbl_prompt.pack()

frm_footer = tk.Frame(bg=backgroundColor,
                      padx=paddingX,
                      pady=paddingY)

lbl_footnote = tk.Label(master=frm_footer,
                        bg=backgroundColor,
                        fg=color,
                        text='Created by Uzzi || 2023-2024')

lbl_footnote.pack()

frm_header.pack(fill='both',
                side='top',)
frm_form.pack(fill='both',
              side='top', 
              expand=True) # Accepts bool, or any data type that equates to True or False e.g. 1s vs 0s
frm_footer.pack(fill='both')

# Executes the window
window.mainloop()
print('The window was closed. Thank you.')