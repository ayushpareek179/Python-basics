import sys

while True:
    print ("Type 'exit' (without quotes) to exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print ("You typed "+response+".")
