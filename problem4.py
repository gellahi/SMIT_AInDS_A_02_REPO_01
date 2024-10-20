name = input("Enter your Name: ")
flipName=name[::-1]
if name.lower() == flipName.lower():
    print("Your Name is 2 way")
else:
    print("Your Name is 1 way")
