import random
import datetime
import encryp

name = []
phone = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i = 0

# Home Function
def Home():

    print("\t\t\t\t\t\t WELCOME TO HOTEL SAITAMA\n")
    print("\t\t\t 1-Booking\n")
    print("\t\t\t 2-Room Service-Menu Card\n")
    print("\t\t\t 3-Payment\n")
    print("\t\t\t 4-Record\n")
    print("\t\t\t 0-Exit\n")

    ch=int(input("->"))

    if ch == 1:
        print(" ")
        Booking()

    elif ch == 2:
        print(" ")
        restaurant()

    elif ch == 3:
        print(" ")
        Payment()

    elif ch == 4:
        print(" ")
        Record()

    else:
        exit()




# Booking fucntion
def Booking():

        # used global keyword to
        # use global variable 'i'
        global i
        print(" BOOKING ROOMS")
        print(" ")

        while 1:
            n = (input("name: "))
            p1 = (input("Phone No.: "))

            # checks if any field is not empty
            if n!="" and p1!="" :#and a!="":
                name.append(n)
                break

            else:
                 print("\nName, Phone no. & Address cannot be empty!")

        cid=str(input("Check_In Date: "))
        checkin.append(cid)
        cid=cid.split('/')
        ci=cid
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)

        cod=str(input("Check_Out Date: "))
        checkout.append(cod)
        cod=cod.split('/')
        co=cod
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])

        # checks if check-out date falls after
        # check-in date
        if co[1]<ci[1] and co[2]<ci[2]:

            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In date\n")
            name.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:

            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass

        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)

        print("----SELECT ROOM TYPE----")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print(("\t\tPress 0 for Room Prices"))

        ch=int(input("->"))

        # if-conditions to display alloted room
        # type and it's price
        if ch==0:
            print(" 1. Standard Non-AC - Rs. 3000")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 5000")
            print(" 4. 3-Bed AC - Rs. 6000")
            ch=int(input("->"))
        if ch==1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")
            price.append(3000)
            print("Price -> 3000")
        elif ch==2:
            room.append('Standard AC')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price -> 4000")
        elif ch==3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(5000)
            print("Price -> 5000")
        elif ch==4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(6000)
            print("Price -> 6000")
        else:
            print(" Wrong choice..!!")


        # randomly generating room no. and customer
        # id for customer
        rn = random.randrange(40)+300
        cusid = random.randrange(40)+10


        # checks if alloted room no. & customer
        # id already not alloted
        while rn in roomno or cid in custid:
            rn = random.randrange(60)+300
            cusid = random.randrange(60)+10

        rc.append(0)
        p.append(0)

        if p1 not in phone:
            phone.append(p1)
        elif p1 in phone:
            for n in range(0,i):
                if p1== phone[n]:
                    if p[n]==1:
                        phone.append(p1)
        elif p1 in phone:
            for n in range(0,i):
                if p1== phone[n]:
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done!")
                        name.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
        print("")
        print("\t\t\t*ROOM BOOKED SUCCESSFULLY*\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cusid)
        roomno.append(rn)
        custid.append(cusid)
        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()

# Function used in booking

def date(c):

    if c[2] >= 2021 and c[2] <= 2022:

        if c[1] != 0 and c[1] <= 12:

            if c[1] == 2 and c[0] != 0 and c[0] <= 31:

                if c[2]%4 == 0 and c[0] <= 29:
                    pass

                elif c[0]<29:
                    pass

                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phone.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()


            # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass

            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass

            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass

            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                pass

            else:
                print("Invalid date\n")
                name.pop(i)
                phone.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()

        else:
            print("Invalid date\n")
            name.pop(i)
            phone.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()

    else:
        print("Invalid date\n")
        name.pop(i)
        phone.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Booking()


# RESTAURANT FUNCTION
def restaurant():
    ph=int(input("Customer Id: "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("-------------------------------------------------------------------------")
            print("                           HOTEL SAITAMA")
            print("-------------------------------------------------------------------------")
            print("                            Menu Card")
            print("-------------------------------------------------------------------------")
            print("\nSIDES                                 DAL____________")
            print("----------------------------------      16 Dal Makhani............ 125.00")
            print(" 1  Regular Tea............. 10.00      17 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 12.00")
            print(" 3  Coffee.................. 15.00      ROTI")
            print(" 4  Cold Drink.............. 25.00     ----------------------------------")
            print(" 5  Bread Butter............ 25.00      18 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 25.00      19 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00      20 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toasted Sandwich... 50.00      21 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00      RICE")
            print("                                       ----------------------------------")
            print(" SOUPS                                  22 Plain Rice.............. 90.00")
            print("----------------------------------      23 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 100.00      24 Veg Pulao.............. 130.00")
            print(" 12 Hot & Sour............. 100.00      25 Peas Pulao............. 135.00")
            print(" 13 Veg. Noodle Soup....... 100.00")
            print(" 14 Sweet Corn............. 100.00")
            print(" 15 Veg. Munchow........... 100.00")
            print("Press 0 -to end ")
            ch=1
            while(ch!=0):

                ch=int(input(" -> "))

                # if-elif-conditions to assign item
                # prices listed in menu card
                if ch==1:
                    rs=10
                    r=r+rs
                elif ch==2:
                    rs=12
                    r=r+rs
                elif ch==3:
                    rs=15
                    r=r+rs
                elif ch<=6 and ch>=4:
                    rs=25
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=15 and ch>=11):
                    rs=100
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=15
                    r=r+rs
                elif (ch==16) :
                    rs=125
                    r=r+rs
                elif ch==17:
                    rs=150
                    r=r+rs
                elif ch==20 or ch==21:
                    rs=20
                    r=r+rs
                elif ch==22 or ch==23:
                    rs=90
                    r=r+rs
                elif ch==24:
                    rs=130
                    r=r+rs
                elif ch==25:
                    rs=135
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)

            # updates restaurant charges and then
            # appends in 'rc' list
            r=r+rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()


# PAYMENT FUNCTION
def Payment():

    ph=str(input("Phone Number: "))
    global i
    f=0

    for n in range(0,i):
        if ph==phone[n] :

            # checks if payment is
            # not already done
             if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")

                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]*day[n])+rc[n])
                print("\n            Pay For HOTEL SAITAMA")
                print("  (y/n)")
                ch=str(input("->"))

                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           HOTEL SAITAMA")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" name: ",name[n],"\t\n Phone No.: ",phone[n])
                    print("\n Check_In Date: ",checkin[n],"\t\n Check_Out Date: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                    print(" Restaurant Charges: \t",rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)

             else:

                for j in range(n+1,i):
                    if ph==phone[j] :
                        if p[j]==0:
                            pass

                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n")
    if f==0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()

# RECORD FUNCTION
def Record():

    # checks if any record exists or not
    if phone!=[]:
        print("        * HOTEL RECORD *\n")
        print("| Name        | Phone No.    | Check_In Date  | Check_Out Date     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")

        for n in range(0,i):
            print("|",name[n]," \t   |",phone[n],"   \t|  ","\t",checkin[n],"\t   |",checkout[n],"\t  |",room[n],"\t  |",price[n])

        print("----------------------------------------------------------------------------------------------------------------------")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()

    else:
        exit()

# Driver Code

Home()