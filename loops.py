def taco_kiosk():
    list = ['Taco', 'Burrito', 'Nachos', 'Drink', 'Quit']
    list_menu = []
    items_ordered = []
    print('Welcome to Taco Palace! Please view the menu below and make a selection')
    menu_count = True
    while menu_count:
        for count, item in enumerate(list, start=1):
            print(f"{count}.{item}")
        selection = int(input('Select an option: '))
        if selection == 1:
            print('You have selected',list[0])
            items_ordered.append(list[0])
            list_menu.append(3)
        elif selection == 2:
            print('You have selected',list[1])
            items_ordered.append(list[1])
            list_menu.append(3)
        elif selection == 3:
            print('You have selected',list[2])
            items_ordered.append(list[2])
            list_menu.append(4)
        elif selection == 4:
            print('You have selected',list[3])
            items_ordered.append(list[3])
            list_menu.append(2.50)
        elif selection == 5:
            menu_count = False
        total = sum(list_menu)
        print('-' * 50)
        print(f"You ordered a {' and a '.join(items_ordered)}")
        print(f'Your total is $ {total:.2f}')
    return total
final_payment = taco_kiosk()