

class pet:

  def __init__(self,name,age,species,lifespan):
    self.set_name(name)
    self.set_lifeSpan()
    self.set_age(age)
    self.set_species(species)

   
    self.set_health(100)
    
# These three get function return the oejcts's decriptions
  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_species(self):
    return self.species

# These three get functrion get the pet objects's status and condtion
  def get_cleaness(self):

    return self.cleaness

  def get_health(self):
    return self.health
  
  def get_fullness(self):
    return self.fullness

  def get_lifeSpan(self):
    return self.lifeSpan
  # These set function are to help set the pet's basic info
  def set_name(self,name):
    self.name = name

  def set_species(self,species):

    self.species = species

  def set_age(self,age):
    
    default_age = 1 
    if (age <= 0) : # Prevent the age to be less than 0 so they can't be unborn
      print("This pet hasn't born yet")
      self.age = default_age

    elif (age > self.get_lifeSpan()):
      self.age = default_age
    else:# If they are less than zero the age will be set to what they want even if it's a decimal
      self.age = age

  def set_lifeSpan(self):
    defualt_lifeSpan = 1

    self.lifeSpan = defualt_lifeSpan

 # These set function are for setting and adjucting thestatus bars for the pet object
  def set_health(self,health):

    default_health = 100
    if (health <= 0):
      self.health = default_health
    
    elif(health > 100):
      self.health = default_health

    else:

      self.health = health

  def set_cleaness(self,cleaness):

    default_cleaness = 100
    if (cleaness <= 0):
      self.cleaness = default_cleaness
    
    elif(cleaness > 100):
      self.cleaness = default_cleaness

    else:

      self.cleaness = cleaness

  def set_fullness(self,fullness):

    default_fullness = 100
    if (fullness <= 0):
      self.fullness = default_fullness
    
    elif(fullness > 100):
      self.fullness = default_fullness

    else:

      self.fullness = fullness

  def update_age(self,age):
    self.age += age # change the age based whatever is put in , so it can be flexible

# This function update the health of the pet , but will not go over 100 the max health
  def update_health(self,health_change):
    max_health = 100
    min_health = 0

    if(self.get_health() + health_change > max_health):# If the the health and the increase health is greater than 100 it will just increase the health bar into the max health of 100

      print("The max health is 100 and can't go higher")
      self.health = max_health
    
    elif(self.get_health() + health_change < min_health):# if the heaht drop lower than a zero set it to a zero to avoid negatives 

      self.health = min_health

      print("The health is 0 and can't go lower")

    else:

      self.health += health_change

  def update_fullness(self,fullness_change):
    max_fullness = 100
    min_fullness = 0
  # Change the fullness to 100 if the change is greater 100 to avoid go avbove the max
    if(self.get_fullness() + fullness_change > max_fullness ):

      print("The max fullness is 100 and can't go higher")
      self.fullness = max_fullness 
    # If the fullness bar drop below 0 set it to zero so that a pet can't be negativly hungry
    elif(self.get_fullness() + fullness_change < min_fullness):

      self.fullness = min_fullness

      print("The fullness is 0 and can't go lower")

    else:

      self.fullness += fullness_change



  def update_cleaness(self,cleaness_change):
    max_cleaness = 100
    min_cleaness = 0

    if(self.get_cleaness() + cleaness_change > max_cleaness):# If the cleaness goes above the mz cleaness , just increase the number up to only the max

      print("The max health is 100 and can't go higher")
      self.cleaness = max_cleaness
    
    elif(self.get_cleaness() + cleaness_change < min_cleaness): # Turn the cleaness bar zero if the cleaness change will be a negative number

      self.cleaness = min_cleaness

      print("The health is 0 and can't go lower")

    else:

      self.cleaness += cleaness_change
  

 
  def hunger(self):
    # Hunger will be affect by two 
    starvation_rate = .5

    cleaness_rate = .2

    appitate = self.get_health() * starvation_rate + self.get_cleanness() * cleaness_rate 

    hunger = -appitate
    return hunger



  def dirtiness(self):

    food_dirt = .2

    playing_dirt = .3
    dirt = self.get_fullness() * food_dirt + self.get_health * play_dirt 
    dirtness = -dirt

    return dirtness
  def sickness(self):

    full = 100
    clean = 100
    dirtness_sickness = clean - self.get_cleaness()# The difference between the max bar and the curretn bar so that 
    starving = full - self.get_fullness()

    sick = dirtness_sickness * .3 + starving  * .4
    sickness = -sick
    return sickness
  
  def display_desciption(self):# This display the decription of the pet
    print("Name: " + self.get_name() + " Age: " + str(self.get_age()) + " species: "+ self.get_species() )
  
  def display_stat(self):# This one will display the statis of the pet 

    print("Health: " + str(self.get_health) + " Fullness: " + str(self.get_fullness) + "cleaness: " + str(self.get_cleaness()))
