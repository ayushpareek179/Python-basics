while True:
    print ("Who are you?")
    name = input()
    if name != "Joe":
        continue
    while True:
        print ("Hello "+name+". What is the password? (It is a fish.)")
        password = input()
        if password == "swordfish":
            break
    break
print ("Access granted.")

