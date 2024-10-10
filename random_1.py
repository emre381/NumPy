import numpy as np

# generate_rand_num = np.random.randint(1,10, size=5)

# generate_rand_num = np.random.random(5)
# print("Random numbers : ", generate_rand_num)

# normal_num = np.random.normal(0,1,5)
rand_num = np.random.rand(3,3)*10
rand_num=rand_num.astype(int)
print("Random numbers : ", rand_num)