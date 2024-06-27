#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def get_user_choice():
    user_choice = input("Enter choice (rock, paper, scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter either rock, paper, or scissors.")
        user_choice = input("Enter choice (rock, paper, scissors): ").strip().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer wins!"
        else:
            return "You win!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()







