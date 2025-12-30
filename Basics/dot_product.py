# # Dot Product collapses 2 list of numbers into a single meaingful value

# Imagine you are at a store.
# Vector A (Your Cart): You have 3 apples and 2 bananas. [3, 2]
# Vector B (Prices): Apples cost $10 and Bananas cost $5. [10, 5]
# To find the Total Bill, you naturally do the dot product without thinking about it:
# Multiply apples by apple price: 3 * 10 = 30
# Multiply bananas by banana price: 2 * 5 = 10
# Sum them up: 30 + 10 = 40. That final number, 40, is the dot product.

import numpy as np

cart = [2, 1, 4]  # 2 shirts, 1 hat, 4 socks
prices = [20, 10, 5]  # Shirt ($20), Hat ($10), Socks ($5)

# Calculate dot product using np.dot

# 1. Convert list to math vector
cart_vector = np.array(cart)
prices_vector = np.array(prices)

# Calculate dot product
total_cost = np.dot(cart_vector, prices_vector)
print(total_cost)  # 70
