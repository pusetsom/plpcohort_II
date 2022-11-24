# name.split - splits the input, this is to avoid counting the whitespaces
# .join - joins the list with no whitespaces
string = input('Input a string name to check the length: ')
if len(''.join(str(string))) == 0:
    print('0 because it\'s an empty string.')
else:
    space = string.split()
    print(f"{str(len(''.join(space)))} because it has {str(len(''.join(space)))} characters.")
    
