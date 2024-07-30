print(f'================== \n Area Calculator 📐 \n ================== \n 1) Triangle \n 2) Rectangle \n 3) Square \n 4) Circle \n 5) Quit')
option = int(input())
if option == 1:
    side = int(input('Enter side: '))
    calc1 = side**2
    print(f'Area is {calc1}')
elif option == 2:
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    calc2 = length*width
    print(f'Area is {calc2}')
elif option == 3:
    height = int(input('Enter height: '))
    base = int(input('Enter base: '))
    calc3 = (height*base)/2
    print(f'Area is {calc3}')

elif option == 4:
    radius = int(input('Enter radius: '))
    calc4 = 3.14 * radius**2
    print(f'Area is {calc4}')
elif option == 5:
    print('Exited')
    exit()
else:
    print('Sorry wrong input!')
