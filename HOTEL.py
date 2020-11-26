import subprocess as sp
import pymysql
import pymysql.cursors

def cd_all():
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM CUSTOMER INNER JOIN (SELECT * FROM CUSTOMER_ADDRESS NATURAL JOIN CUSTOMER_CONTACT) AS T ON CUSTOMER.Customer_id = T.Cust_id" 
                cur.execute(query)
                records = cur.fetchall()
                print("Customers")
                print("\n")
                for row in records:
                    print("Customer_id: ", row['Customer_id'])
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Email: ", row['Email'])
                    print("Contact_number: ", row['C_contact_no'])
                    print("Address: ", row['Cust_address'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def cd_h_id():
    c = input("Enter the hotel id> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM RESERVATION INNER JOIN (SELECT * FROM CUSTOMER INNER JOIN (SELECT * FROM CUSTOMER_ADDRESS NATURAL JOIN CUSTOMER_CONTACT) AS T ON CUSTOMER.Customer_id = T.Cust_id)AS X ON RESERVATION.Cust_id_num=X.Customer_id AND RESERVATION.Hotel_id=%s"
                cur.execute(query,c)
                records = cur.fetchall()
                print("Customers")
                print("\n")
                for row in records:
                    print("Customer_id: ", row['Customer_id'])
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Email: ", row['Email'])
                    print("Contact_number: ", row['C_contact_no'])
                    print("Address: ", row['Cust_address'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def cd_cust_id():
    c = input("Enter the customer id> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM ID_PROOF NATURAL JOIN (SELECT * FROM RESERVATION INNER JOIN (SELECT * FROM CUSTOMER INNER JOIN (SELECT * FROM CUSTOMER_ADDRESS NATURAL JOIN CUSTOMER_CONTACT) AS T ON CUSTOMER.Customer_id = T.Cust_id WHERE CUSTOMER.Customer_id=%s)AS X ON RESERVATION.Cust_id_num=X.Customer_id) AS A" 
                cur.execute(query,c)
                records = cur.fetchall()
                print("Details of", c)
                print("\n")
                for row in records:
                    print("Customer_id: ", row['Customer_id'])
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Email: ", row['Email'])
                    print("Contact_number: ", row['C_contact_no'])
                    print("Address: ", row['Cust_address'])
                    print("Pay_id: ", row['Pay_id'])
                    print("Hotel_id: ", row['Hotel_id'])
                    print("Room_num: ", row['Room_num'])
                    print("Reserve_id: ", row['Reserve_id'])
                    print("Checkin_date: ", row['Checkin_date'])
                    print("Checkout_date: ", row['Checkout_date'])
                    print("Gender: ", row['Gender'])
                    print("ID_Type: ", row['ID_Type'])
                    print("ID_Number: ", row['ID_Number'])
                    print("DOB: ", row['DOB'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def cd_h_id_day():
    h = input("Enter the hotel id> ")
    d = input("Enter the date (format: YYYY-MM-DD)> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM RESERVATION INNER JOIN (SELECT * FROM CUSTOMER INNER JOIN (SELECT * FROM CUSTOMER_ADDRESS NATURAL JOIN CUSTOMER_CONTACT) AS T ON CUSTOMER.Customer_id = T.Cust_id)AS X ON RESERVATION.Cust_id_num=X.Customer_id AND RESERVATION.Hotel_id=%s AND RESERVATION.Checkin_date<=%s AND RESERVATION.Checkout_date>=%s"
                cur.execute(query,(h,d,d))
                records = cur.fetchall()
                print("Customers")
                print("\n")
                for row in records:
                    print("Customer_id: ", row['Customer_id'])
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Email: ", row['Email'])
                    print("Contact_number: ", row['C_contact_no'])
                    print("Address: ", row['Cust_address'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def cd_name():
    c = input("Enter first name or last name> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM ID_PROOF NATURAL JOIN (SELECT * FROM RESERVATION INNER JOIN (SELECT * FROM CUSTOMER INNER JOIN (SELECT * FROM CUSTOMER_ADDRESS NATURAL JOIN CUSTOMER_CONTACT) AS T ON CUSTOMER.Customer_id = T.Cust_id WHERE CUSTOMER.F_name LIKE %s OR CUSTOMER.L_name LIKE %s ) AS X ON RESERVATION.Cust_id_num=X.Customer_id) AS A" 
                cur.execute(query,('%'+c+'%', '%'+c+'%'))
                records = cur.fetchall()
                print("Details related to ", c)
                print("\n")
                for row in records:
                    print("Customer_id: ", row['Customer_id'])
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Email: ", row['Email'])
                    print("Contact_number: ", row['C_contact_no'])
                    print("Address: ", row['Cust_address'])
                    print("Pay_id: ", row['Pay_id'])
                    print("Hotel_id: ", row['Hotel_id'])
                    print("Room_num: ", row['Room_num'])
                    print("Reserve_id: ", row['Reserve_id'])
                    print("Checkin_date: ", row['Checkin_date'])
                    print("Checkout_date: ", row['Checkout_date'])
                    print("Gender: ", row['Gender'])
                    print("ID_Type: ", row['ID_Type'])
                    print("ID_Number: ", row['ID_Number'])
                    print("DOB: ", row['DOB'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def ed_ssn():
    h = input("Enter the SSN of the employee> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT *  FROM EMPLOYEE INNER JOIN EMPLOYEE_CONTACT WHERE EMPLOYEE.Ssn=%s AND EMPLOYEE.Ssn=EMPLOYEE_CONTACT.Emp_Ssn"
                cur.execute(query,h)
                records = cur.fetchall()
                for row in records:
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Ssn: ", row['Ssn'])
                    print("Dept_no: ", row['Dept_no'])
                    print("Salary: ", row['Salary'])
                    print("Contact_no: ", row['E_contact_no'])
                    if row['Dept_no'][-1]=='1':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN HOUSEKEEPING WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Room_served: ", row1['Room_served'])
                    elif row['Dept_no'][-1]=='2':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN WAITER WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Hours_of_working: ", row1['Hours_of_working'])
                    elif row['Dept_no'][-1]=='3':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN RECEPTIONIST WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Qualification: ", row1['Qualification'])
                            print("Hours: ", row1['Hours'])
                    elif row['Dept_no'][-1]=='4':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN MANAGER WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Number_of_people_managing: ", row1['Number_of_people_managing'])
                    elif row['Dept_no'][-1]=='5':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN CHEF WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Expertise: ", row1['Expertise'])
                            print("Super_ssn: ", row1['Super_ssn'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def ed_name():
    h = input("Enter the name of the employee (partial entries allowed)> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT *  FROM EMPLOYEE INNER JOIN EMPLOYEE_CONTACT WHERE (EMPLOYEE.F_name LIKE %s OR EMPLOYEE.L_NAME LIKE %s) AND EMPLOYEE.Ssn=EMPLOYEE_CONTACT.Emp_Ssn"
                cur.execute(query,('%'+h+'%', '%'+h+'%'))
                records = cur.fetchall()
                for row in records:
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Ssn: ", row['Ssn'])
                    print("Dept_no: ", row['Dept_no'])
                    print("Salary: ", row['Salary'])
                    print("Contact_no: ", row['E_contact_no'])
                    if row['Dept_no'][-1]=='1':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN HOUSEKEEPING WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Room_served: ", row1['Room_served'])
                    elif row['Dept_no'][-1]=='2':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN WAITER WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Hours_of_working: ", row1['Hours_of_working'])
                    elif row['Dept_no'][-1]=='3':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN RECEPTIONIST WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Qualification: ", row1['Qualification'])
                            print("Hours: ", row1['Hours'])
                    elif row['Dept_no'][-1]=='4':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN MANAGER WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Number_of_people_managing: ", row1['Number_of_people_managing'])
                    elif row['Dept_no'][-1]=='5':
                        q = "SELECT *  FROM EMPLOYEE NATURAL JOIN CHEF WHERE EMPLOYEE.Ssn=%s"
                        cur.execute(q,h)
                        record1 = cur.fetchall()
                        for row1 in record1:
                            print("Expertise: ", row1['Expertise'])
                            print("Super_ssn: ", row1['Super_ssn'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def ed_h_id_d_no():
    h = input("Enter the department id> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT *  FROM EMPLOYEE WHERE EMPLOYEE.Dept_no=%s"
                cur.execute(query,h)
                records = cur.fetchall()
                for row in records:
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("Ssn: ", row['Ssn'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def customer_details():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. Show customer details using Customer name or surname (partial entries allowed)")
            print("2. Show customer details using Customer_id")
            print("3. Show list of customer ids staying in a hotel on a particular day")
            print("4. Show customer ids of all the customers in a hotel")
            print("5. Show customer details of all the customers in all the hotels")
            print("6. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                cd_name()
            elif ch==2:
                cd_cust_id()
                return
            elif ch==3:
                cd_h_id_day()
                return
            elif ch==4:
                cd_h_id()
                return
            elif ch==5:
                cd_all()
                return
            elif ch==6:
                return
            else:
                print("Invalid entry")
                tmp=input("Enter any key to CONTINUE> ")

def employee_details():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. Show employee details using name(partial entries allowed)")
            print("2. Show employee details using Ssn")
            print("3. Show employees working in a department")
            print("4. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                ed_name()
            elif ch==2:
                ed_ssn()
                return
            elif ch==3:
                ed_h_id_d_no()
                return
            elif ch==4:
                return
            else:
                print("Invalid entry")
                tmp=input("Enter any key to CONTINUE> ")

def insert_emp():
    try:
        row={}
        print("Enter new employee details: ")
        row["Dept_no"] = (input("Dept_no: "))
        row["Ssn"] = input("SSN: ")
        name = (input("Name (F_name L_name): ")).split(' ')
        row["F_name"] = name[0]
        row["L_name"] = name[1]
        row["Salary"] = int(input("Salary: "))
        query = "INSERT INTO EMPLOYEE(Dept_no, Ssn, F_name, L_name,  Salary) VALUES('%s', '%s', '%s', '%s', '%d')" % (row["Dept_no"], row["Ssn"], row["F_name"], row["L_name"], row["Salary"])
        print(query)
        cur.execute(query)
        con.commit()
        
        row5={}
        row5["E_Contact_no"] = input("Contact_number: ")
        query5 = "INSERT INTO EMPLOYEE_CONTACT(Emp_Ssn, E_contact_no) VALUES ('%s', '%s')" % (row["Ssn"], row5["E_Contact_no"])
        print(query5)
        cur.execute(query5)
        con.commit()
        
        if row['Dept_no'][-1]=='1':
        	row["room"] = input("Enter the room served> ")
        	q = "INSERT INTO HOUSEKEEPING(Ssn, Room_served) VALUES('%s', '%s')" % (row["Ssn"], row["room"])
        	print(row["room"])
        	print(q)
        	input("Enter any key to CONTINUE> ")
        	cur.execute(q)
        	con.commit()
        elif row['Dept_no'][-1]=='2':
        	x = int(input("Enter Hours_of_working> "))
        	q = "INSERT INTO WAITER(Ssn, Hours_of_working) VALUES ('%s', '%d')" % (row["Ssn"], x)
        	cur.execute(q)
        	con.commit()
        elif row['Dept_no'][-1]=='3':
        	x = int(input("Enter Hours> "))
        	y = input("Qualification> ")
        	q = "INSERT INTO RECEPTIONIST(Ssn, Qualification, Hours) VALUES ('%s', '%s', '%d')" % (row["Ssn"], y, x)
        	cur.execute(q)
        	con.commit()
        elif row['Dept_no'][-1]=='4':
        	x = int(input("Number_of_people_managing> "))
        	q = "INSERT INTO MANAGER(Ssn, Number_of_people_managing) VALUES ('%s', '%d')" % (row["Ssn"], x)
        	cur.execute(q)
        	con.commit()
        elif row['Dept_no'][-1]=='5':
        	x = input("Expertise> ")
        	y = input("Super_ssn> ")
        	q = "INSERT INTO CHEF(Ssn, Expertise, Super_ssn) VALUES ('%s', '%s', '%s')" % (row["Ssn"], x, y)
        	cur.execute(q)
        	con.commit()
        print("Inserted Into Database")
        input("Enter any key to CONTINUE> ")
        return
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return

def available_rooms():
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM ROOM WHERE Is_available = 1"
                cur.execute(query)
                records = cur.fetchall()
                print("Available Rooms")
                print("\n")
                for row in records:
                    print("H_id: ", row['H_id'])
                    print("Room_number: ", row['Room_number'])
                    print("Room_category: ", row['Room_category'])
                    print("Cost: ", row['Cost'])
                    print("Number_of_people_staying: ", row['Number_of_people_staying'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def insert_cust():

	while(1):
		try:
				
			row = {}
			print("Enter the details of the Customer: ")
			row["Customer_id"] = (input("Customer_id: "))
			row["Email"] = input("Email: ")
			name = (input("Name (F_name L_name): ")).split(' ')
			row["F_name"] = name[0]
			row["L_name"] = name[1]
			query = "INSERT INTO CUSTOMER(Customer_id, Email, F_name, L_name) VALUES (%s, %s, %s, %s)"
			print(query, (row["Customer_id"], row["Email"], row["F_name"], row["L_name"]))
			cur.execute(query, (row["Customer_id"], row["Email"], row["F_name"], row["L_name"]))
			con.commit()
				
			row5={}
			row5["Contact_number"] = input("Contact_number: ")
			query5 = "INSERT INTO CUSTOMER_CONTACT(Cust_id, C_contact_no) VALUES ('%s', '%s')" % (row["Customer_id"],row5["Contact_number"])
			print(query5)
			cur.execute(query5)
			con.commit()

            # row6={}
            # row6["Address"] = input("Address: ")
            # query6 = "INSERT INTO CUSTOMER_ADDRESS(Cust_id, Cust_address) VALUES ('%s', '%s')" % (row["Customer_id"],row5["Address"])
            # print(query6)
            # cur.execute(query6)
            # con.commit()

			row1 = {}
			print("Enter Payment details: ")
			row1["Payment_id"] = (input("Payment_id: "))
			row1["Amount"] = int(input("Amount: "))
			row1["Payment_mode"] = input("Payment_mode: ")
			row1["Date"] = input("Enter the date (format: YYYY-MM-DD)> ")
			query1 = "INSERT INTO PAYMENT (Payment_id, Amount, Payment_mode, Date) VALUES ('%s', '%d', '%s', '%s')" % (row1["Payment_id"], row1["Amount"], row1["Payment_mode"], row1["Date"])
			print(query1)
			cur.execute(query1)
			con.commit()
			
			row2={}
			print("Enter ID_PROOF details: ")
			row2["Gender"] = input("Gender (M/F): ")
			row2["ID_Type"] = input("ID_Type (Aadhar/Passport/PAN): ")
			row2["ID_Number"] = input("ID_Number: ")
			row2["DOB"] = input("Enter the date of birth (format: YYYY-MM-DD)> ")
			query2 = "INSERT INTO ID_PROOF(Gender, ID_Type, ID_Number, DOB, Cust_id) VALUES('%c', '%s', '%s', '%s', '%s')" % (row2["Gender"], row2["ID_Type"], row2["ID_Number"], row2["DOB"], row["Customer_id"])
			cur.execute(query2)
			con.commit()
			available_rooms()
			row3={}
			print("Enter Room details: ")
			row3["Room_num"] = input("Room_number: ")
			row3["Reserve_id"] = input("Reservation ID: ")
			row3["Checkin_date"] = input("Checkin_date(YYYY-MM-DD): ")
			row3["Checkout_date"] = input("Checkout_date(YYYY-MM-DD): ")
			row3["Hotel_id"] = int(input("Hotel_id: "))
			query3 = "INSERT INTO RESERVATION(Pay_id, Hotel_id, Room_num, Cust_id_num, Reserve_id, Checkin_date, Checkout_date) VALUES('%s', '%d', '%s', '%s', '%s', '%s', '%s')" % (row1["Payment_id"], row3["Hotel_id"], row3["Room_num"], row["Customer_id"], row3["Reserve_id"], row3["Checkin_date"], row3["Checkout_date"])
			print(query3)
			cur.execute(query3)
			con.commit()
			query4 = "UPDATE ROOM SET Is_available=0 WHERE Room_number = '%s'" % (row3["Room_num"])
			print(query4)
			cur.execute(query4)
			con.commit()
			input("Enter any key to CONTINUE> ")
			break
		except Exception as e:
			con.rollback()
			print("Failed to insert into database")
			print(">>>>>>>>>>>>>", e)
			return


def menu():
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM FOOD_ITEM2"
                cur.execute(query)
                records = cur.fetchall()
                print("Menu")
                print("\n")
                for row in records:
                    print("Id: ", row['Item_num'])
                    print("Item_name: ", row['Item_name'])
                    print("Price: ", row['Price'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def menu_name():
    h = input("Enter the name of food item (partial entries allowed)> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM FOOD_ITEM2 WHERE Item_name LIKE %s"
                cur.execute(query, '%'+h+'%')
                records = cur.fetchall()
                print("Available food items matching your search")
                print("\n")
                for row in records:
                    print("Id: ", row['Item_num'])
                    print("Item_name: ", row['Item_name'])
                    print("Price: ", row['Price'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def avg_monthly_sales():
    h = input("Enter the month(1-12)> ")
    y = input("Enter the year> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT AVG(Amount) AS 'Average monthly sales' FROM PAYMENT WHERE EXTRACT(MONTH FROM PAYMENT.Date) = %s AND EXTRACT(YEAR FROM PAYMENT.Date) = %s"
                cur.execute(query, (h, y))
                records = cur.fetchall()
                print(records)
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def avg_yearly_sales():
    y = input("Enter the year> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT AVG(Amount) AS 'Average yearly sales' FROM PAYMENT WHERE EXTRACT(YEAR FROM PAYMENT.Date) = %s"
                cur.execute(query, y)
                records = cur.fetchall()
                print(records)
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break    

def cust_amt():
    h = input("Enter the amount> ")
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)
                query = "SELECT * FROM PAYMENT INNER JOIN (SELECT * FROM CUSTOMER INNER JOIN RESERVATION WHERE CUSTOMER.Customer_id=RESERVATION.Cust_id_num)AS A WHERE A.Pay_id=PAYMENT.Payment_id AND PAYMENT.Amount >= %s"
                cur.execute(query, h)
                records = cur.fetchall()
                for row in records:
                    print("F_name: ", row['F_name'])
                    print("L_name: ", row['L_name'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def food_max_min():
    while(1):
        try:
            k = input("Enter any key to CONTINUE> ")
            with con.cursor() as cur:
                tmp=sp.call('clear',shell=True)

                query = "SELECT MIN(Item_name) AS min_ordered FROM FOOD_ITEM2 INNER JOIN FOOD_ITEM1 ON FOOD_ITEM1.Item_no=FOOD_ITEM2.Item_num"
                cur.execute(query)
                records = cur.fetchall()
                for row in records:
                    print("Min ordered item: ", row['min_ordered'])
                    print("\n")
                query = "SELECT MAX(Item_name) AS max_ordered FROM FOOD_ITEM2 INNER JOIN FOOD_ITEM1 WHERE FOOD_ITEM1.Item_no=FOOD_ITEM2.Item_num"
                cur.execute(query)
                records = cur.fetchall()
                for row in records:
                    print("Max ordered item: ", row['max_ordered'])
                    print("\n")
        except Exception as e:
            con.rollback()
            print(">>>>>>>>>>>>>", e)

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def order_food():
	cust_id = input("Enter your customer ID> ")
	item_no = int(input("Enter food item number> "))

	q = "INSERT INTO FOOD_ITEM1(Item_no, Cust_id) VALUES ('%d', '%s')" % (item_no, cust_id)
	cur.execute(q)
	con.commit()

def retrieve():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. Show all the available rooms")
            print("2. Customer details")
            print("3. Employee details")
            print("4. Average monthly sales")
            print("5. Average yearly sales")
            print("6. Menu")
            print("7. Search food items")
            print("8. Number of customers with payment greater than a specified amount")
            print("9. Item least ordered and item most ordered")
            print("10. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                available_rooms()
                return
            elif ch==2:
                customer_details()
                return
            elif ch==3:
                employee_details()
                return
            elif ch==4:
                avg_monthly_sales()
                return
            elif ch==5:
                avg_yearly_sales()
                return
            elif ch==6:
                menu()
                return
            elif ch==7:
                menu_name()
                return
            elif ch==8:
                cust_amt()
                return
            elif ch==9:
                food_max_min()
                return
            elif ch==10:
                return

def insert():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear', shell=True)
            print("1. Hire an Employee")
            print("2. Register a Customer")
            print("3. Order food item")
            print("4. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==1:
                insert_emp()
            elif ch==2:
                insert_cust()
            elif ch==3:
            	order_food()
            elif ch==4:
                return

def update_emp():
    while(1):
        try:
            row={}
            print("Update employee details: ")
            row["Dept_no"] = (input("Dept_no: "))
            row["Ssn"] = input("SSN: ")
            name = (input("Name (F_name L_name): ")).split(' ')
            row["F_name"] = name[0]
            row["L_name"] = name[1]
            row["Salary"] = int(input("Salary: "))
            query = "UPDATE EMPLOYEE SET Dept_no='%s', F_name='%s', L_name='%s', Salary='%d' where Ssn='%s'" % (row["Dept_no"], row["F_name"], row["L_name"], row["Salary"], row["Ssn"])
            print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def update_hotel():
    while(1):
        try:
            row={}
            print("Update hotel details: ")
            row["Hotel_id"] = int(input("Hotel_id: "))
            row["Hotel_name"] = input("Hotel_name: ")
            row["Hotel_contact_number"] = input("Hotel_contact_number: ")
            row["Ratings"] = int(input("Ratings: "))
            query = "UPDATE HOTEL SET Hotel_name='%s', Hotel_contact_number='%s', Ratings='%d' where Hotel_id='%d'" % (row["Hotel_name"], row["Hotel_contact_number"], row["Ratings"], row["Hotel_id"])
            print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def update_department():
    while(1):
        try:
            row={}
            print("Update department details: ")
            row["Department_number"] = (input("Department_number: "))
            row["Department_name"] = (input("Department_name: "))
            row["Department_contact_number"] = (input("Department_contact_number: "))
            query = "UPDATE DEPARTMENT SET Department_name='%s', Department_contact_number='%s' where Department_number='%s'" % (row["Department_name"], row["Department_contact_number"], row["Department_number"])
            print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break


def update():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear', shell=True)
            print("1. Change details of Employee")
            print("2. Change details of Hotel")
            print("3. Change details of Department")
            print("4. Return back to previous menu")
            ch=int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==1:
                update_emp()
            elif ch==2:
                update_hotel()
            elif ch==3:
                update_department()
            elif ch==4:
                return
    
def delete_emp():
    while(1):
        try:
            row={}
            print("employee Ssn to delete: ")
            row["Ssn"] = input("SSN: ")
            query ="DELETE FROM EMPLOYEE where Ssn='%s'" % (row["Ssn"])
            print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def delete_reservation():
    while(1):
        try:
            row={}
            print("Customer ID to delete: ")
            row["Customer_id"] = input("Customer_id: ")
            query ="DELETE FROM CUSTOMER where Customer_id='%s'" % (row["Customer_id"])
            print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break

def delete():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear', shell=True)
            print("1. Delete Employee")
            print("2. Delete Reservation")
            print("3. Return to the previous menu")
            ch=int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==1:
                delete_emp()
            elif ch==2:
                delete_reservation()
            elif ch==3:
                return

def dispatch(ch):
    if(ch==1):
        insert()
    elif(ch==2):
        update()
    elif(ch==3):
        delete()
    elif(ch==4):
        retrieve()
    else:
        print("Error: Invalid option")


while(1):
    username = input("Enter username:")
    password = input("Enter password: ")
    
    tmp = sp.call('clear', shell=True)
    try:
        con = pymysql.connect(host='localhost',user=username,password=password,db='HOTEL_RESORT',cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)
        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE> ")
        with con.cursor() as cur:
            while(1):
                tmp=sp.call('clear',shell=True)
                print("1. Insert data")
                print("2. Update data")
                print("3. Delete data")
                print("4. Retrieve data")
                print("5. Logout")
                print("6. Exit")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch==5:
                    break
                if ch==6:
                    exit(0)
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE> ")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE> ")
