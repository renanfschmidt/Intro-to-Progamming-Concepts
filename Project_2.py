beverages = {
    '1': {'name': 'coca', 'price': 2.50},
    '2': {'name': 'fanta', 'price': 3.00},
    '3': {'name': 'pepsi', 'price': 2.75},
    '4': {'name': 'water', 'price': 1.50},
    '5': {'name': 'dr.pepper', 'price': 1.00},
    '6': {'name': 'mountain dew', 'price': 4.00},
}
while True:
 print("\nVending Machine")
 for key, value in beverages.items():
  print(f"{key}: {value['name']}  ${value['price']}")
 user_choice = input('\nChoose a beverage (or type "off" to shut down): ')
 if user_choice.lower() == 'off':
  print("end")
  break
 if user_choice in beverages:
  drink= beverages[user_choice]
  print(f"You chose:{drink['name']}(${drink['price']})")
  insert_money =float(input('Insert money:'))
  if insert_money <drink['price']:
   print("Not enough money.")
  else:
    change=insert_money- drink['price']
    print(f"Dispensing {drink['name']}...")
    if change> 0:
     print(f"Heres your change: ${(change)}")
 else:
        print("Invalid selection")

#Renan Faria Schmidt