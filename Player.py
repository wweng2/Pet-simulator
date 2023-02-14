
class player:
  
  def __init__(self,name,age,story):
    
    self.name = name
    self.set_age(age)

    self.set_story(story)

  # Get function that return values the class have have 
  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_story(self):
    return self.story

  def set_age(self,age):

    default_age = 1 
    if (age <= 0) : # Prevent the age to be less than 0 so they can't be unborn
      print("This is too young to have a pet, as your aren't born yet ")
      self.age = default_age
    else:# If they are less than zero the age will be set to what they want even if it's a decimal
      self.age = age



  def set_story(self, story):
    self.story = story # turn the story variable to a strin that the use type

  def update_age(self,time):

    self.age += time # update age by any numbert the use want can be use to increase or decrease the age

  def update_story(self,chapter):

    self.story = self.story + "/n" + str(chapter) # add a new part to the story portion of the character that is separate by a new line for reading sake


  def display_stat(self):

    print("name: " + self.get_name() +"\n" + "age: " + str(self.get_age()) +"\n" + "story: " + self.get_story() +"\n" )