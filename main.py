print('Welcome to the Exclusive Elite 101 Chatbot!')
name = input('Please enter your name: ')
print(f'Welcome {name}, nice to meet you!')
age = input(f'{name}, how old are you? ')
print('Pleasure to assist you, how could I help you today?')

print('\n Please choose from the following options: \n 1. Say something inspiring \n 2. Whats a great way to earn money \n 3. What are good grocery stores near me? \n 4. Exit the Conversation')
userchoice = input('Enter the number of your choice: ')



if userchoice == "1":
  print("You have a bright future ahead of you!") 

if userchoice == "2":
  print('You can earn money by working hard and being very consistant!')

if userchoice == "3":
  print('You can find great grocery stores near you by utilizing google maps!')

if userchoice == "4":
  print("Thank you for using the Exclusive Elite 101 Chatbot! Have a great day!")
