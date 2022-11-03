from datetime import date
import mysql.connector
from tkinter import *
import tkinter.messagebox as message_box

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="herbm"
)

mycursor = mydb.cursor()


def customer():
    def search_herbs():
        search_window = Tk()
        search_window.geometry("500x300")
        search_window.title('Search')
        l1 = Label(search_window, text="Enter herb Uses")
        l1.place(x=20, y=80)

        e5 = Entry(search_window)
        e5.place(x=200, y=80)

        l2 = Button(search_window, text="Search", command=lambda: search_ex(e5.get()))
        l2.place(x=250, y=150)

    def search_ex(result):
        mycursor.execute('select * from herbs where uses=%s;', (result,))
        mycursor.fetchall()
        if mycursor.rowcount == 1:

            Herb_window1 = Tk()
            herb_id = Label(Herb_window1, text='Herb ID')
            herb_id.grid(row=0, column=0)

            iname = Label(Herb_window1, text='English Name')
            iname.grid(row=0, column=1)

            idec = Label(Herb_window1, text='Botanical Name')
            idec.grid(row=0, column=2)

            idec1 = Label(Herb_window1, text='Uses')
            idec1.grid(row=0, column=3)

            idec2 = Label(Herb_window1, text='Quantity In Stock')
            idec2.grid(row=0, column=4)

            ip = Label(Herb_window1, text='Country of Origin')
            ip.grid(row=0, column=5)

            qs = Label(Herb_window1, text='Herb Price')
            qs.grid(row=0, column=6)
            mycursor.execute('select * from herbs where uses=%s;', (result,))

            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(Herb_window1, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            l2 = Button(Herb_window1, text="Quit", command=lambda: Herb_window1.destroy())
            l2.grid(row=i + 2, column=3)
        else:
            message_box.showwarning('Error', 'Invalid Input! Please check your spelling or Your item is not listed!!')

    def show_herbs():
        Herb_window = Tk()
        herb_id = Label(Herb_window, text='Herb ID')
        herb_id.grid(row=0, column=0)

        iname = Label(Herb_window, text='English Name')
        iname.grid(row=0, column=1)

        idec = Label(Herb_window, text='Botanical Name')
        idec.grid(row=0, column=2)

        idec1 = Label(Herb_window, text='Uses')
        idec1.grid(row=0, column=3)

        idec2 = Label(Herb_window, text='Quantity In Stock')
        idec2.grid(row=0, column=4)

        ip = Label(Herb_window, text='Country of Origin')
        ip.grid(row=0, column=5)

        qs = Label(Herb_window, text='Herb Price')
        qs.grid(row=0, column=6)

        mycursor.execute("select * from herbs")
        i = 1
        for x in mycursor.fetchall():
            for j in range(len(x)):
                e = Entry(Herb_window, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(0, x[j])
            i = i + 1

    def order_lists1():
        insert_window = Tk()
        insert_window.geometry("600x500")

        l1 = Button(insert_window, text="Add herbs", command=lambda: herbs_insert())
        l1.place(x=20, y=20)

        l1 = Label(insert_window, text="Enter Total Order Price")
        l1.place(x=20, y=80)

        l1 = Label(insert_window, text="Enter Customer ID")
        l1.place(x=20, y=140)

        e4 = Entry(insert_window)
        e4.place(x=200, y=80)

        e5 = Entry(insert_window)
        e5.place(x=200, y=140)

        insert_into = Button(insert_window, text='ADD',
                             command=lambda: insert_values_orders(e4.get(), e5.get(), herb_id_list,
                                                                  quantity_ordered_list))
        insert_into.place(x=200, y=200)

    def insert_values_orders(oprice, uid, herb_list, quantity_list):
        odate = date.today()
        print(odate)
        mycursor.execute('INSERT INTO orders(order_date, total_price, customer_id) VALUES(%s,%s,%s)',
                         (odate, oprice, uid,))
        mydb.commit()

        mycursor.execute('select order_id from orders order by order_id desc limit 1')
        oid = mycursor.fetchall()[0][0]

        for i in range(0, len(herb_list)):
            mycursor.execute('insert into contain(order_id,herb_id, quantity_ordered) values(%s, %s, %s)',
                             (oid, herb_list[i], quantity_list[i]))
        mydb.commit()
        herb_id_list.clear()
        quantity_ordered_list.clear()

    herb_id_list = []
    quantity_ordered_list = []

    def herbs_insert():
        insert_window = Tk()
        insert_window.geometry("600x300")
        l1 = Label(insert_window, text="Enter herb ID")
        l1.place(x=20, y=20)

        a = Entry(insert_window)
        a.place(x=150, y=20)

        l2 = Label(insert_window, text="Enter QUANTITY ORDERED")
        l2.place(x=20, y=60)

        b = Entry(insert_window)
        b.place(x=200, y=60)

        herbs = Button(insert_window, text="OHKK", command=lambda: fetch_herb_id(a.get(), b.get()))
        herbs.place(x=20, y=150)

    def fetch_herb_id(herb_id, quantity_ordered):
        herb_id_list.append(herb_id)
        quantity_ordered_list.append(quantity_ordered)

    newWindow1 = Tk()
    newWindow1.geometry("500x300")

    show_inventory = Button(newWindow1, text="Show All herbs", command=show_herbs)
    show_inventory.place(x=80, y=40)
    show_order_lists = Button(newWindow1, text='Show order lists', command=order_lists1)
    show_order_lists.place(x=200, y=40)
    search_herbs = Button(newWindow1, text='Search', command=search_herbs)
    search_herbs.place(x=350, y=40)


def login_user():
    admin_username = admin_id_entry.get()
    admin_password = admin_pass_entry.get()
    mycursor.execute('select * from admin where admin_name=%s and admin_pass=%s;', (admin_username, admin_password))
    mycursor.fetchall()
    if mycursor.rowcount == 1:
        def inventory():
            Herb_window = Toplevel(newWindow)
            herb_id = Label(Herb_window, text='Herb ID')
            herb_id.grid(row=0, column=0)

            iname = Label(Herb_window, text='English Name')
            iname.grid(row=0, column=1)

            idec = Label(Herb_window, text='Botanical Name')
            idec.grid(row=0, column=2)

            idec1 = Label(Herb_window, text='Uses')
            idec1.grid(row=0, column=3)

            idec2 = Label(Herb_window, text='Quantity In Stock')
            idec2.grid(row=0, column=4)

            ip = Label(Herb_window, text='Country of Origin')
            ip.grid(row=0, column=5)

            qs = Label(Herb_window, text='Herb Price')
            qs.grid(row=0, column=6)

            mycursor.execute("select * from herbs")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(Herb_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            btn = Button(Herb_window, text="Add herb", command=lambda: add_product())
            btn.grid(row=i + 2, column=1)

            btn = Button(Herb_window, text="Delete herb", command=lambda: remove_product())
            btn.grid(row=i + 2, column=2)

            btn = Button(Herb_window, text="Restock Herbs", command=lambda: restock())
            btn.grid(row=i + 2, column=3)

        def add_product():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("1000x500")
            l1 = Label(insert_window, text="Enter English Name")
            l1.place(x=20, y=20)

            l1 = Label(insert_window, text="Enter Botanical Name")
            l1.place(x=20, y=80)

            l1 = Label(insert_window, text="Enter Uses")
            l1.place(x=20, y=140)

            l1 = Label(insert_window, text="Enter Quantity")
            l1.place(x=20, y=200)

            l1 = Label(insert_window, text="Enter country of origin")
            l1.place(x=20, y=260)

            l1 = Label(insert_window, text="Enter Herb Price")
            l1.place(x=20, y=320)

            e1 = Entry(insert_window)
            e1.place(x=200, y=20)

            e2 = Entry(insert_window)
            e2.place(x=200, y=80)

            e3 = Entry(insert_window)
            e3.place(x=200, y=140)

            e4 = Entry(insert_window)
            e4.place(x=200, y=200)

            e5 = Entry(insert_window)
            e5.place(x=200, y=260)

            e6 = Entry(insert_window)
            e6.place(x=200, y=320)

            insert_into = Button(insert_window, text='INSERT INTO INVENTORY',
                                 command=lambda: insert_values_inventory(e1.get(), e2.get(), e3.get(), e4.get(),
                                                                         e5.get(), e6.get()))
            insert_into.place(x=300, y=390)

        def insert_values_inventory(iname, idec, idec1, idec2, ip, qs):
            mycursor.execute('Insert into herbs(common_name, botanical_name,Uses, quantity_in_stock,country_of_origin,'
                             'herb_price)'
                             ' values(%s, %s, %s, %s, %s, %s)', (iname, idec, idec1, idec2, ip, qs))
            mydb.commit()

        def remove_product():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("300x300")
            l1 = Label(insert_window, text="Enter Herb ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insert_window)
            e1.place(x=200, y=20)

            insert_into = Button(insert_window, text='DELETE',
                                 command=lambda: delete_product(e1.get()))
            insert_into.place(x=60, y=80)

        def delete_product(herb_id):
            mycursor.execute('delete from herbs where herb_id=%s', (herb_id,))
            mydb.commit()

        def restock():
            another_window = Toplevel(newWindow)
            another_window.geometry('500x200')
            lbl = Label(another_window, text="Enter herb Id to be Restocked")
            lbl.place(x=20, y=20)

            en = Entry(another_window)
            en.place(x=250, y=20)

            bt = Button(another_window, text="Restock", command=lambda: restock_query(en.get()))
            bt.place(x=150, y=75)

        def restock_query(herb_id):
            mycursor.execute(
                'update herbs set quantity_in_stock = quantity_in_stock + 50 where herb_id = %s', (herb_id,))
            mydb.commit()

        def order_lists():
            order_window = Toplevel(newWindow)

            order_id = Label(order_window, text='ORDER ID')
            order_id.grid(row=0, column=0)

            od = Label(order_window, text='ORDER DATE')
            od.grid(row=0, column=1)

            tp = Label(order_window, text='TOTAL PRICE')
            tp.grid(row=0, column=2)

            ui = Label(order_window, text='Customer ID')
            ui.grid(row=0, column=3)

            mycursor.execute("select * from orders")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(order_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            lbl = Label(order_window, text="Enter Order ID to view")
            lbl.grid(row=i + 3, column=1)
            order_entry = Entry(order_window, width=10)
            order_entry.grid(row=i + 3, column=2)
            btn = Button(order_window, text="OHKK", command=lambda: show_order(order_entry.get()))
            btn.grid(row=i + 3, column=3)

            create_user = Button(order_window, text='ADD ORDER', command=lambda: insert_order())
            create_user.grid(row=i + 3, column=0)

        def show_order(oid):
            so_window = Toplevel(newWindow)
            oii = Label(so_window, text='ORDER herb ID')
            oii.grid(row=0, column=0)

            ii = Label(so_window, text='herb ID')
            ii.grid(row=0, column=1)

            oi = Label(so_window, text='ORDER ID')
            oi.grid(row=0, column=2)

            qo = Label(so_window, text='QUANTITY ORDERED')
            qo.grid(row=0, column=3)

            it_nm = Label(so_window, text='Common Name')
            it_nm.grid(row=0, column=4)

            it_ds = Label(so_window, text='Botanical Name')
            it_ds.grid(row=0, column=5)

            it_ds = Label(so_window, text='Uses')
            it_ds.grid(row=0, column=6)

            it_ds = Label(so_window, text='country_of_origin')
            it_ds.grid(row=0, column=7)

            ip = Label(so_window, text='Herb PRICE')
            ip.grid(row=0, column=8)

            mycursor.execute(
                "select contain.order_herb_id, contain.herb_id, contain.order_id, contain.quantity_ordered,"
                " herbs.common_name, herbs.botanical_name,herbs.uses,herbs.country_of_origin, herbs.herb_price"
                " from contain inner join  herbs on contain.herb_id = herbs.herb_id"
                " where order_id=%s", (oid,)
            )

            l = 1
            for x in mycursor.fetchall():
                for y in range(len(x)):
                    e = Entry(so_window, width=10, fg='blue')
                    e.grid(row=l, column=y)
                    e.insert(END, x[y])
                l = l + 1

            lbl = Label(so_window, text="Enter Order herb ID to be completed")
            lbl.grid(row=l + 1, column=3)
            order_update = Entry(so_window, width=10)
            order_update.grid(row=l + 2, column=3)
            btn = Button(so_window, text="OHKK", command=lambda: update_inventory(order_update.get()))
            btn.grid(row=l + 3, column=3)

        def insert_order():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("600x500")

            l1 = Button(insert_window, text="Add herbs", command=lambda: herbs_insert())
            l1.place(x=20, y=20)

            l1 = Label(insert_window, text="Enter Total Order Price")
            l1.place(x=20, y=80)

            l1 = Label(insert_window, text="Enter Customer ID")
            l1.place(x=20, y=140)

            e4 = Entry(insert_window)
            e4.place(x=200, y=80)

            e5 = Entry(insert_window)
            e5.place(x=200, y=140)

            insert_into = Button(insert_window, text='ADD',
                                 command=lambda: insert_values_orders(e4.get(), e5.get(), herb_id_list,
                                                                      quantity_ordered_list))
            insert_into.place(x=200, y=200)

        def insert_values_orders(oprice, uid, herb_list, quantity_list):
            odate = date.today()
            print(odate)
            mycursor.execute('INSERT INTO orders(order_date, total_price, customer_id) VALUES(%s,%s,%s)',
                             (odate, oprice, uid,))
            mydb.commit()

            mycursor.execute('select order_id from orders order by order_id desc limit 1')
            oid = mycursor.fetchall()[0][0]

            for i in range(0, len(herb_list)):
                mycursor.execute('insert into contain(order_id,herb_id, quantity_ordered) values(%s, %s, %s)',
                                 (oid, herb_list[i], quantity_list[i]))
            mydb.commit()
            herb_id_list.clear()
            quantity_ordered_list.clear()

        herb_id_list = []
        quantity_ordered_list = []

        def herbs_insert():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("600x300")
            l1 = Label(insert_window, text="Enter herb ID")
            l1.place(x=20, y=20)

            a = Entry(insert_window)
            a.place(x=150, y=20)

            l2 = Label(insert_window, text="Enter QUANTITY ORDERED")
            l2.place(x=20, y=60)

            b = Entry(insert_window)
            b.place(x=200, y=60)

            herbs = Button(insert_window, text="OHKK", command=lambda: fetch_herb_id(a.get(), b.get()))
            herbs.place(x=20, y=150)

        def fetch_herb_id(herb_id, quantity_ordered):
            herb_id_list.append(herb_id)
            quantity_ordered_list.append(quantity_ordered)

        def update_inventory(order_herb_id):
            mycursor.execute('select herb_id, order_id, quantity_ordered from contain where order_herb_id=%s',
                             (order_herb_id,))

            herb_id, order_herb_id, quantity_ordered = mycursor.fetchall()[0]

            mycursor.execute('select quantity_in_stock from herbs where herb_id = %s', (herb_id,))
            quantity_in_stock = mycursor.fetchall()[0][0]

            if quantity_in_stock >= quantity_ordered:
                mycursor.execute(
                    'update herbs set quantity_in_stock = quantity_in_stock - %s where herb_id = %s',
                    (quantity_ordered, herb_id,))
                mydb.commit()

                mycursor.execute('select count(*) from contain where order_id=%s', (str(order_herb_id),))
                rows = mycursor.fetchall()[0][0]
                if rows == 1:
                    mycursor.execute('delete from orders where order_id=%s', (order_herb_id,))
                    mydb.commit()
                mycursor.execute('delete from contain where order_herb_id=%s', (order_herb_id,))
                mydb.commit()

            else:
                message_box.showwarning('Error', 'Required quantity not available')

        # mycursor.execute('select * from herbs')
        # for x in mycursor.fetchall():
        #     print(x)

        def users():
            user_window = Toplevel(newWindow)

            uid = Label(user_window, text='Customer ID')
            uid.grid(row=0, column=0)

            fname = Label(user_window, text='NAME')
            fname.grid(row=0, column=1)

            lname = Label(user_window, text='Customer password')
            lname.grid(row=0, column=2)

            uadd = Label(user_window, text='Customer ADDRESS')
            uadd.grid(row=0, column=3)

            uadd1 = Label(user_window, text='Country')
            uadd1.grid(row=0, column=4)

            mycursor.execute("select * from customer")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(user_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            create_user = Button(user_window, text='ADD USER', command=lambda: insert_user())
            create_user.grid(row=1, column=6)

            del_user = Button(user_window, text='DELETE USER', command=lambda: delete_user())
            del_user.grid(row=2, column=6)

        def insert_user():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("500x300")
            l1 = Label(insert_window, text="Enter User's first name")
            l1.place(x=20, y=20)

            l1 = Label(insert_window, text="Enter customer password")
            l1.place(x=20, y=80)

            l1 = Label(insert_window, text="Enter User's address")
            l1.place(x=20, y=140)

            e1 = Entry(insert_window)
            e1.place(x=200, y=20)

            e2 = Entry(insert_window)
            e2.place(x=200, y=80)

            e3 = Entry(insert_window)
            e3.place(x=200, y=140)

            insert_into = Button(insert_window, text='INSERT',
                                 command=lambda: insert_values_users(e1.get(), e2.get(), e3.get()))
            insert_into.place(x=300, y=270)

        def insert_values_users(ufname, ulname, uadd):
            mycursor.execute('INSERT INTO customer(customer_name,customer_pass,customer_address) VALUES(%s,%s,%s)',
                             (ufname, ulname, uadd,))
            mydb.commit()

        def delete_user():
            insert_window = Toplevel(newWindow)
            insert_window.geometry("500x300")
            l1 = Label(insert_window, text="Enter User ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insert_window)
            e1.place(x=200, y=20)

            insert_into = Button(insert_window, text='DELETE',
                                 command=lambda: remove_user(e1.get()))
            insert_into.place(x=60, y=80)

        def remove_user(user_id):
            mycursor.execute('delete from users where user_id=%s', (user_id,))
            mydb.commit()

        newWindow = Tk()
        newWindow.geometry("500x300")

        show_inventory = Button(newWindow, text="Show herbs", command=inventory)
        show_inventory.place(x=20, y=20)

        show_order_lists = Button(newWindow, text='Show order lists', command=order_lists)
        show_order_lists.place(x=150, y=20)

        show_users = Button(newWindow, text='Show customers', command=users)
        show_users.place(x=300, y=20)

    else:
        print(mycursor.rowcount)
        message_box.showwarning('Error', 'Invalid login credentials')


root = Tk()
root.geometry("600x300")
root.title('Herb Inventory')

adid = Label(root, text="Enter Admin ID: ")
adid.place(x=120, y=30)

password = Label(root, text="Enter password: ")
password.place(x=120, y=60)

admin_id_entry = Entry(root)
admin_id_entry.place(x=250, y=30)

admin_pass_entry = Entry(root, show='*')
admin_pass_entry.place(x=250, y=60)

login_button = Button(root, text="Login", command=login_user, height=2, width=7)
login_button.place(x=250, y=130)

login_button2 = Button(root, text="Customer", command=customer, height=2, width=7)
login_button2.place(x=500, y=250)

root.mainloop()
