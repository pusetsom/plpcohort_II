# name.split - splits the input, this is to avoid counting the whitespaces
# .join - joins the list with no whitespaces
string = input('Input a string name to check the length: ')
if len(''.join(str(string))) == 0:
    print("Empty string")
else:
    space = string.split()
    print("{0} is {1}".format(string, str(len(''.join(space)))))
