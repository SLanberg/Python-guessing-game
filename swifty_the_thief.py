"""SWIFTY THE THIEF"""

import random
# Player lives
lives = 3

# List that we will use as improvised "npc inventory"
npc_inventory = ['purse', 'backpack', 'inner pocket', 'lunch box', 'bag']

# Set item to find to be random integer from first to fifth element of list
item_to_find = npc_inventory[random.randint(0, 4)]

print("""
                    .
                   / \\
                  _\ /_
        .     .  (,'v`.)  .     .
        \)   ( )  ,' `.  ( )   (/
         \`. / `-'     `-' \ ,'/
          : '    _______    ' :
          |  _,-'  ,-.  `-._  |
          |,' ( )__`-'__( ) `.|
          (|,-,'-._   _.-`.-.|)
          /  /<( o)> <( o)>\  \         (I'm the king of this land! Give me all your money!
          :  :     | |     :  :          I'll build another castle for me with gold that I stol... I
          |  |     ; :     |  |            MEAN TOOK WHAT BELONG TO ME FROM YOU! AND ALL BECAUSE I HAVE THIS CONTRACT!)
          |  |    (.-.)    |  |          /
          |  |  ,' ___ `.  |  |
          ;  |)/ ,'---'. \(|  :
      _,-/   |/\(       )/\|   \-._
_..--'.-(    |   `-'''-'   |    )-.`--.._
         `.  ;`._________,':  ,'
        ,' `/               \`.
             `------.------'
                    '
                    """)
# Here we inform player what inventory slots king has
print(f"""we can try to find and steal king's contract from: {(", ".join(npc_inventory))}""")
print("\nType item you want to search\n")
# We restrict player to have 3 tries
while lives > 0:
    to_steal = input('Where do you want to check?')
    if to_steal.casefold() == item_to_find.casefold():
        print(f"""\nYou stole contract from {item_to_find}!
Now your village can survive this winter and topple the king!
  .__.
 (|  |)
  (  )
  _)(_ """)
        break
    else:
        lives -= 1                   # Lives of player with each failed try -1
        print(f'\nYou tried to find anything, but nothing in there! You have - {lives} health')
        if lives == 0:               # Death, Game Over screen.
            print(f"""\nGAME OVER THE KING CAUGHT YOU! CONTRACT WAS AT {item_to_find.upper()}!
    %%% %%%%%%%            |#|
    %%%% %%%%%%%%%%%        |#|####
  %%%%% %         %%%       |#|=#####
 %%%%% %   @    @   %%      | | ==####
%%%%%% % (_  ()  )  %%     | |    ===##
%%  %%% %  \_    | %%      | |       =##
%    %%%% %  u^uuu %%     | |         ==#
      %%%% %%%%%%%%%      | |           V
                                                """)
