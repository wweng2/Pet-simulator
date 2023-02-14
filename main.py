from Dog import dog
from Cat import cat
from Frog import frog
from Hamster import hamster
from Lizard import lizard
from Rabbit import rabbit
from Tortoise import tortoise

from Player import player
import random


class simulation:
  
  def pet_create():


    pet_type = str(input("What kind of pet would you like/n : we have Cat,Dog,Frog,Hamster,Lizard,Rabbit, tortoise))

    check = false
    while(check == false):
      age = int(input("Please choose an age for the pet starting out from 1-3"))
      
      if(age>= 1 and age <=3):
        check = true
    
    if(pet_type == "Cat"):
      pet = Cat()
    return pet
  
  def player_create():
    print("Player creation is starting , please fill out the info require ")

    name = str(input("What is your name? "))

    age = int(input("What is your age? "))

    while(age < 0):

      age = int(input("What is your age? "))
    
    story = str(input("Would you like to type a story for youself? "))

    Player = player(name,age,story)

    
    return Player

  def time_increase(day):
    day += 1

    return day
    

  def score_count(score,score_increase):
    score_count += score_increase
  
  def pet_end(pet,day):
    if(day > pet.get_lifespan()):
      return true
    else:
      return false: 
  
  def section_end(pet):
    print("This has ended , here is now your score")
    print(score)

    pet.display_desciption

  
  def simulation():

    print("Let create the player now")

    player = player_create()

    choice = 0
    day = 0
    


   
    while(choice != 1):
      option = 0
      while(option != 2):

      
 
  def game_over(pet,day):
    

    



