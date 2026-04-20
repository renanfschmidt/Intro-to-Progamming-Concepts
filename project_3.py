seats =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
total_cost =80
while len(seats)> 0:
 print(f"Available seats:{seats}")
 choice =input("Select a seat number or type exit: ")
 if choice.lower() =='exit':
    break
 selection =int(choice)
 if selection in seats:
  if 1<= selection<= 4:
   print("This is a first-class seat,a $50 fee applies.")
   total_cost +=50
  elif 13<= selection<= 20:
   confirm =input("This is an emergency row,do you accept responsibility to help?(yes/no)")
   if confirm.lower()!= 'yes':
     print("Seat selection cancelled.")
     continue
   seats.remove(selection)
  print(f"Seat {selection} reserved")
else:
 print("seat already taken.")


print(f"Total cost ${total_cost}")

#Renan Faria Schmidt#