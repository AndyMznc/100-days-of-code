import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
friends2 = ["John", "Sofie", "Sarah"]

dozen_list = [friends, friends2]

print(f"The dozen list : {dozen_list[1][1]}")

print(len(friends))

# 1. Option
randomizer = random.randint(0, 4)
print(friends[randomizer])

# 2. Option (The best, shorter and no need to know how many items are in the list.)
print(random.choice(friends))
