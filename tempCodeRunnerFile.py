bucket2 = ("watermelon", "mango")
t = list(bucket2)
t[1] = "kiwi"
bucket2 = tuple(t)
print(bucket2)