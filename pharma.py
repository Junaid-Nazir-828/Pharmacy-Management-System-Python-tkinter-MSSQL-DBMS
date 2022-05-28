from tkinter import *
from tkinter import ttk
import sys
import pypyodbc as odbc
from tkinter import messagebox


class PharmacyManagementSystem:
    arg1 = None  # root in the constructor

    def __init__(self, arg1):  # root from main will be passed as arg1

        # variables used in database connection function at line number 249
        self.database_name = None
        self.server_name = None
        self.conn = None
        self.cursor = None

        # variables for storing entered text in entry boxes
        self.ref_var = StringVar()
        self.comp_var = StringVar()
        self.typ_var = StringVar()
        self.nam_var = StringVar()
        self.lot_var = StringVar()
        self.issue_var = StringVar()
        self.expire_var = StringVar()
        self.use_var = StringVar()
        self.side_var = StringVar()
        self.price_var = StringVar()

        # here r represents root
        self.r = arg1
        self.r.title("Pharmacy Management System")
        self.r.geometry("1550x800")

        label = Label(self.arg1, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg='white'
                      , fg='green', font=("times new roman", 50, "bold"), padx=2, pady=4)
        label.pack(side=TOP, fill=X)

        # ------------------------------------Data Frames---------------------------------------- #
        # Data Frame below label
        data_frame = Frame(self.arg1, bd=15, relief=RIDGE, padx=20)
        data_frame.place(x=0, y=120, width=1280, height=400)

        # Data Frame inside  data_frame at left side
        data_frame_left = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", fg="green",
                                     font=("arial", 12, "bold"))
        data_frame_left.place(x=0, y=5, width=800, height=350)

        # Data Frame inside data_frame at right side
        data_frame_right = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=20, fg="green",
                                      font=("arial", 12, "bold"))
        data_frame_right.place(x=810, y=5, width=400, height=350)
        # ---------------------------------------------------------------------------------------- #

        # -------------------------------Inside Left Data Frame----------------------------------- #

        #   Empty Column
        empty_label_1 = Label(data_frame_left, text="          ")
        empty_label_1.grid(row=0, column=0, padx=2, pady=6)

        # Reference No.:
        ref_label = Label(data_frame_left, text="Reference No.:", font=("arial", 12, "bold"))
        ref_label.grid(row=0, column=1, padx=2, pady=6)
        ref_entry = Entry(data_frame_left, textvariable=self.ref_var, font=("arial", 12, "bold"), bg="white", bd=2,
                          relief=RIDGE, width=15)
        ref_entry.grid(row=0, column=2)

        # Company Name:
        company_name_label = Label(data_frame_left, text="Company Name:", font=("arial", 12, "bold"))
        company_name_label.grid(row=1, column=1, padx=2, pady=6)
        company_name_entry = Entry(data_frame_left, textvariable=self.comp_var, font=("arial", 12, "bold"), bg="white",
                                   bd=2, relief=RIDGE,
                                   width=15)
        company_name_entry.grid(row=1, column=2)

        # Type of Medicine:
        med_typ_label = Label(data_frame_left, text="Type of Medicine:", font=("arial", 12, "bold"))
        med_typ_label.grid(row=2, column=1, padx=2, pady=6)

        med_typ_combo = ttk.Combobox(data_frame_left, textvariable=self.typ_var, width=13, font=("arial", 12, "bold"),
                                     state="readonly")
        med_typ_combo["values"] = ("None", "Liquid", "Tablet", "Capsule", "Drops", "Inhaler", "Injection", "patches")
        med_typ_combo.grid(row=2, column=2)
        med_typ_combo.current(0)

        # Name of Medicine
        med_name_label = Label(data_frame_left, text="Medicine Name:", font=("arial", 12, "bold"))
        med_name_label.grid(row=3, column=1, padx=2, pady=6)
        med_name_entry = Entry(data_frame_left, textvariable=self.nam_var, font=("arial", 12, "bold"), bg="white", bd=2,
                               relief=RIDGE, width=15)
        med_name_entry.grid(row=3, column=2)

        # Lot No.:
        lot_no_label = Label(data_frame_left, text="Lot No.:", font=("arial", 12, "bold"))
        lot_no_label.grid(row=4, column=1, padx=2, pady=6)
        lot_no_entry = Entry(data_frame_left, textvariable=self.lot_var, font=("arial", 12, "bold"), bg="white", bd=2,
                             relief=RIDGE, width=15)
        lot_no_entry.grid(row=4, column=2)

        # Issue Date:
        issue_date_label = Label(data_frame_left, text="Issue Date:", font=("arial", 12, "bold"))
        issue_date_label.grid(row=5, column=1, padx=2, pady=6)
        issue_date_entry = Entry(data_frame_left, textvariable=self.issue_var, font=("arial", 12, "bold"), bg="white",
                                 bd=2, relief=RIDGE, width=15)
        issue_date_entry.grid(row=5, column=2)

        # Expiry Date:
        expiry_date_label = Label(data_frame_left, text="Expiry Date:", font=("arial", 12, "bold"))
        expiry_date_label.grid(row=6, column=1, padx=2, pady=6)
        expiry_date_entry = Entry(data_frame_left, textvariable=self.expire_var, font=("arial", 12, "bold"), bg="white",
                                  bd=2, relief=RIDGE, width=15)
        expiry_date_entry.grid(row=6, column=2)

        # Uses:
        uses_label = Label(data_frame_left, text="Uses:", font=("arial", 12, "bold"))
        uses_label.grid(row=7, column=1, padx=2, pady=6)
        uses_entry = Entry(data_frame_left, textvariable=self.use_var, font=("arial", 12, "bold"), bg="white", bd=2,
                           relief=RIDGE, width=15)
        uses_entry.grid(row=7, column=2)

        #   Empty Column
        empty_label_2 = Label(data_frame_left, text="                               ")
        empty_label_2.grid(row=0, column=3, padx=2, pady=6)

        # Side Effect:
        side_eff_label = Label(data_frame_left, text="Side Effects:", font=("arial", 12, "bold"))
        side_eff_label.grid(row=0, column=4, padx=2, pady=6)
        side_eff_entry = Entry(data_frame_left, textvariable=self.side_var, font=("arial", 12, "bold"), bg="white",
                               bd=2, relief=RIDGE, width=15, )
        side_eff_entry.grid(row=0, column=5)

        # Price:
        price_label = Label(data_frame_left, text="Price:", font=("arial", 12, "bold"))
        price_label.grid(row=1, column=4, padx=2, pady=6)
        price_entry = Entry(data_frame_left, textvariable=self.price_var, font=("arial", 12, "bold"), bg="white", bd=2,
                            relief=RIDGE, width=15)
        price_entry.grid(row=1, column=5)

        # ------------------------------------Button Frame---------------------------------------- #
        # Button Frame below Data Frame
        button_frame = Frame(self.arg1, bd=15, relief=RIDGE, padx=10)
        button_frame.place(x=0, y=520, width=1280, height=60)

        # Add Button inside button_frame
        add_button = Button(button_frame, text="  Add  ", fg="green", font=("arial", 12, "bold"),
                            command=lambda: self.add_data())
        add_button.grid(row=0, column=0, padx=20)

        # Update Button inside button_frame
        update_button = Button(button_frame, text="Update", fg="green", font=("arial", 12, "bold"),
                               command=lambda: self.update())
        update_button.grid(row=0, column=1, padx=20)

        # Delete Button inside button_frame
        delete_button = Button(button_frame, text="Delete", fg="green", font=("arial", 12, "bold"),
                               command=lambda: self.delete())
        delete_button.grid(row=0, column=3, padx=20)

        # Reset Button inside button_frame
        reset_button = Button(button_frame, text=" Reset ", fg="green", font=("arial", 12, "bold"),
                              command=lambda: self.reset())
        reset_button.grid(row=0, column=4, padx=20)

        # Exit Button inside button_frame
        exit_button = Button(button_frame, text="  Exit  ", fg="green", font=("arial", 12, "bold"))
        exit_button.grid(row=0, column=5, padx=20)

        # Searching:
        # adding label for "Search By:"
        search_label = Label(button_frame, text="Search By:", fg="red", font=("arial", 12, "bold"))
        search_label.grid(row=0, column=6, padx=20)

        # variables used in searching:
        self.search_var = StringVar()
        self.search_text = StringVar()

        # search combo
        search_combo = ttk.Combobox(button_frame, textvariable=self.search_var, width=18, font=("arial", 10, "bold"),
                                    state="readonly")
        search_combo["values"] = ("Reference Number", "Medicine Name", "Lot Number")
        search_combo.grid(row=0, column=7, padx=15)
        search_combo.current(0)

        # Entry for searching
        search_entry = Entry(button_frame, textvariable=self.search_text, bd=3, relief=RIDGE, width=12,
                             font=("arial", 12, "bold"))
        search_entry.grid(row=0, column=8, padx=20)

        # Search Button
        search_button = Button(button_frame, text=" Search ", fg="green", font=("arial", 12, "bold"),
                               command=lambda: self.search())
        search_button.grid(row=0, column=9, padx=20)

        # Show All Button
        search_button = Button(button_frame, text=" Show All ", fg="green", font=("arial", 12, "bold"),
                               command=lambda: self.get_data())
        search_button.grid(row=0, column=10, padx=20)
        # ---------------------------------------------------------------------------------------- #

        # ------------------------------------Detail Frame---------------------------------------- #
        detail_frame = Frame(self.arg1, bd=15, relief=RIDGE, padx=10)
        detail_frame.place(x=0, y=580, width=1280, height=400)

        # Table in Right Frame
        table_frame = Frame(detail_frame, bd=10, relief=RIDGE)
        table_frame.place(x=0, y=1, width=1230, height=370)

        # Scroll Bars
        scroll_x_2 = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x_2.pack(side=BOTTOM, fill=X)
        scroll_y_2 = ttk.Scrollbar(table_frame, orient=VERTICAL)
        scroll_y_2.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(table_frame, columns=("ref", "comp_name", "type", "med_name", "lot_no",
                                                                 "issue_date", "expire_date", "uses", "side_eff",
                                                                 "price"))
        scroll_x_2.pack(side=BOTTOM, fill=X)
        scroll_y_2.pack(side=RIGHT, fill=Y)

        scroll_x_2.config(command=self.pharmacy_table.xview)
        scroll_y_2.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("ref", text="Reference No.")
        self.pharmacy_table.heading("comp_name", text="Company Name")
        self.pharmacy_table.heading("type", text="Type")
        self.pharmacy_table.heading("med_name", text="Name")
        self.pharmacy_table.heading("lot_no", text="Lot No.")
        self.pharmacy_table.heading("issue_date", text="Issue Date")
        self.pharmacy_table.heading("expire_date", text="Expiry Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("side_eff", text="Side Effects")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("ref", width=100)
        self.pharmacy_table.column("comp_name", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("med_name", width=100)
        self.pharmacy_table.column("lot_no", width=100)
        self.pharmacy_table.column("issue_date", width=100)
        self.pharmacy_table.column("expire_date", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("side_eff", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)

    def connect_database(self):
        self.database_name = 'Pharmacy Management System'
        self.server_name = 'YOUR_SERVER_NAME'   # put your server name inside ''
        try:
            self.conn = odbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                        SERVER=' + self.server_name + ';\
                                        DATABASE=' + self.database_name + ';\
                                        Trusted_Connection=yes')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
            print("Operation Failed")
            messagebox.showerror("Error!", "Connection to DataBase Failed")
            sys.exit()

    def add_data(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Reference Number must not be NULL")
        else:
            self.connect_database()
            query = '''INSERT INTO pharma VALUES(?,?,?,?,?,?,?,?,?,?)'''
            record = [self.ref_var.get(), self.comp_var.get(), self.typ_var.get(), self.nam_var.get(),
                      self.lot_var.get(),
                      self.issue_var.get(), self.expire_var.get(), self.use_var.get(), self.side_var.get(),
                      self.price_var.get()]

            try:
                self.cursor.execute(query, record)
            except Exception as e:
                self.cursor.rollback()
                print(e)
                print("Cursor Rollback")
                messagebox.showerror("Error!", "Insertion Failed")
            else:
                self.cursor.commit()
                self.get_data()
                self.cursor.close()
                print("Data Insertion Successful")
                messagebox.showinfo("Success ", "Insertion Successful")
            finally:
                if self.conn.connected == 1:
                    self.conn.close()
                    print("Connection Closed")

    def get_data(self):
        self.connect_database()
        query = '''SELECT * FROM pharma'''

        try:
            self.cursor.execute(query)
            row = self.cursor.fetchall()
            if len(row) != 0 or len(row) == 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                    self.pharmacy_table.insert("", END, values=i)
        except Exception as e:
            self.cursor.rollback()
            print(e)
            print("Cursor Roll backed")
            messagebox.showerror("Error!", "Failed to Show Data")
        else:
            self.cursor.commit()
            self.cursor.close()
            print("all records retrieved")
        finally:
            if self.conn.connected == 1:
                self.conn.close()
                print('Connection Closed')

    def get_cursor(self, ev):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0])
        self.comp_var.set(row[1])
        self.typ_var.set(row[2])
        self.nam_var.set(row[3])
        self.lot_var.set(row[4])
        self.issue_var.set(row[5])
        self.expire_var.set(row[6])
        self.use_var.set(row[7])
        self.side_var.set(row[8])
        self.price_var.set(row[9])

    def update(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Reference Number Required")
        else:
            self.connect_database()

            query = "UPDATE pharma set comp_name = '" + self.comp_var.get() + "' ,typ = '" + self.typ_var.get() +\
                    "' ,med_name = '" + self.nam_var.get() + "' ,lot_no = '" + self.lot_var.get() + "' ,issue = '" +\
                    self.issue_var.get() + "' ,expire = '" + self.expire_var.get() + "' ,uses = '" + self.use_var.get()\
                    + "' ,side_eff = '" + self.side_var.get() + "' ,price = '" + self.ref_var.get() +\
                    "' where ref_no = " + self.ref_var.get()
            try:
                self.cursor.execute(query)
            except Exception as e:
                self.cursor.rollback()
                print(e)
                print("Cursor Roll backed")
                messagebox.showerror("Error!", "Failed to update")
            else:
                self.cursor.commit()
                self.get_data()
                self.cursor.close()
                print("Update Successful")
                messagebox.showinfo("Success", "Update Successful")
            finally:
                if self.conn.connected == 1:
                    self.conn.close()
                    print('Connection Closed')

    def delete(self):
        self.connect_database()

        query = "DELETE from pharma where ref_no = " + self.ref_var.get()
        try:
            self.cursor.execute(query)
        except Exception as e:
            self.cursor.rollback()
            print(e)
            print("Cursor Roll backed")
            messagebox.showerror("Error!", "Failed to delete")
        else:
            self.cursor.commit()
            self.reset()
            self.get_data()
            self.cursor.close()
            print("Delete Successful")
            messagebox.showinfo("Success", "Delete Successful")
        finally:
            if self.conn.connected == 1:
                self.conn.close()
                print('Connection Closed')

    def reset(self):
        self.comp_var.set("")
        self.typ_var.set("")
        self.nam_var.set("")
        self.lot_var.set("")
        self.issue_var.set("")
        self.expire_var.set("")
        self.use_var.set("")
        self.side_var.set("")
        self.price_var.set("")

    def search(self):
        self.connect_database()

        temp_var = ""
        if self.search_var.get() == "Reference Number":
            temp_var = "ref_no"
        elif self.search_var.get() == "Medicine Name":
            temp_var = "med_name"
        elif self.search_var.get() == "Lot Number":
            temp_var = "lot_no"

        query = "SELECT * from pharma WHERE " + temp_var + " LIKE '" + self.search_text.get() + "'"
        print(query)
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                    self.pharmacy_table.insert("", END, values=i)
            else:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                messagebox.showerror("Error!", "No Item Found")
        except Exception as e:
            self.cursor.rollback()
            print(e)
            print("Cursor Roll backed")
            messagebox.showerror("Error!", "Failed to search")
        else:
            self.cursor.commit()
            self.cursor.close()
            print("Search Successful")
        finally:
            if self.conn.connected == 1:
                self.conn.close()
                print('Connection Closed')

        # ---------------------------------------------------------------------------------------- #


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
