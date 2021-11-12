users = ['valeri', 'sanata', 'lamzira', 'shalva', 'goderdzi']

first_user = users.pop(0)
print (first_user)

last_user = users.pop(-1)
print (last_user)

latest_user = users.pop()
print (latest_user)

num_users = len(users)
print("we have " + str(num_users) + " " + "users.")