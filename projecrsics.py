import tkinter as tk
from tkinter import messagebox

user_data = []

def login_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text=" Welcome back!\n Sign in to your account",fg="white",bg="DeepSkyBlue",font=("arial", 15, "bold"))
    label.pack(pady=20)
    email_label = tk.Label(root, text="Email:", fg="white",bg="DeepSkyBlue",font=("arial", 13,"bold"))
    email_label.pack(padx=10,pady=10)


    email_entry = tk.Entry(root,width=35)
    email_entry.pack()


    password_label = tk.Label(root, text="Password:", fg="white",bg="DeepSkyBlue", font=("arial",13,"bold"))
    password_label.pack(padx=10,pady=10)

    password_entry = tk.Entry(root, width=35,show="*")
    password_entry.pack()

    login_button = tk.Button(root, text="Login",font=("arial", 15, "bold"),fg="black",bg="MintCream",width=10,height=1, command=lambda: login(root, email_entry.get(), password_entry.get()))
    login_button.pack(padx=10,pady=10)

    register_button = tk.Button(root, text="Register",font=("arial", 13, "bold"),fg="black",bg="MintCream",width=10,height=1, command=lambda: register_page(root))
    register_button.pack(padx=10,pady=10)

def login(root, email, password):

    is_valid_user = validate_user(email, password)
    if is_valid_user:
        show_home_page_User(root, "User Page")

    elif email == "admin@gmail.com" and password == "admin123":
        show_home_page_Admin(root, "Admin Page")

    else:
        messagebox.showerror("Login Error", "Invalid email or password")

def validate_user(email, password):
    for existing_user in user_data:
        if existing_user.get("Email") == email and existing_user.get("Password") == password:
            return True

    return False




def show_home_page_Admin(root, page_title):
    register_label = tk.Label(root, text="Admin")
    register_label.pack(padx=5,pady=5)

    for widget in root.winfo_children():
        widget.destroy()
    root.title(page_title)
    add = tk.Button(root,text="Add product",width=15,height=2)
    add.pack(pady=15)
    dell = tk.Button(root, text="Update product",width=15,height=2)
    dell.pack(pady=15)








def show_home_page_User(root, page_title):
    for widget in root.winfo_children():
        widget.destroy()
    root.title(page_title)
    root.config(background="#00bfff")
    label = tk.Label(root, text="Categories", fg="white", bg="DeepSkyBlue", font=("arial", 20, "bold"))
    label.pack(pady=30)

    push1 = tk.Button(root, text="Home appliances", font=("arial", 13),width=15,height=2,command=lambda: home_app(root))
    push1.pack(padx=10,pady=10)

    push2 = tk.Button(root, text="Electronics", font=("arial", 13), width=15,height=2,command=lambda: electronics(root))
    push2.pack(padx=10, pady=10)

    push3 = tk.Button(root, text="Fashion", font=("arial", 13), width=15,height=2, command=lambda: fashion(root))
    push3.pack(padx=10, pady=10)

    push4 = tk.Button(root, text="Books", font=("arial", 13), width=15,height=2,command=lambda: books(root))
    push4.pack(padx=10, pady=10)

    push5 = tk.Button(root, text="Sports", font=("arial", 13), width=15,height=2,command=lambda: sports(root))
    push5.pack(padx=10, pady=10)


def sports(root):
    for widget in root.winfo_children():
        widget.destroy()

    lab = tk.Label(root, text="Sports", font=("arial", 20, "bold"), fg="white", bg="DeepSkyBlue")
    lab.pack(pady=15)
    lab2 = tk.Label(root, text="Search in Sports", font=("arial", 13, "bold"), fg="white", bg="DeepSkyBlue")
    lab2.pack()
    sear = tk.Entry(root)
    sear.pack(padx=10, pady=10)
    search = tk.Button(root, text="Search", font=("arial", 13, "bold"))
    search.pack()

    photo1 = tk.PhotoImage(file="ssw.png")
    res = photo1.subsample(2, 2)
    screen_btn = tk.Button(root, text="Football\n price = 100$", image=res, compound="top", width=200, height=220)
    screen_btn.place(x=5, y=100)
    screen_btn.pack()





    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray", command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)



def books(root):
    for widget in root.winfo_children():
        widget.destroy()

    lab = tk.Label(root, text="Books", font=("arial", 20, "bold"), fg="white", bg="DeepSkyBlue")
    lab.pack(pady=15)
    lab2 = tk.Label(root, text="Search in Books", font=("arial", 13, "bold"), fg="white", bg="DeepSkyBlue")
    lab2.pack()
    sear = tk.Entry(root)
    sear.pack(padx=10, pady=10)
    search = tk.Button(root, text="Search", font=("arial", 13, "bold"))
    search.pack()
    photo1 = tk.PhotoImage(file="rich dad poor dad.png")
    res = photo1.subsample(3, 3)
    screen_btn = tk.Button(root, text="rich dad poor dad\n price = 20$", image=res, compound="top", width=180, height=190)
    screen_btn.place(x=5, y=100)
    screen_btn.pack()







    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray", command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)







def fashion(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="beige")
    lab = tk.Label(root, text="Fashion", font=("arial", 20, "bold"), fg="white", bg="DeepSkyBlue")
    lab.pack(pady=15)
    lab2 = tk.Label(root, text="Search in Fashion", font=("arial", 13, "bold"), fg="white", bg="DeepSkyBlue")
    lab2.pack()
    sear = tk.Entry(root)
    sear.pack(padx=10, pady=10)
    search = tk.Button(root, text="Search", font=("arial", 13, "bold"))
    search.pack()

    screen_btn = tk.Label(root, text="Name:T-shirt\n Model year:2018\n brand: Zara\n price = 100$", fg="black",bg="white")
    screen_btn.pack()

    back_button1 = tk.Button(root, text="Add to cart ", bg="green", fg="white")
    back_button1.pack(padx=5, pady=5)

    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray",command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)












def home_app(root):
    for widget in root.winfo_children():
        widget.destroy()

    lab = tk.Label(root, text="Home appliances", font=("arial", 20, "bold"), fg="white", bg="DeepSkyBlue")
    lab.pack(pady=15)
    lab2 = tk.Label(root, text="Search in Home appliances", font=("arial", 13, "bold"), fg="white", bg="DeepSkyBlue")
    lab2.pack()
    sear = tk.Entry(root)
    sear.pack(padx=10, pady=10)
    search = tk.Button(root, text="Search", font=("arial", 13, "bold"))
    search.pack()

    screen_btn = tk.Label(root, text="Name:Arduino\n Model year:2021\n brand: Microchip\n price = 500$", fg="black",
                          bg="white")
    screen_btn.pack()

    back_button1 = tk.Button(root, text="Add to cart ", bg="green", fg="white")
    back_button1.pack(padx=5, pady=5)

    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray",command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)










def electronics(root):
    for widget in root.winfo_children():
        widget.destroy()
    lab = tk.Label(root, text="Electronics", font=("arial", 20,"bold"),fg="white", bg="DeepSkyBlue")
    lab.pack(pady=15)
    lab2 = tk.Label(root, text="Search in Electronics", font=("arial", 13,"bold"),fg="white", bg="DeepSkyBlue")
    lab2.pack()
    sear = tk.Entry(root)
    sear.pack(padx=10, pady=10)
    search = tk.Button(root, text="Search", font=("arial",13,"bold"))
    search.pack()

    screen_btn = tk.Label(root, text="Name:Dell screen\n Model year:2020\n brand: Dell\n price = 200$",fg="black",bg="white")
    screen_btn.pack()

    def search(root):

        form = [{"Name": "Dell screen", "Model year": 2020, "Brand": "Dell", "Price": 500},
                {"Name": "Laptop", "Model year": 2018, "Brand": "HP", "Price": 2200},
                {"Name": "Iphone 12", "Model year": 2020, "Brand": "Apple", "Price": 1000}]

        for item in form:

            if sear.get() == item["Name"]:
                screen_btn = tk.Label(root, text= item,
                                      fg="black", bg="white")
                screen_btn.pack()
















    back_button1 = tk.Button(root, text="Add to cart ", bg="green",fg="white")
    back_button1.pack(padx=5, pady=5)


    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray",command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)





def info1(root):
    for widget in root.winfo_children():
        widget.destroy()
    data = tk.Label(root,text="Name: Dell screen\n Model: 2020\n  ")




    push_product1 = tk.Button(root, text="Add to cart", font=("arial", 10, "bold"))
    push_product1.pack(pady=5)
    product1 = tk.Label(root, text="Arduino \n Price = 500$", font=("arial", 15, "bold"), fg="white", bg="DeepSkyBlue")
    product1.pack(pady=10)
    push_product2 = tk.Button(root, text="Add to cart", font=("arial", 10, "bold"))
    push_product2.pack(pady=5)

    back_button1 = tk.Button(root, text="Back to Categories ", bg="gray", command=lambda: show_home_page_User(root, "user page"))
    back_button1.pack(padx=5, pady=5)




def register_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    register_label = tk.Label(root, text="Register", font=("arial",19,"bold"),fg="white",bg="DeepSkyBlue")
    register_label.pack(padx=5,pady=5)

    name_label = tk.Label(root, text="Name:",font=("bold"),fg="white",bg="DeepSkyBlue")
    name_label.pack(padx=5,pady=5)

    name_entry = tk.Entry(root, width=35)
    name_entry.pack(padx=5,pady=5)
    for i in name_entry.get():
        if i =="":
            return False
        else:
            return True


    phone_label = tk.Label(root, text="Phone Number:",font=("bold"),fg="white",bg="DeepSkyBlue")
    phone_label.pack(padx=5,pady=5)

    phone_entry = tk.Entry(root,width=35)
    phone_entry.pack(padx=5,pady=5)

    email_label = tk.Label(root, text="Email:",font=("bold"),fg="white",bg="DeepSkyBlue")
    email_label.pack(padx=5,pady=5)

    email_entry = tk.Entry(root,width=35)
    email_entry.pack(padx=5,pady=5)

    gender_label = tk.Label(root, text="Gender:",fg="white",bg="DeepSkyBlue")
    gender_label.pack(padx=5,pady=5)
    Gender_Variable = tk.StringVar(root)
    Gender_Variable.set("Gender")
    Gender_Option = tk.OptionMenu(root,
                                  Gender_Variable,
                                  "Male", "Female")
    Gender_Option.pack()

    governorate_label = tk.Label(root, text="Governorate:",font=("bold"),fg="white",bg="DeepSkyBlue")
    governorate_label.pack(padx=5,pady=5)

    governorate_Variable = tk.StringVar(root)
    governorate_Variable.set("Governorate")
    governorate_Option = tk.OptionMenu(root,
                                  governorate_Variable,
                                  "Cairo", "Giza","Alexandria","Assiut","Aswan","Beheira","Bani Suef", "New Valley", "Damietta", "Fayyoum", "Matruh", "Red Sea","South Sinai",
                                       "North Sinai","Suez","Helwan","Sharqia","Dakahlia","Kafr el-Sheikh","Monufia","Minya","Gharbia","Qena","Sohag","Qalyubia","Luxor")

    governorate_Option.pack()
    password_label = tk.Label(root, text="Password:",font=("bold"),fg="white",bg="DeepSkyBlue")
    password_label.pack(padx=5,pady=5)


    password_entry = tk.Entry(root,width=35, show="*")
    password_entry.pack(padx=5,pady=5)

    age_label = tk.Label(root, text="Age:",font=("bold"),fg="white",bg="DeepSkyBlue")
    age_label.pack(padx=5,pady=5)

    Age_Variable = tk.StringVar(root)
    Age_Variable.set("Age")
    Age_Option = tk.OptionMenu(root, Age_Variable,
                               "below 14", "15",
                               "16", "17",
                               "above 18")
    Age_Option.pack()



    national_id_label = tk.Label(root, text="National ID:",font=("bold"),fg="white",bg="DeepSkyBlue")
    national_id_label.pack(padx=5,pady=5)

    national_id_entry = tk.Entry(root,width=35)
    national_id_entry.pack(padx=5,pady=5)


    register_button = tk.Button(root, text="Submit",fg="white",bg="green", command=lambda: save_user_data(root, name_entry.get(), phone_entry.get(),
                                                                                       email_entry.get(), Gender_Variable.get(),
                                                                                       governorate_Variable.get(), password_entry.get(),
                                                                                       Age_Variable.get(), national_id_entry.get()))
    register_button.pack(padx=5,pady=5)

    back_button = tk.Button(root, text="Back to login",bg="gray", command=lambda: login_page(root))
    back_button.pack(padx=5,pady=5)

def save_user_data(root,name, phone, email, gender, governorate, password, age, national_id):
    user_info = {
        "Name": name,
        "Phone Number": phone,
        "Email": email,
        "Gender": gender,
        "Governorate": governorate,
        "Password": password,
        "Age": age,
        "National ID": national_id
    }

    for existing_user in user_data:
        if existing_user.get("Email") == email:
            messagebox.showerror("Registration Error", "User with this email already exists!")
            return


    user_data.append(user_info)
    print("List of registered users:")
    for user in user_data:
        print(user)
    messagebox.showinfo("Registration Success", "User data has been registered successfully!")




root = tk.Tk()
root.geometry("500x600")
root.title("Online Shopping System")
root.config(background="DeepSkyBlue")
login_page(root)
root.mainloop()