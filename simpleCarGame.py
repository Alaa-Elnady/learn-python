# While Loop Example
# We will build simulation of simple car system as a game
# 1. You will recive an input from user (It must be "help" word to list the car system otpions to him/her) 
  # NOTE: If the user entered anything other than "help" word you should show warning msg like: I don't understand that ...
# 2. After recieving the word help from user the options will listed like this: 
  # start - to start the car
  # stop - to stop the car
  # quit - to exit
# 3. According to the option he/she enter the action of this option appear:
  # If he enter start ---> show : Car started ... Ready to go!
  # If he enter stop ---> show : Car stopped
  # If he enter quit ---> the game will terminate 

# Solution:
user_command = ''
started = False
while True:
  user_command = input('> ').lower()
  if user_command == 'start':
    if started:
      print('Car is already started!')
    else:
      started = True
      print('Car started ... Ready to go!')
  elif user_command == 'stop':
    if not started:
      print('Car is already stopped!')
    else:
      started = False
      print('Car stopped.')
  elif user_command == 'help':
    print(''' 
      start - to start the car
      stop - to stop the car
      quit - to exit
    ''') 
  elif user_command == 'quit':
    break  
  else:
    print("Sorry, I don't understand that ...")
