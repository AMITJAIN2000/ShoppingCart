def additems():
    items=input("enter the product which you add in the cart")

    cart.append(items.lower())
    print(cart)
def removeitems():
    item=input("enter the product  which you want to remove")
    if len(cart)==0:
        print("your cart is empty")
    else:
        cart.remove(item.lower())
    print(cart)
    return cart
def clearitems():
    #item = input("enter the product  which you want to clea the cart")
    #print("add")
    cart.clear()
    print(cart)
def showitems():
    print(cart)

cart=[]

while(True):
    print("Shopping Cart")
    print("1.add items")
    print("2.remove items")
    print("3.clearitems")
    print("4.show items")
    print("5.quit")
    try:
        select=int(input("enter what you want to do operation in above:-"))
        if select==1:
            additems()
        elif select==2:
            removeitems()
        elif select==3:
            clearitems()
        elif select==4:
            showitems()
        elif select==5:
            break
        else:
            print("please select correct one")
    except:
        print("please selected number")
print("thank you")

