print("*****creams story*****")
print("creams story menu bars")
print("strawberry-120")
print("vanilla-100")
print("butterscotch-150")
print("blackcurrent-180")
print("chocobar-140")
one_strawberry=120
one_vanilla=100
one_butterscotch=150
one_blackcurrent=180
one_chocobar=140
menus=["strawberry","vanilla","butterscotch","blackcurrent","chocobar"]
your_favour=input("enter your favour:")
if your_favour in menus:
    print(f"yes {your_favour} is available")
    quantity=int(input(f"how many {your_favour} you want:"))
    add=(input("you want extra toppins:"))
    if your_favour=="strawberry":
        total=one_strawberry*quantity
        if total>=500:
            offer_total=total-100
            print(f"you ordered 500rs above so 100rs less your bill finally your bill is {offer_total} ")
        else:
            print(f"your bill is {total}")
    elif your_favour=="vanilla":
        total=one_vanilla*quantity
        if total>=500:
            offer_total=total-100
            print(f"you ordered 500rs above so 100rs less your bill finally your bill is {offer_total} ")
        else:
            print(f"your bill is {total}")
    elif your_favour=="butterscotch":
        total=one_butterscotch*quantity
        if total>=500:
            offer_total=total-100
            print(f"you ordered 500rs above so 100rs less your bill finally your total bill is {offer_total} ")
        else:
            print(f"your bill is {total}")
    elif your_favour=="blackcurrent":
        total=one_blackcurrent*quantity
        if total>=500:
            offer_total=total-100
            print(f"you ordered 500rs above so 100rs less your bill finally your total bill is {offer_total} ")
        else:
            print(f"your bill is {total}")
    elif your_favour=="chocobar":
        total=one_chocobar*quantity
        if total>=500:
            offer_total=total-100
            print(f"you ordered 500rs above so 100rs less your bill finally your total bill is {offer_total} ")
        else:
            print(f"your bill is {total}")
else:
    print(f"sorry {your_favour} is not available")

                                    
                            
                    
            
            
            




