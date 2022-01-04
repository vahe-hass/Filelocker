from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pathfinder import *
from cipher import *
from home import *
import os



class Login:

    def __init__(self):
        root = Tk()
        root.title('File locker V 1.0')
        root.iconbitmap(str(icon_path) + '\\lock1.ico')

        # geometry fixing so the window would be on center
        scr_w = root.winfo_screenwidth()
        scr_h = root.winfo_screenheight()
        x_cord = (scr_w / 2) - (300 / 2)
        y_cord = (scr_h / 2) - (150/ 2)
        root.geometry('%dx%d+%d+%d' % (300, 150, x_cord, y_cord))

        #labels
        username_label = Label(root, text='Username')
        username_label.place(x=10, y=10)
        password_label= Label(root, text='Password')
        password_label.place(x=10, y=35)
        # entaries
        username_entry = ttk.Entry(root, width=30)
        username_entry.place(x=80, y=10)

        password_entry = ttk.Entry(root, width=30, show="*")
        password_entry.place(x=80, y=35)

        # creating an account for the first time
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
                    file = open(path1, 'w')
                    file.write(reg_user_entry.get())
                    file.close()
                    Cipher.encryptfile(path1)
                    create_password()
                else:
                    messagebox.showinfo('File locker V 1.0', 'Please set Your username and password'+'\n'+ '           to create an account' )


            def create_password():
                if pass_regis_ent.get() != "":
                    file = open(path2, 'w')
                    file.write(pass_regis_ent.get())
                    file.close()
                    Cipher.encryptfile(path2)
                    root.destroy()
                    Homescreen()
                else:
                    messagebox.showinfo('File locker V 1.0', 'Please set Your username and password'+'\n'+ '           to create an account' )


            register_buttun = ttk.Button(root, text='Register', command=create_username)
            register_buttun.pack(pady=20)


        # Authenticating Username and password
        def Username_auth():
            try:
                os.chdir(data_path)
                Cipher.decryptfile(path1)
                file = open(path1, 'r')
                read = file.read()
                file.close()
                if username_entry.get() == read:
                    Cipher.encryptfile(path1)
                    Password_auth()
                else:
                    Cipher.encryptfile(path1)
                    invalid_userlabel = Label(root, text='Invalid Username and password').place(x=60, y=70)
            except FileNotFoundError:
                try:
                    Cipher.encryptfile(path1)
                except FileNotFoundError:
                    pass
                messagebox.showinfo('File locker V 1.0', 'Please create an account to proceed' )

        def Password_auth():
            Cipher.decryptfile(path2)
            file = open(path2, 'r')
            read = file.read()
            file.close()
            if password_entry.get() == read:
                root.destroy()
                Cipher.encryptfile(path2)
                Cipher.decryptfiles(os.listdir(str(files_path)), os.chdir(files_path))
                Homescreen()

            else:
                Cipher.encryptfile(path2)
                invalid_passlabel = Label(root, text='Invalid Username and password').place(x=60, y=70)


        # buttons
        s = ttk.Style()
        s.configure('Kim.TButton', font=('Helvetica', 12))
        create_account_button = ttk.Button(root, text='Create Account', command=register, style='Kim.TButton')
        get_dir = os.listdir(data_path)
        if len(get_dir) < 2:
            self_destruct_list = os.listdir(files_path)
            dir_ch = os.chdir(files_path)
            for i in self_destruct_list:
                os.remove(i)
            create_account_button.pack(fill=X, side=BOTTOM)


        login_button = ttk.Button(root, text='Login!', command=Username_auth, style='Kim.TButton')
        login_button.pack(fill=X, side=BOTTOM)




        root.resizable(width=False, height=False)
        root.mainloop()

if __name__ == '__main__':
    Login()
