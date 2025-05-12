itemsincart = 0

def add_to_cart(item):
    global itemsincart
    if item < 0:
        raise Exception("Cannot add a negative number of items")
    elif item >5:
        raise Exception("Cart limit exceeded")
    else:
        itemsincart = itemsincart + item
        print(f"{item} items added. Total in cart: {itemsincart}")
try:
    add_to_cart(2)
    add_to_cart(-1)


except Exception as e:
    print(e)