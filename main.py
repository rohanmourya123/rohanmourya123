
print("")
print("-*****  Welcome to ICE_CREAM _PALOR  *****- ")

cone_type = { 1:['Plane_cone',1.5], 2:['Waffle_cone',2],3:['Cup',1]}
scoop_flavour = { 1:['Vanilla',0.5], 2:['Strawberry',0.5],3:['chocolate',0.5],4:['Caramel',0.5], 5:['Rainbow',0.5],6:['Coffe',0.5],
                  7:['Bubble_gum',0.5]}
Topping_chices = { 1:['Peanuts',0.75], 2:['Caramel sauce',0.5],3:['Rainbow-sprinkels',0.5],4:['Pecan',1], 5:['chocolate sprinkles',0.5]}




print(" ")

print("-----********** MENU ***********-----")
print("-----------**Cone-Type **--------")
print("---- Type ------------------ Price ----")
print(" ")
print(" 1) Plain Cone.              Rs 1.5  \n 2) Waffle Cone.             Rs 2 \n 3) Cup.                     Rs 1")

print("")
print("--------------------------------------------")

Names=str(input(" Enter Customer Name = "))
last=input(" Enter last name= ")
# checking for name is valid or no

if not Names.isalpha():
    if not last.isalpha():
        print("Please enter a valid name.")
else:
    n = int(input("Enter How many ICE-CREAM U Want ="))

    cost=0
    for i in range(1,n+1):
        print("For ICE_CREAM ",i)

        print("---- Type ------------------ Price ----")
        print(" ")
        print(" 1) Plain Cone.              Rs 1.5  \n 2) Waffle Cone.             Rs 2 \n 3) Cup.                     Rs 1")

        print("--------------------------------------------")

        price=0;
        l=[]



        while True:
            #l2.append(Total_cost)
            ct= int(input("Enter cone type : "))
            if ct==1:
               p= price + cone_type[1][1]
               cone=cone_type[1][0]
               # l.append(p)
               break
            elif ct==2:
                p=price + cone_type[2][1]
                cone = cone_type[2][0]
                # l.append(p)
                break
            elif ct == 3:
                p=price + cone_type[3][1]
                cone = cone_type[3][0]
               # l.append(p)
                break
            else:
                 print(" Invalid Type!")
                 continue
        print("Price of ",cone ,"is  Rs ",p)
        l.append(p)
        print(l)

        print("")
        print("--------------------------------------------")


        while True:
            scoop = int(input("Enter the Scoop Amount : "))
            if scoop==1 or scoop==2 or scoop == 3 :
                break
            else:
                print("Max 3 scoop are available  ")
                continue
        #print("Price of 1 Qty", , ":","RS",p)
        print("")

        print("---------*** Scoop_Flavours *** ---------- ")
        print("----- Type ------------------Price ------")
        print(" ")
        print(" 1) Vanilla .              Rs 0.5  \n 2) Strawberry.            Rs 0.5 \n 3) Chocolate.             Rs 0.5\n "
              "4) Caramel .              Rs 0.5  \n 5) Rainbow.               Rs 0.5 \n 6) Coffe.                 Rs 0.5\n")

        print("--------------------------------------------")

        while True:
            price2=0
            sf= int(input("Enter  Scoop_Flavours : "))
            if sf==1:
               b= price2 + scoop_flavour[1][1] * scoop
               flavour = scoop_flavour[1][0]
               qty = scoop_flavour[1][1]
              # l.append(p)
               break
            elif sf==2:
                b=price2 + scoop_flavour[2][1] * scoop
                flavour = scoop_flavour[2][0]
                qty = scoop_flavour[2][1]
               # l.append(p)
                break
            elif sf == 3:
                b=price2 + scoop_flavour[3][1] * scoop
                flavour = scoop_flavour[3][0]
                qty = scoop_flavour[3][1]
               # l.append(p)
                break
            elif sf==4:
                b=price2 + scoop_flavour[4][1] * scoop
                flavour = scoop_flavour[4][0]
                qty = scoop_flavour[4][1]
               #l.append(p)
                break
            elif sf == 5:
                b=price2 + scoop_flavour[5][1] * scoop
                flavour = scoop_flavour[5][0]
                qty = scoop_flavour[5][1]
                # l.append(p)
                break
            elif sf== 6:
                b=price2 + scoop_flavour[6][1] * scoop
                flavour = scoop_flavour[6][0]
                qty = scoop_flavour[6][1]
               #l.append(p)
                break
            else:
                 print(" Invalid Type!")
                 continue

        print("Price of 1 Qty of ",flavour," is : Rs ",qty)
        print("Price of ",scoop," Qty  scoop of ",flavour,": ","Rs", b)
        print("")
        l.append(b)

        print(l)

        print("")
        print("--------------------------------------------")

        price1=0


        while True:
            topping = int(input("Enter the Topping Amount : "))
            if topping==1 or topping==2 or topping == 3  or topping == 4:
                break
            else:
                print("Max 3 Topping  are available  ")
                continue
        # print("Price of 1 Qty :",p)
        print("")

        print("----------**** Toppings **** ------------ ")
        print("------ Type ---------------- Price --------")
        print(" ")

        print(
            " 1) Peanuts .              Rs 0.75  \n 2) Caramel sauce.         Rs 0.5 \n 3) Rainbow-sprinkels.     Rs 0.5\n "
            "4) Pecan .                Rs 1  \n 5) chocolate sprinkles.   Rs 0.5 ")

        print("--------------------------------------------")

        while True:

            tc = int(input("Enter topping choice :"))

            if tc == 1:
                c = price1 + Topping_chices[1][1] * topping
                tops = Topping_chices[1][0]
                qty = Topping_chices[1][1]
               # l.append(p)
                break
            elif tc == 2:
                    c = price1 + Topping_chices[2][1] * topping
                    tops = Topping_chices[2][0]
                    qty = Topping_chices[2][1]
                   # l.append(p)
                    break
            elif tc == 3:
                    c = price1 + Topping_chices[3][1] * topping
                    tops = Topping_chices[3][0]
                    qty = Topping_chices[3][1]
                   # l.append(p)
                    break
            elif tc == 4:
                    c = price1 + Topping_chices[4][1] * topping
                    tops = Topping_chices[4][0]
                    qty = Topping_chices[4][1]
                   # l.append(p)
                    break
            elif tc == 5:
                    c = price1 + Topping_chices[4][1] * topping
                    tops = Topping_chices[5][0]
                    qty = Topping_chices[5][1]
                   # l.append(p)
                    break
            else:
                print("invalid choice")
                continue

        print("Price of 1 Qty ", tops,":",qty)
        print("Price of ",topping," Topping of ",tops,":","RS",c)
        print("--------------------------------------------")
        l.append(c)
        print(l)
        tp = sum(l)

        print("Total of ", cone, "+", flavour, "+", tops, ":", "RS", tp)

        cost = p + b + c + cost
        print("")
        print("")
    print("---------------------------------------------")
    print("Name of Customer =",Names + " ",last)

    print("Total cost of ",n ,", ice_cream  is :","RS",cost)
    print("---------------------------------------------")

