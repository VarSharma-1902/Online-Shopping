from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox

import back_end

#root window 
mainWindow = Tk() 
mainWindow.title("")
#mainWindow.iconbitmap("G:/My Drive/Market Billing System/Misc/Icon Image.ico")
mainWindow.geometry("1000x600")

heading = Label(mainWindow, text = "Online Shopping", font=("Arial", 40))
heading.place(x = 350, y = 10)
new_window = name_entry = dob_entry = gVar = address_entry = pin_entry = ph_entry = rEmail_entry = rPwd_entry = rConfirmPwd_entry = ''
def reg_window():
    global new_window, name_entry,dob_entry, gVar, address_entry, pin_entry, ph_entry, rEmail_entry, rPwd_entry, rConfirmPwd_entry

    new_window = Toplevel() 
    new_window.geometry("1000x600") 
    new_window.title("")
    #new_window.iconbitmap("G:/My Drive/Market Billing System/Misc/Icon Image.ico")
    #name
    name_label = Label(new_window, text = "Name : ") 
    name_label.grid(row = 1, column = 1)
    name_entry = Entry(new_window, borderwidth=5) 
    name_entry.grid(row = 1, column = 2)
    #date of birth
    dob_label = Label(new_window, text = "Date of Birth : ") 
    dob_label.grid(row = 2, column = 1)
    dob_entry = Entry(new_window, borderwidth=5) 
    dob_entry.grid(row = 2, column = 2)
    #gender
    gender_label = Label(new_window, text="Gender:") 
    gender_label.grid(row = 3, column = 1)
    gVar = StringVar() 
    gVar.set("Male")
    gender_radio_male = Radiobutton(new_window, text = "Male", value="Male")
    gender_radio_male.grid(row = 3, column = 2)
    
    gender_radio_female = Radiobutton(new_window, text = "Female", value="Female")
    gender_radio_female.grid(row = 3, column = 3)
    gender_radio_others = Radiobutton(new_window, text = "Others", value="Others")
    gender_radio_others.grid(row = 3, column = 4) 
    #address
    address_label = Label(new_window, text = "Address : ") 
    address_label.grid(row = 4, column = 1)
    address_entry = Entry(new_window, borderwidth=5, width = 100) 
    address_entry.grid(row  =  4,  column  =  2,  columnspan=3)
    #pincode
    pin_label = Label(new_window, text = "Pin Code : ") 
    pin_label.grid(row = 5, column = 1)
    pin_entry = Entry(new_window, borderwidth=5) 
    pin_entry.grid(row = 5, column = 2)
    #phone number
    ph_label = Label(new_window, text = "Phone Number : ") 
    ph_label.grid(row = 6, column = 1)
    ph_entry = Entry(new_window, borderwidth=5) 
    ph_entry.grid(row = 6, column = 2)
    #email id
    rEmail_label = Label(new_window, text = "Email Id : ") 
    rEmail_label.grid(row = 7, column = 1)
    rEmail_entry = Entry(new_window, borderwidth=5) 
    rEmail_entry.grid(row = 7, column = 2)
    #new password
    rPwd_label = Label(new_window, text = "New Password : ") 
    rPwd_label.grid(row = 8, column = 1)
    rPwd_entry = Entry(new_window, borderwidth=5) 
    rPwd_entry.grid(row  =  8,   column   =   2) 
    #confirm password
    rConfirmPwd_label = Label(new_window, text = "Confirm Password : ") 
    rConfirmPwd_label.grid(row = 9, column = 1)
    rConfirmPwd_entry = Entry(new_window, borderwidth=5) 
    rConfirmPwd_entry.grid(row = 9, column = 2)

    #submit
    def popup():
        if(rPwd_entry.get() == rConfirmPwd_entry.get()):
            response = messagebox.askyesnocancel("Submit", "Are you sure to submit?")
            if response == 1: 
                cust_db()
        else:
            messagebox.showwarning("","Password and Confirm Password don't match!")
 
    enter_details = Button(new_window, text = "Submit", command=popup) 
    enter_details.grid(row = 10, column=2)
 
#add customer details to the database 
def cust_db():
    back_end.sql_cust_db(name_entry.get(), dob_entry.get(), gVar.get(), address_entry.get(), pin_entry.get(), ph_entry.get(), rEmail_entry.get(), rPwd_entry.get())
    new_window.destroy()

#check whether the customer exists or not 
def check_record_exist():
    result = back_end.sql_check_record_exist(email_entry.get(), pswd_entry.get())
    for i in result: 
        if i[0] == 1:
            shopping() 
        else:
            messagebox.showinfo("Caution", "Invalid Email ID or Password")

#add data to text file
bill = open("bill_file.txt", "a+") 
def create_bill(item, qty, price):
    bill = open("bill_file.txt", "a+")
    bill.write(str(item) + " "+ str(qty) + "kg Rs." + str(price) + "\n")

total = 0

def total_cost(num): 
    global  total 
    total += num


#shopping widget 
def shopping():
    global shop_window 
    shop_window = Toplevel()
    shop_window.geometry("1000x600")
    #shop_window.iconbitmap("G:/My Drive/Market Billing System/Misc/Icon Image.ico")
    total_label = Label(shop_window, text = "Total Amount = Rs.0") 
    total_label.grid(row=7, column=5)

#categories button 
#vegetables section
    veg_button = Label(shop_window, text = "Vegetables") 
    veg_button.grid(row = 1, column = 0, padx=90, pady=20) 
    #display list of veggies 
    veggies = back_end.extract_vegetables() 
    clicked_veg = StringVar()
    clicked_veg.set(veggies[0][1]) 
    veg_options = []     
    for i in range(12): 
        veg_options.append(veggies[i][1])
    veg_drop = OptionMenu(shop_window, clicked_veg, *veg_options) 
    veg_drop.grid(row = 1, column = 1, padx=90, pady=20)
    #select quantity
    veg_qty_txt = Entry(shop_window, width = 10) 
    veg_qty_txt.insert(0, 0)
    veg_qty_txt.grid(row = 1, column = 3, pady=20) 
    def inc_value_veg():
        qty = veg_qty_txt.get() 
        if(int(qty)<400):
            veg_qty_txt.delete(0,END) 
            veg_qty_txt.insert(0, int(qty)+1)
        else:
            veg_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            veg_add.grid(row = 1, column = 4, pady=20)

    def dec_value_veg():
        qty = veg_qty_txt.get() 
        if(int(qty)>0):
            veg_qty_txt.delete(0,END) 
            veg_qty_txt.insert(0, int(qty)-1)
        else:
            veg_sub = Button(shop_window, text = "-", width = 3, state= DISABLED)
            veg_sub.grid(row = 1, column = 2, pady=20)

    veg_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_veg(), calc_cost_veg()])
    veg_add.grid(row = 1, column  =  4,  pady=20) 
    veg_sub = Button(shop_window, text = "-", width=3,
    command=lambda:[dec_value_veg(), calc_cost_veg()]) 
    veg_sub.grid(row = 1, column = 2, pady=20)

    #cost calculation and display 
    cost_of_veggies_list = [] 
    for i in range(12):
        cost_of_veggies_list.append([veggies[i][1], veggies[i][2]]) 
    veg_cost = Label(shop_window, text = "0")
    veg_cost.grid(row=1, column=5, padx = 50, pady = 20) 
    v = []
    def calc_cost_veg(): 
        global veg_cost 
        cost_of_veg = 0
        veg_type = clicked_veg.get() 
        veg_qty = int(veg_qty_txt.get()) 
        for i in range(12):
            if (veg_type == veggies[i][1]): 
                cost_of_veg = veg_qty * veggies[i][2] 
                v.append(cost_of_veg)
                break
        veg_cost = Label(shop_window, text = "Rs."+str(cost_of_veg)) 
        veg_cost.grid(row=1, column=5, padx = 50, pady = 20)


    add_veg = Button(shop_window, text = "Add Item", command=lambda:[create_bill(clicked_veg.get(), veg_qty_txt.get(), v[-1]), total_cost(v[-1]), update_total()])
    add_veg.grid(row = 1, column=6)

    def update_total():
        total_label = Label(shop_window, text = "Total Amount = Rs."+str(total))
        total_label.grid(row=7, column=5)

#fruits section
    fruit_button = Label(shop_window, text = "Fruits") 
    fruit_button.grid(row = 2, column = 0, padx=90, pady=20) 
    #display list of fruits
    fruits = back_end.extract_fruits() 
    clicked_fruit = StringVar() 
    clicked_fruit.set(fruits[0][1]) 
    fruit_options = []
    for i in range(7): 
        fruit_options.append(fruits[i][1])
    fruit_drop = OptionMenu(shop_window, clicked_fruit, *fruit_options) 
    fruit_drop.grid(row = 2, column = 1, padx=90, pady=20)
    #select quantity
    fruit_qty_txt = Entry(shop_window, width = 10) 
    fruit_qty_txt.insert(0, 0) 
    fruit_qty_txt.grid(row = 2, column = 3, pady=20) 
    def inc_value_fruit():
        qty = fruit_qty_txt.get() 
        if(int(qty)<200):
            fruit_qty_txt.delete(0,END) 
            fruit_qty_txt.insert(0, int(qty)+1)
        else:
            fruit_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            fruit_add.grid(row = 2, column = 4, pady=20)

    def dec_value_fruit():
        qty = fruit_qty_txt.get()
    
        if(int(qty)>0): 
            fruit_qty_txt.delete(0,END) 
            fruit_qty_txt.insert(0, int(qty)-1)
        else:
            fruit_sub = Button(shop_window, text = "-", width = 3, state=DISABLED)
            fruit_sub.grid(row = 2, column = 2, pady=20)

    fruit_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_fruit(), calc_cost_fruit()])
    fruit_add.grid(row = 2,  column  =  4,  pady=20) 
    fruit_sub = Button(shop_window, text = "-", width=3,
    command=lambda:[dec_value_fruit(), calc_cost_fruit()]) 
    fruit_sub.grid(row = 2, column = 2, pady=20)

    #cost calculation and display 
    cost_fruit_list = []
    for i in range(7): 
        cost_fruit_list.append([fruits[i][1], fruits[i][2]])
    f = []
    def calc_cost_fruit(): 
        global fruit_cost
        fruit_type = clicked_fruit.get() 
        fruit_qty = int(fruit_qty_txt.get()) 
        for i in range(12):
            if (fruit_type ==  fruits[i][1]): 
                cost_of_fruit = fruit_qty * fruits[i][2] 
                f.append(cost_of_fruit)
                break
        fruit_cost = Label(shop_window, text = "Rs."+str(cost_of_fruit)) 
        fruit_cost.grid(row=2, column=5, padx = 50, pady = 20)
    fruit_cost = Label(shop_window, text = "0") 
    fruit_cost.grid(row=2, column=5, padx = 50, pady = 20) 
    add_fruit = Button(shop_window, text = "Add Item",
    command=lambda:[create_bill(clicked_fruit.get(), fruit_qty_txt.get(), f[- 1]), total_cost(f[-1]), update_total()])
    add_fruit.grid(row = 2, column=6) 
    #total_cost(f[-1])

#bodycare products section
    bodyCare_button = Label(shop_window, text = "Body Care") 
    bodyCare_button.grid(row = 3, column = 0, padx=90, pady=20) 
    #display list of bodycare products
    bodycare = back_end.extract_bodycare() 
    clicked_bodycare = StringVar() 
    clicked_bodycare.set(bodycare[0][1]) 
    bodycare_options = []
    for i in range(8):
        bodycare_options.append(bodycare[i][1])
    bodycare_drop = OptionMenu(shop_window, clicked_bodycare,
    *bodycare_options)
    bodycare_drop.grid(row = 3, column = 1, padx=90, pady=20) #select quantity
    bodycare_qty_txt = Entry(shop_window, width = 10) 
    bodycare_qty_txt.insert(0, 0) 
    bodycare_qty_txt.grid(row = 3, column = 3, pady=20) 
    def inc_value_bodycare():
        qty = bodycare_qty_txt.get() 
        if(int(qty)<150):
            bodycare_qty_txt.delete(0,END) 
            bodycare_qty_txt.insert(0, int(qty)+1)
        else:
            bodycare_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            bodycare_add.grid(row  =  3,  column  =  4,  pady=20)

    def dec_value_bodycare():
        qty = bodycare_qty_txt.get() 
        if(int(qty)>0):
            bodycare_qty_txt.delete(0,END) 
            bodycare_qty_txt.insert(0, int(qty)-1)
        else:
            bodycare_sub = Button(shop_window, text = "-", width = 3, state=DISABLED)
            bodycare_sub.grid(row = 3, column = 2, pady=20)

    bodycare_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_bodycare(), calc_cost_bodycare()])
    bodycare_add.grid(row = 3, column = 4, pady=20) 
    bodycare_sub = Button(shop_window, text = "-", width=3,
    command=lambda:[dec_value_bodycare(), calc_cost_bodycare()]) 
    bodycare_sub.grid(row = 3, column = 2, pady=20)

    #cost calculation and display 
    cost_of_bodycare_list = [] 
    for i in range(8):
        cost_of_bodycare_list.append([bodycare[i][1], bodycare[i][2]])

    b = []
    def calc_cost_bodycare():
        bodycare_type = clicked_bodycare.get() 
        bodycare_qty = int(bodycare_qty_txt.get()) 
        for i in range(8):
            if (bodycare_type == bodycare[i][1]): 
                cost_of_bodycare = bodycare_qty * bodycare[i][2] 
                b.append(cost_of_bodycare)
            break
        bodycare_cost = Label(shop_window, text = "Rs."+str(cost_of_bodycare))
        bodycare_cost.grid(row=3, column=5, padx = 50, pady = 20)

    bodycare_cost = Label(shop_window, text = "0") 
    bodycare_cost.grid(row=3, column=5, padx = 50, pady = 20)

    add_bodycare = Button(shop_window, text = "Add Item", command=lambda:[create_bill(clicked_bodycare.get(), bodycare_qty_txt.get(), b[-1]), total_cost(b[-1]), update_total()])
    add_bodycare.grid(row = 3, column=6)

#hair care products section
    hairCare_button = Label(shop_window, text = "Hair Care") 
    hairCare_button.grid(row = 4, column = 0, padx=90, pady=20) 
    #display list of haircare products
    haircare = back_end.extract_haircare() 
    clicked_haircare = StringVar() 
    clicked_haircare.set(haircare[0][1]) 
    haircare_options = []
    for i in range(6): 
        haircare_options.append(haircare[i][1])
    haircare_drop = OptionMenu(shop_window, clicked_haircare,*haircare_options)
    haircare_drop.grid(row = 4, column = 1, padx=90, pady=20) 
    #select quantity
    haircare_qty_txt = Entry(shop_window, width = 10) 
    haircare_qty_txt.insert(0,0) 
    haircare_qty_txt.grid(row = 4, column = 3, pady=20) 
    def inc_value_haircare():
        qty = haircare_qty_txt.get() 
        if(int(qty)<100):
            haircare_qty_txt.delete(0,END) 
            haircare_qty_txt.insert(0, int(qty)+1)
        else:
            haircare_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            haircare_add.grid(row = 4, column = 4, pady=20)

    def dec_value_haircare():
        qty = haircare_qty_txt.get() 
        if(int(qty)>0):
            haircare_qty_txt.delete(0,END) 
            haircare_qty_txt.insert(0, int(qty)-1)
        else:
            haircare_sub = Button(shop_window, text = "-", width = 3, state=DISABLED)
            haircare_sub.grid(row = 4, column = 2, pady=20)

    haircare_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_haircare(), calc_cost_haircare()])
    haircare_add.grid(row = 4, column = 4, pady=20) 
    haircare_sub = Button(shop_window, text = "-", width=3,
    command=lambda:[dec_value_haircare(), calc_cost_haircare()]) 
    haircare_sub.grid(row = 4, column = 2, pady=20)

    #cost calculation and display 
    cost_of_haircare_list = [] 
    for i in range(6):
        cost_of_haircare_list.append([haircare[i][1], haircare[i][2]])

    h = []
    def calc_cost_haircare():
        haircare_type = clicked_haircare.get() 
        haircare_qty = int(haircare_qty_txt.get()) 
        for i in range(6):
            if (haircare_type == haircare[i][1]): 
                cost_of_haircare = haircare_qty * haircare[i][2] 
                h.append(cost_of_haircare)
                break
        haircare_cost = Label(shop_window, text = "Rs."+str(cost_of_haircare))
        haircare_cost.grid(row=4, column=5, padx = 50, pady = 20)

    haircare_cost = Label(shop_window, text = "0") 
    haircare_cost.grid(row=4, column=5, padx = 50, pady = 20)

    add_haircare = Button(shop_window, text = "Add Item", command=lambda:[create_bill(clicked_haircare.get(), haircare_qty_txt.get(), h[-1]), total_cost(h[-1]), update_total()])
    add_haircare.grid(row = 4, column=6)

#snacks section
    snacksFood_button = Label(shop_window, text = "Snacks and Food") 
    snacksFood_button.grid(row = 5, column = 0, padx=90, pady=20) 
    #display list of snacks products
    snack = back_end.extract_snacks() 
    clicked_snack = StringVar() 
    clicked_snack.set(snack[0][1]) 
    snack_options = []
    for i in range(7): 
        snack_options.append(snack[i][1])
        snack_drop = OptionMenu(shop_window, clicked_snack, *snack_options) 
        snack_drop.grid(row = 5, column = 1, padx=90, pady=20)
    #select quantity
    snack_qty_txt = Entry(shop_window, width = 10) 
    snack_qty_txt.insert(0,0) 
    snack_qty_txt.grid(row = 5, column = 3, pady=20) 
    def inc_value_snack():
        qty = snack_qty_txt.get() 
        if(int(qty)<150):
            snack_qty_txt.delete(0,END) 
            snack_qty_txt.insert(0, int(qty)+1)
        else:
            snack_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            snack_add.grid(row = 5, column = 4, pady=20)

    def dec_value_snack():
        qty = snack_qty_txt.get() 
        if(int(qty)>0):
            snack_qty_txt.delete(0,END) 
            snack_qty_txt.insert(0, int(qty)-1)
        else:
            snack_sub = Button(shop_window, text = "-", width = 3, state=DISABLED)
        snack_sub.grid(row = 5, column = 2, pady=20)

    snack_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_snack(), calc_cost_snack()])
    snack_add.grid(row = 5, column = 4, pady=20) 
    snack_sub = Button(shop_window, text = "-", width=3,
    command=lambda:[dec_value_snack(), calc_cost_snack()]) 
    snack_sub.grid(row = 5, column = 2, pady=20)

    #cost calculation and display 
    cost_of_snack_list = []
    for i in range(7): 
        cost_of_snack_list.append([snack[i][1], snack[i][2]])

    s = []
    def calc_cost_snack():
        snack_type = clicked_snack.get() 
        snack_qty = int(snack_qty_txt.get()) 
        for i in range(7):
            if (snack_type == snack[i][1]): 
                cost_of_snack = snack_qty * snack[i][2] 
                s.append(cost_of_snack)
                break
        snack_cost = Label(shop_window, text = "Rs."+str(cost_of_snack)) 
        snack_cost.grid(row=5, column=5, padx = 50, pady = 20)

    snack_cost = Label(shop_window, text = "0")
    
    snack_cost.grid(row=5, column=5, padx = 50, pady = 20)

    add_snack = Button(shop_window, text = "Add Item", command=lambda:[create_bill(clicked_snack.get(), snack_qty_txt.get(), s[- 1]), total_cost(s[-1]), update_total()])
    add_snack.grid(row = 5, column=6)


#stationery products section
    stat_button = Label(shop_window, text = "Stationery") 
    stat_button.grid(row = 6, column = 0, padx=90, pady=20) 
    #display list of stationery products
    stat = back_end.extract_stationery() 
    clicked_stat = StringVar() 
    clicked_stat.set(stat[0][1]) 
    stat_options = []
    for i in range(15): 
        stat_options.append(stat[i][1])
    stat_drop = OptionMenu(shop_window, clicked_stat, *stat_options) 
    stat_drop.grid(row = 6, column = 1, padx=90, pady=20)
    #select quantity
    stat_qty_txt = Entry(shop_window, width = 10) 
    stat_qty_txt.insert(0,0) 
    stat_qty_txt.grid(row = 6, column = 3, pady=20) 
    def inc_value_stat():
        qty = stat_qty_txt.get() 
        if(int(qty)<500):
            stat_qty_txt.delete(0,END) 
            stat_qty_txt.insert(0, int(qty)+1)
        else:
            stat_add = Button(shop_window, text = "+", width = 3, state=DISABLED)
            stat_add.grid(row = 6, column = 4, pady=20)

    def dec_value_stat():
        qty = stat_qty_txt.get() 
        if(int(qty)>0):
            stat_qty_txt.delete(0,END) 
            stat_qty_txt.insert(0, int(qty)-1)
        else:
            stat_sub = Button(shop_window, text = "-", width = 3, state=DISABLED)
            stat_sub.grid(row  =  6,  column  =  2,  pady=20)

    stat_add = Button(shop_window, text = "+", width = 3, command=lambda:[inc_value_stat(), calc_cost_stat()])
    stat_add.grid(row = 6, column  =  4,  pady=20) 
    stat_sub = Button(shop_window, text = "-", width=3,
    
    command=lambda:[dec_value_stat(), calc_cost_stat()]) 
    stat_sub.grid(row = 6, column = 2, pady=20)

    #cost calculation and display 
    cost_of_stat_list = []
    for i in range(15): 
        cost_of_stat_list.append([stat[i][1], stat[i][2]])

    stationery = []
    def calc_cost_stat():
        stat_type = clicked_stat.get() 
        stat_qty = int(stat_qty_txt.get()) 
        for i in range(15):
            if (stat_type == stat[i][1]): cost_of_stat = stat_qty * stat[i][2]
            stationery.append(cost_of_stat) 
            break
        stat_cost = Label(shop_window, text = "Rs."+str(cost_of_stat)) 
        stat_cost.grid(row=6, column=5, padx = 50, pady = 20)

        stat_cost = Label(shop_window, text = "0") 
        stat_cost.grid(row=6, column=5, padx = 50, pady = 20)

    add_stat = Button(shop_window, text = "Add Item", command=lambda:[create_bill(clicked_stat.get(), stat_qty_txt.get(), stationery[-1]), total_cost(stationery[-1]), update_total()])
    add_stat.grid(row = 6, column=6)

    logOut_button = Button(shop_window, text = "Logout", width=20, command=shop_window.destroy)
    logOut_button.grid(row =0, column=6)

    payment_options= ["Cash", "Credit Card", "Debit Card"] 
    pay_var = StringVar()
    pay_var.set(payment_options[0])
    payment_drop = OptionMenu(shop_window, pay_var, *payment_options) 
    payment_drop.grid(row = 7, column=6)

    def add_final_amt_to_file():
        add_total = open("bill_file.txt", "a+") 
        add_total.write("Total = Rs."+str(total))

    def select_payment():
        if(pay_var.get() == "Credit Card" or pay_var.get() == "Debit Card"): 
            payment()
        elif(pay_var.get() == "Cash"): 
            messagebox.showinfo("Success","Thank You for Choosing Us!") 
            shop_window.destroy()
    
    pay_bill = Button(shop_window, text= "Proceed to Payment", command=lambda:[add_final_amt_to_file(), select_payment()])
    pay_bill.grid(row=8, column = 6, pady = 20)



def payment():
    payment_window = Toplevel() 
    payment_window.geometry("1000x600")
    #payment_window.iconbitmap("G:/My Drive/Market Billing System/Misc/Icon Image.ico")

    payment_frame = LabelFrame(payment_window, padx = 30, pady = 30) 
    payment_frame.place(x=200, y=70)

    #enter card details
    enter_details = Label(payment_frame, text="Enter Card Details:") 
    enter_details.grid(row = 0, column = 0)

    #card type
    card = StringVar() 
    card.set("Credit Card")
    card_options = ["Credit Card", "Debit Card"]
    card_dropmenu = OptionMenu(payment_frame, card, *card_options) 
    card_dropmenu.grid(row=1, column = 0)

    #card number
    cardNo_label = Label(payment_frame, text = "Card No: ") 
    cardNo_label.grid(row = 2, column = 0)
    cardNo_entry1 = Entry(payment_frame, borderwidth=5) 
    cardNo_entry1.grid(row = 2,  column  =  1) 
    cardNo_entry2 = Entry(payment_frame, borderwidth=5) 
    cardNo_entry2.grid(row = 2,  column  =  2) 
    cardNo_entry3 = Entry(payment_frame, borderwidth=5) 
    cardNo_entry3.grid(row = 2,  column  =  3) 
    cardNo_entry4 = Entry(payment_frame, borderwidth=5) 
    cardNo_entry4.grid(row = 2, column = 4)

    #date of expiry
    expiryDate_label = Label(payment_frame, text= "Expiry Date: ") 
    expiryDate_label.grid(row=3, column=0)
    expiryDate_entry = Entry(payment_frame, borderwidth=5) 
    expiryDate_entry.grid(row=3, column = 1)

    #cvv
    cvv_label = Label(payment_frame, text = "CVV: ") 
    cvv_label.grid(row=3, column=2)
    
    cvv_entry = Entry(payment_frame) 
    cvv_entry.grid(row=3, column=3)

    #name on the card
    nameCard_label = Label(payment_frame, text= "Name on the Card: ") 
    nameCard_label.grid(row=4, column=0)
    nameCard_entry = Entry(payment_frame, borderwidth=5) 
    nameCard_entry.grid(row=4, column=1)

    #make payment
    makePay = Button(payment_frame, text="Make Payment", command=lambda:[messagebox.showinfo("Success",  "Payment  Successful\nThank You for Choosing Us!"), shop_window.destroy(), payment_window.destroy()])
    makePay.grid(row=5, column=4)


reg_label = Label(mainWindow, text = "Not a Member?") 
reg_label.place(x= 800, y = 70)
reg_Button = Button(mainWindow, text="Register", padx = 10, command=reg_window)
reg_Button.place(x=900, y=70)


#sign-in frame widget
sign_in_Frame = LabelFrame(mainWindow, text = "Sign In", padx = 30, pady = 30)
sign_in_Frame.place(x  =  300,  y  = 150)

email_label = Label(sign_in_Frame, text = "Email Id : ") 
email_label.grid(row = 0, column = 0)
email_entry = Entry(sign_in_Frame, borderwidth=5) 
email_entry.grid(row = 0, column = 1)
pswd_label = Label(sign_in_Frame, text = "Password : ") 
pswd_label.grid(row = 1, column = 0)
pswd_entry = Entry(sign_in_Frame, borderwidth=5) 
pswd_entry.grid(row = 1, column = 1)
submit_button = Button(sign_in_Frame, text = "Submit", command=check_record_exist)
submit_button.grid(row = 2, column=2) 

#write total cost to the file

#close bill file 
bill.close()

mainWindow.mainloop()
