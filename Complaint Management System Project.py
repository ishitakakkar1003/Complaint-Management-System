######################### DATA BASE CREATION ##########################

import mysql.connector as sql
conn=sql.connect(host='localhost',password='root',user='root') 
cur=conn.cursor()

## DATABASE CREATED ##
cur.execute('create database Complaint_Management_System')
print("Database created")
cur.execute('show databases')
for x in cur:
             print(x)

             
########################### TABLES #####################################           

import mysql.connector as sql
conn=sql.connect(host='localhost',password='root',user='root',database='Complaint_Management_System') 
cur=conn.cursor()

## CREATE COMPLAINTS TABLE ##
cur.execute('create table complaints_RWA(Complaint_No int(5) primary key,House_No int(5),\
                                        Floor int(3),Phone_No bigint(20),\
                                        Name_of_Complainant varchar(30),\
                                        Complaint_Description varchar(200),\
                                        Date_of_Lodging_Complaint varchar(10))') 
print("Complaint table created!")


## CREATE STATUS TABLE ##
cur.execute('create table complaint_status(Complaint_No int(5) references complaints_rwa(Complaint_No),\
                                            Action_Taken varchar(200) DEFAULT "No Action Taken",\
                                            Complaint_Resolved varchar(3) DEFAULT "No")')
print("Complaint Status table created!")


############################ MAIN #####################################

print('=============WELCOME TO RWA MANAGEMENT SYSTEM=============')
print()
ch='y'
while ch=='y':
    ans=input(("Are you an admin or a user?\nadmin/user:"))
    if ans=='admin':
        conn.autocommit = True                      
        user=input('Admin Id:')
        passw=input('Password:')
        if user=='admin' and passw=='ishitakeyyshav':
            print()
            print("Welcome to the admin interface of The RWA Complaint Management System.")
            print("Admins have access to the entire database and can monitor data")
            print("through the following features:")
            while True:
                print()
                print('1.ADD NEW COMPLAINT')                                                                 
                print('2.DELETE COMPLAINT')                          
                print('3.VIEW COMPLAINT DETAILS')
                print('4.UPDATE COMPLAINT STATUS')
                print('5.VIEW COMPLAINT STATUS')
                print('6.QUIT')
                print()
                n=int(input('Enter your choice\n(1/2/3/4/5/6):'))
                print()

                if n == 1:
                    print("ADD NEW COMPLAINT")
                    print()
                    c_no=int(input('Complaint Number:'))
                    no=int(input('House No.:'))
                    floor=input('Floor No.(1/2/3...):')           
                    ph_no=int(input('Phone Number:'))
                    name=input('Name of Complainant:')
                    desc=input('Description:')
                    date=input('Date(DD-MM-YY):')
                    Action_Taken='No Action Taken'
                    Complaint_Resolved='No'
                    V_SQLInsert="INSERT  INTO complaints_RWA values ("+ str(c_no) +"," +  str(no) + ",\
                                                                     " + str(floor) + ","+str(ph_no) + ",\
                                                                     ' " + name + " ',' "+ desc + " ',\
                                                                     ' "+ date +" ' ) "
                    cur.execute(V_SQLInsert)
                    W_SQLInsert="INSERT INTO complaint_status values ("+ str(c_no) +",' " + Action_Taken + " ',\
                                                                      ' " + Complaint_Resolved + " ' )"
                    cur.execute(W_SQLInsert)
                    print()
                    print('COMPLAINT LODGED SUCCESFULLY!')
                    conn.commit()

                if n == 2:
                    print('DELETE COMPLAINT')
                    print()
                    Complaint_no=int(input('Complaint_No.:'))
                    cur.execute('delete from Complaints_rwa where complaint_no='+str(Complaint_no) )
                    print('COMPLAINT DELETED SUCCESFULLY!')

                if n == 3:
                    print("1. VIEW ALL COMPLAINTS")
                    print("2. VIEW A SPECIFIC COMPLAINT")
                    print()
                    a=int(input("select your choice:"))
                    if a==1:
                        print("Following data is in the order:(Complaint No.,H.No.,Fl.No.,Ph.No.,Name,Description,Date)")
                        cur.execute('select * from complaints_rwa' )
                        record=cur.fetchall()
                        if record==0:
                            print('No Data Exists')
                        else:
                            for x in record:
                               print(x)
                    if a==2:
                        c_number=int(input("Enter complaint number:"))
                        print("Following data is in the order:(Complaint No.,H.No.,Fl.No.,Ph.No.,Name,Description,Date)")
                        cur.execute('select * from complaints_rwa where Complaint_No='+str(c_number)+'' )
                        record=cur.fetchall()
                        if record==0:
                            print('No Data Exists')
                        else:
                            for x in record:
                               print(x)
    
                if n==4:                                                         
                    c_number=int(input('Complaint Number:'))
                    print()
                    action=input('Action Status:')
                    print()
                    resolve=input('Complaint Resolved:')
                    print()
                    sql = "UPDATE Complaint_status SET action_taken= %s WHERE Complaint_No = %s"
                    val = (str(action), str(c_number))
                    cur.execute(sql, val)
                    sql = "UPDATE Complaint_status SET complaint_resolved= %s WHERE Complaint_No = %s"
                    val = (str(resolve), str(c_number))
                    cur.execute(sql, val)
                    print()
                    print('COMPLAINT STATUS UPDATED SUCCESFULLY')
                    conn.commit()

                if n == 5:
                    print("1. VIEW ALL COMPLAINTS")
                    print("2. VIEW A SPECIFIC COMPLAINT")
                    print()
                    a=int(input("select your choice:"))
                    if a==1:
                        cur.execute('select * from complaint_status' )
                        record=cur.fetchall()
                        if record==0:
                            print('No Data Exists')
                        else:
                            for x in record:
                               print(x)
                    if a==2:
                        c_number=int(input("Enter complaint number:"))
                        cur.execute('select * from complaint_status where Complaint_No='+str(c_number)+'' )
                        record=cur.fetchall()
                        if record==0:
                            print('No Data Exists')
                        else:
                            for x in record:
                               print(x)
                    
                if n==6:
                    break

                if n>6:
                    print("Invalid Choice")
                    continue 

                if n<1:
                    print("Invalid choice")
                    continue 

        if user!='admin' or passw!='ishitakeyyshav':
            print("Incorrect Password or Admin Id")

    if ans=='user':
        print()
        print("Welcome to the user interface of The RWA Complaint Management System.")
        print("We, at the RWA, apologise for any inconvinience caused. Feel free to")
        print("lodge your complaints or view your complaint status or complaint details.")
        conn.autocommit = True                      
        while True:
            print()
            print('1.ADD NEW COMPLAINT')                                                                
            print('2.VIEW COMPLAINT DETAILS')
            print('3.VIEW COMPLAINT STATUS')
            print('4.QUIT') 
            print()
            n=int(input('Enter your choice\n(1/2/3/4):'))
            print()

            if n == 1:
                print("ADD NEW COMPLAINT")
                print()
                c_no=int(input('Complaint Number:'))
                no=int(input('House No.:'))
                floor=input('Floor No.(1/2/3...):')
                ph_no=int(input('Phone Number:'))
                name=input('Name of Complainant:')
                desc=input('Description:')
                date=input('Date(DD-MM-YY):')
                Action_Taken='No Action Taken'
                Complaint_Resolved='No'
                V_SQLInsert="INSERT  INTO complaints_RWA values ("+ str(c_no) +"," +  str(no) + ",\
                                                                 " + str(floor) + ","+str(ph_no) + ",\
                                                                 ' " + name + " ',' "+ desc + " ',\
                                                                 ' "+ date +" ' ) "
                cur.execute(V_SQLInsert)
                W_SQLInsert="INSERT INTO complaint_status values ("+ str(c_no) +",' " + Action_Taken + " ',\
                                                                  ' " + Complaint_Resolved + " ' )"
                cur.execute(W_SQLInsert)
                print()
                print('COMPLAINT LODGED SUCCESFULLY')
                conn.commit()

            if n == 2:
                print("VIEW COMPLAINT DETAILS")
                print()
                c_number=int(input("Enter complaint number:"))
                print("Following data is in the order:(Complaint No.,H.No.,Fl.No.,Ph.No.,Name,Description,Date)")
                cur.execute('select * from complaints_rwa where Complaint_No='+str(c_number)+'' )
                record=cur.fetchall()
                if record==0:
                    print('No Data Exists')
                else:
                    for x in record:
                       print(x)
                       
                
            if n == 3:
                print("VIEW COMPLAINT STATUS")
                print()
                c_number=int(input("Enter complaint number:"))
                cur.execute('select * from complaint_status where Complaint_No='+str(c_number)+'' ) 
                record=cur.fetchall()
                if record==0:
                    print('No Data Exists')
                else:
                    for x in record:
                       print(x)

                 
            if n==4:
                break

            if n>4:
                print("Invalid choice")
                continue

            if n<1:
                print("Invalid choice")
                continue

        
    ch=input("Do you want to continue?\ny/n:")

print("Thank you for your time!")

