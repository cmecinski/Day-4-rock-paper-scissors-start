import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if int(player_choice) >= 3 or int(player_choice) < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[int(player_choice)])
  
  print("\n Computer chose:\n")
  computer_choice = random.randint(0, 2)
  print(game_images[computer_choice])
  
  Outcome_matrix1 = ["Tie","Win","Lose"]
  Outcome_matrix2 = ["Lose","Tie","Win"]
  Outcome_matrix3 = ["Win", "Lose", "Tie"]
  
  map = [Outcome_matrix1,Outcome_matrix2,Outcome_matrix3]
  
  position_string = str(player_choice) + str(computer_choice)
  column = int(position_string[0]) - 1
  row = int(position_string[1]) - 1
  
  print(f"You {map[row][column]}")