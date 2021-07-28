"""You working as software developer. One of your customer is planning to make on 50% discount on the products he is selling
so he asked from you to desing a program that give the price of the any product after 50% discount"""

def product_input():
    while True:
        try:
            product_value = float(input("enter the product value "))
            return product_value

        except:
            print("product input incorrect")
    
def discount_input():
    while True:
        try:
            discount = int(input("enter the discount of 0 to 100% "))
            if not 0 <= discount or discount >= 100:
                print("discount input error")
            else:
                return discount
        except:
            print("data input incorrect")

def calculate_discount(discount, product_value): #i change the names of the variables it will recive....why?...dont know

    discounted_product =product_value -( product_value * (discount/100))
    return print(f"the product value with discount of {discount}% will be ${discounted_product}")

if __name__ == '__main__':

    product = product_input()
    offer = discount_input()
    calculate_discount(offer,product)



