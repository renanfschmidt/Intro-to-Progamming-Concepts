def taco_kiosk():
    menu={
        'taco':2,
        'burrito':3,
        'Quit':0
    }
    print('Welcome to Taco Palace! Please view the menu below and make a selection')
    menu_count = True
    while menu_count:
        for count, item in enumerate(menu, start=1):
            print(f"{count}.{item}")
        selection = int(input('Select an option: '))
        if selection == 1:
            print('You have selected',menu['taco'])
        if selection == 2:
            print('You have selected', menu['burrito'])
        elif selection == 3:
            menu_count = False
        total = sum(menu.values())
        print('-' * 50)
        print(f'Your total is $ {total:.2f}')
    return total
final_payment = taco_kiosk()
