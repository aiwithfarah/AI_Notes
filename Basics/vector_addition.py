# Vecotr Addition ---> How AI combines different signals

import numpy as np

source_a = [10, 20, 30]
source_b = [5, 5, 5]

# convert list to math vector
vector_a = np.array(source_a)
vector_b = np.array(source_b)

# add them
print(vector_a + vector_b)  # [15 25 35]

# Element-wise Addition. NumPy took the first element of A and added it to the first element of B, and so on.
