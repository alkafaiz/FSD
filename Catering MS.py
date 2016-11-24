#APU Catering Management System v.1.3
#11/21/16
#@Faiz Alkautsar

order = {'breakfast': 0, 'launch': 0, 'tent': 0,'chairs':0,'tables': 0,'tableCloths': 0}
cart = [ ]
paid = "No"

#MENU PRICE ORDERED
bf_price = 0
bf_priceDisc = 0
ln_price = 0
ln_priceDisc = 0
tent_price = 0
chs_price = 0
tab_price = 0
tbcl_price = 0
amountDisc = 0
amountPayment = 0

name = input("Enter customer name : ")
userfile = name+".txt"
print("Welcome, ",name,"!")
while True :
    print("===================================\nAPU Catering Management System v.1.3\n===================================")
    user = input("O - Order \nR - Report \nP - Payment \nE - Exit\ntype(O/R/P/E): ")
    if user == "O" :                #ORDER MENU
        print("==========\nORDER MODULE\n==========")
        user = input("F - Place orders for food \nS - Place orders for other services \nM - Return to Main Menu\ntype: ")
        #THIS SCRIPT CONTAINS HOW TO STORE THE ORDER
    
        if user == "F" :
            user = input("B - Breakfast \nL - Lunch \nO - Main Menu\ntype :")
            if user == "B" :    #Breakfast
                print("========\nBREAKFAST\n========")
                print("Nasi lemak\nFried noodles\nRoti Chanai\nPasta\nHot Drink\nRM 20.00/guest")
                user = input("1 - Order\n2 - Main Menu\ntype : ")
                if user =="1" :
                    bfOrder = int(input("For how many guest would you order? "))
                    order['breakfast'] += bfOrder
                    cart.append('breakfast')
                    print("order accepted")
                elif user =="2" :
                    continue
            elif user == "L" :  #Launch
                print("========\nLAUNCH\n========")
                print("Chicken Chop\nSteamed Fish\nSalad\nFried rice\nSoft Drink\nRM 30.00/guest")
                user = input("1 - Order\n2 - Main Menu\ntype : ")
                if user == "1" :
                    lnOrder = int(input("For how many guest would you order? "))
                    order['launch'] += lnOrder
                    cart.append('launch')
                    print("order accepted")
                elif user == "2" :
                    continue
            elif user == "O" :
                continue
        elif user == "S" :
            user = input("1 - Tent\n2 - Chairs\n3 - Tables\n4 - Table cloths\ntype :")
            if user == "1" : #tent
                print ("RM 400 per unit of 10 by 10 ft")
                user = input("1 - order\n2 - Main Menu\ntype : ")
                if user == "1" :
                    tentOrder = int(input("How many tent you want to order : "))
                    order['tent'] += tentOrder
                    cart.append('tent')
                    print("order accepted")
                elif user =="2" :
                    continue
                else :
                    print("invalid entry")
                    continue
            elif user == "2" :  #chairs
                print("RM 100 for 50 chairs")
                user = input("1 - order\n2 - Main Menu\ntype : ")
                if user == "1" :
                    while True :
                        chairsOrder = int(input("How many chair you want to order(enter multiplied by50): "))
                        if chairsOrder%50 == 0 :
                            order['chairs'] += chairsOrder
                            break
                        else :
                            print("please insert multiplied by 50")
                            continue
                    cart.append('chairs')
                    print("Order accepted. Thankyou")
                elif user == "2" :
                    continue
                else :
                    print("invalid entry")
                    continue
            elif user == "3" :  #tables
                print("RM80 for 10 tables")
                user = input("1 - order\n2 - Main Menu\ntype : ")
                if user == "1" :
                    while True :
                        tablesOrder = int(input("How many tables you want to order(enter multiplied by 10) : "))
                        if tablesOrder%10 == 0 :
                            order['tables'] += tablesOrder
                            break
                        else :
                            print("please insert number multiplication of 10")
                            continue
                    cart.append('tables')
                    print("order accepted")
                        
                elif user == "2" :
                    continue
                else :
                    print("invalid entry")
                    continue

            elif user == "4" :  #table cloths
                print("RM20 for 10 table clothes")
                user = input("1 - order\n2 - Main Menu\ntype : ")
                if user == "1" :
                    while True :
                        tableClothsOrder = int(input("How many table cloths you want to order(enter multiplied by 10) : "))
                        if tableClothsOrder%10 == 0 :
                            order['tableCloths'] += tableClothsOrder
                            break
                        else :
                            print("please insert number multiplication of 10")
                            continue
                    cart.append('tableCloths')
                    print("order accepted")
                        
                elif user == "2" :
                    continue
                else :
                    print("invalid entry")
                    continue
              
            else :
                print("invalid entry")
                continue
        elif user == "M" :
            continue
        else :
            print("invalid entry")
            continue

        #update price
        bf = int(order['breakfast'])
        ln = int(order['launch'])
        tent = int(order['tent'])
        chs = int(order['chairs'])
        tab = int(order['tables'])
        tbcl = int(order['tableCloths'])
        #Food Price, calculate discount
        if bf > 0 :
            bf_price = bf * 20
            if bf in range(1,10) :
                bf_priceDisc *= 0
            if 10<= bf <= 25 :
                bf_priceDisc = bf * 20 * 5/100
            if 26 <= bf <= 50 :
                bf_priceDisc = bf * 20 * 10/100
            if 51 <= bf <= 100 :
                bf_priceDisc = bf * 20 * 15/100
            if 100 < bf :
                bf_priceDisc = bf * 20 * 20/100
            
        if ln > 0 :
            ln_price = ln * 30
            if 0 < ln <= 9 :
                ln_priceDisc = 0
            if 10<= ln <= 25 :
                ln_priceDisc = ln * 30 * 5/100
            if 26 <= ln <= 50 :
                ln_priceDisc = ln * 30 * 10/100
            if 51 <= ln <= 100 :
                ln_priceDisc = ln * 30 * 15/100
            if 100 < ln :
                ln_priceDisc = ln * 30 * 20/100

        #NO discount for additional request
        if tent > 0 :
            tent_price = tent * 400
        if chs > 0 :
            chs = chs/50
            chs_price = chs * 100
        if tab > 0 :
            tab = tab/10
            tab_price = tab * 80
        if tbcl > 0 :
            tbcl = tbcl/10
            tbcl_price = tbcl * 20
        amountDisc = bf_priceDisc + ln_priceDisc
        amountPayment = (bf_price-bf_priceDisc)+(ln_price-ln_priceDisc)+tent_price+chs_price+tab_price+tbcl_price
        

        
    
    elif user == "P" : #Payment Module
        print("==========\nPAYMENT MODULE\n==========")
        user = input("T - Display total amount to be paid\nP - Make payment\nM - Return to Main Menu\ntype :")
        if user == "T" :
            print("Total amount to be paid\t: RM ",str(amountPayment))
        elif user == "P" :
            print("Total amount to be paid\t: RM ", (amountPayment))
            pay = input("Make Payment?\n1 - Yes\n2 - No\ntype : ")
            if pay == "1" :
                paid = "Yes"
                while amountPayment != 0 :
                    break
                if amountPayment == 0 :
                    print("you haven't made the order")
                    continue
                    
                #Writing an output file
                
                phone = input("Enter phone number : ")
                adress = input("Enter adress : ")
                
                file = open(userfile,"w+")
                file.write("==============================\nAPU Catering Management System\n==============================\n")
                file.write("\nCUSTOMER DETAIL\nName\t\t: "+name+"\n")
                file.write("Phone\t\t: "+phone+"\nAdress\t\t: "+adress+"\n")
                file.write("\nSUMMARY OF THE ORDERS\n")
                file.write("ITEM(s)\t\tQTY\t PRICE\n")

                if 'breakfast' in cart:
                    file.write("Breakfast\t"+str(bf)+"\t RM "+str(float(bf_price))+"\n")
                if 'launch' in cart :
                    file.write("Launch\t\t"+str(ln)+"\t RM "+str(float(ln_price))+"\n")
                if 'tent' in cart :
                    file.write("Tent\t\t"+str(tent)+"\t RM "+str(float(tent_price))+"\n")
                if 'chairs' in cart :
                    file.write("Chairs\t\t"+str(chs)+"\t RM "+str(float(chs_price))+"\n")
                if 'tables' in cart :
                    file.write("Table\t\t"+str(tab)+"\t RM "+str(float(tab_price))+"\n")
                if 'tableCloths' in cart :
                    file.write("Table Cloths\t"+str(tbcl)+"\t RM "+str(float(tbcl_price))+"\n")

                subtotal = amountPayment+amountDisc
                file.write("\nSUBTOTAL\tRM "+ str(float(subtotal))+"\n==========================\n")
                file.write("Discount\tRM "+ str(float(amountDisc))+"\n")
                file.write("TOTAL\t\tRM "+str(float(amountPayment))+"\n")

                import time
                time = time.strftime("%c")
                file.write("\n--PAID--\n\n"+time+"\n")
                
                file.close()        

                file = open(userfile, "r+")
                file = file.read()
                print(file)
                
                amountPayment = 0
                try:
                    for key, value in order.items():
                        order[key] = 0
                except :
                    print("System failure")
                print("Transaction successful\n")
                user = input("Transaction is complete. Go back to main menu(Y/N)? ")
                if user == "Y" :
                    continue
                elif user == "N" :
                    print("Thank you, ",name)
                    break
                else :
                    print("invalid entry")
                    continue
               
            elif pay == "2" :
                continue
            else :
                print("invalid entry")
                continue
            
        elif user == "M" :
            continue
        else :
            print("invalid entry")
            continue

    elif user == "R" :  #Report Module
        print("==========\nREPORT MODULE\n==========")
        user = input("I - Display the invoice for order made\nS - Display the summary of order and payments made\nM - Return to Main Menu\ntype : ")
        if user == "I" :
            print("=======\nINVOICE\n========")
            for key, value in order.items():
                if int(value) > 0 :
                    try :
                        print(key('chairs'), "\t\t",value)
                    except :
                        print(key,"\t=",value)
            continue
            
        if user == "S" :            #Final Summary of the orders
            if paid == "Yes" :
                file = open(userfile, "r+")
                file = file.read()
                print(file)
                
            if paid == "No" :
                print("Sorry, you haven't made the payment")
                continue
        if user == "M" :
            continue
    elif user == "E" :
        print("Thankyou")
        break

    else :
        print("invalid entry")
        continue
    
    

