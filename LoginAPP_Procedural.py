import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

pwd = ['admin']
user = ['admin']

root = customtkinter.CTk() #The app function
root.geometry('500x350') #Setting the geometry of the program, is in pixels.


frame = customtkinter.CTkFrame(master=root) #The main frame
frame.pack(pady=20, padx=60, fill = 'both', expand = 'true') #initialising the frame

label = customtkinter.CTkLabel(master=frame, text='Login', font=('inter', 25))



label.pack(pady= 20, padx=10)

def retrieve_input():
    UsernameInput = entr1.get()
    PasswordInput = entr2.get()

    if UsernameInput in user:
        block = 1
    if PasswordInput in pwd:
        block = block +1
    
    if block ==2:
        print("welcome to the system")
    

entr1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username') #username textbox
entr1.pack(pady = 12, padx = 10)

entr2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show = "•")
entr2.pack(pady = 12, padx = 10)


button = customtkinter.CTkButton(master=frame, text='Enter', command=retrieve_input )

button.pack(pady=20, padx=20)

root.mainloop()