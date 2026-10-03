print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      ''' )
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
your_choice=input("Lets Play!\nDo you want to go Left or Right? Write L or R = ")
if your_choice == 'l' or your_choice == 'L':
    swim=input("Welcome to the River. Do you wish to swim or wait for boat? Write S for Swim and W for wait = ")
    if swim == "W" or swim == "w":
        door= input("Which door you wish to enter. R for Red, B for Blue or Y for Yellow = ")
        if door == "Y" or door == "y":
            print("YOU WIN.")
        elif door == "R" or door == "r":
            print("FIRE. GAME OVER.")
        elif door == "B" or door == "b":
            print("WATER. GAME OVER.")    
        else: 
            print("Make better choices. GAME OVER!")
    elif swim == "S" or swim == "s":
        print("Sorry. Attacked by Trout. GAME OVER")
    else:
        print("Wrong Input. Write S for Swim and W for wait.")
elif your_choice == 'r' or your_choice == 'R':
    print("You are in a hole. GAME OVER") 
else: 
    print("Wrong Input. Write L for Left or R for Right.")    