from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import shutil
from pathfinder import *
from cipher import *
import os



class Homescreen:

    def __init__(self):
        root = Tk()
        root.title('File locker V 1.0')
        root.iconbitmap(str(icon_path) + '\\lock1.ico')

        # geometry fixing so the window would be on center
        scr_w = root.winfo_screenwidth()
        scr_h = root.winfo_screenheight()
        x_cord = (scr_w / 2) - (500 / 2)
        y_cord = (scr_h / 2) - (500 / 2)
        root.geometry('%dx%d+%d+%d' % (500, 500, x_cord, y_cord))


        # Homescreen background image
        canvas = Canvas(root,width=500,height=500)
        image = ImageTk.PhotoImage(Image.open(str(icon_path) + '\\Bg1.png'))
        canvas.create_image(0,0,anchor=NW,image=image)
        canvas.pack()


        # User can save uploded photos with this feature
        def copy_to_vault():
            selected_copy_path = filedialog.askopenfilenames(initialdir=main_path)
            for t in selected_copy_path:
                shutil.copy(str(t), files_path)


        # open function
        def Open_directory():
            selected_open_path = filedialog.askopenfilenames(initialdir=files_path)
            selected_open_path_string = "".join(selected_open_path)
            os.popen(selected_open_path_string)


        # Quiting application
        def Quit():
            Cipher.encryptfiles(os.listdir(str(files_path)), os.chdir(files_path))
            root.destroy()


        # Reseting username and password
        def register():
            for child in root.winfo_children():
                child.destroy()


            register_user_label = Label(root, text='Set Username')
            register_user_label.pack()
            reg_user_entry = Entry(root)
            reg_user_entry.pack()
            pass_reg_label = Label(root, text='Set Password')
            pass_reg_label.pack()
            pass_regis_ent = Entry(root)
            pass_regis_ent.pack()

            def create_username():
                if reg_user_entry.get() != "":
                    Cipher.decryptfile(path1)
                    file = open(path1, 'w')
                    file.truncate(0)
                    file.write(reg_user_entry.get())
                    file.close()
                    Cipher.encryptfile(path1)
                    create_password()
                else:
                    messagebox.showinfo('File locker V 1.0', 'Please set Your'+'\n'+'username and password to create an account')


            def create_password():
                if pass_regis_ent.get() != "":
                    Cipher.decryptfile(path2)
                    file = open(path2, 'w')
                    file.truncate(0)
                    file.write(pass_regis_ent.get())
                    file.close()
                    Cipher.encryptfile(path2)
                    root.destroy()
                    Homescreen()
                else:
                    messagebox.showinfo('File locker V 1.0', 'Please set Your'+'\n'+'username and password to create an account')

            register_buttun = ttk.Button(root, text='Reset', command=create_username)
            register_buttun.pack(pady=20)


        # Buttons
        s = ttk.Style()
        s.configure('W.TButton', font =('calibri', 10))


        open_button = ttk.Button(root, text='Open Vault', command=Open_directory, style='W.TButton')
        open_button.place(x=5, y=410)

        upload_files_button = ttk.Button(root, text='Copy To Vault', command=copy_to_vault, style='W.TButton')
        upload_files_button.place(x=5, y=440)

        quit_button = ttk.Button(root, text='Quit', command=Quit,  style='W.TButton')
        quit_button.place(x=5, y=470)

        reset_password = ttk.Button(root, text='Reset password', command=register, style='W.TButton')
        reset_password.place(x=398, y=470)

        root.resizable(width=False, height=False)
        root.protocol('WM_DELETE_WINDOW', Quit)
        root.mainloop()

if __name__ == '__main__':
    Homescreen()
