# Prices & Constant(s)
mousePrice_1 = 6.63
mousePrice_2 = 6.30
mousePrice_3 = 6.23
mousePrice_4orMore = 6.17
shippingCostBarrier = 3
shippingCost = 2.99

# Input
quantity = int(input("\nQuantity Purchasing\n-------------------\nHow many 2.4GHz Wireless Optical Mice would you like to purchase? "))

if quantity == 1:
    price = mousePrice_1
elif quantity == 2:
    price = mousePrice_2
elif quantity == 3:
    price = mousePrice_3
else:
    price = mousePrice_4orMore

subtotal = quantity * price

# Shipping Cost
if quantity < shippingCostBarrier:
    shipping = shippingCost
else:
    shipping = 0.0

# Grand Total
total = shipping + subtotal

# Generate formatted output
print(f'You\'ve Purchased ({quantity}) 2.4GHz Wireless Optical Mice')
print(f'At a unit price of $ {price:.2f} each')
print(f'Your subtotal for this order is: $ {subtotal:.2f}')
print(f'Calculated shipping costs are: $ {shipping:.2f}')
print(' -------')
print(f'Your total bill comes to: $ {total:.2f}')
print('Thank you for your order!!!')