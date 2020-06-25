print('enter x for exit')
binary=input('enter a number in binary form')
if binary == 'x':
    exit()
else:
        decimal = int(binary, 2)
        print(binary,"in decimal",decimal)
