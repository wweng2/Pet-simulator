from Pet import pet

class tortoise(pet):


  def set_lifeSpan(self):
    defualt_lifeSpan = 50# The max  year a dog can live 

    self.lifeSpan = defualt_lifeSpan
  def hunger(self):
    # Hunger will be affect by two 
    starvation_rate = .2

    cleaness_rate = .1

    appitate = self.get_health() * starvation_rate + self.get_cleanness() * cleaness_rate 

    hunger = -appitate
    return hunger



  def dirtiness(self):

    food_dirt = .1

    playing_dirt = .2
    dirt = self.get_fullness() * food_dirt + self.get_health * play_dirt 
    dirtness = -dirt

    return dirtness
  def sickness(self):

    full = 100
    clean = 100
    dirtness_sickness = clean - self.get_cleaness()# The difference between the max bar and the curretn bar so that 
    starving = full - self.get_fullness()

    sick = dirtness_sickness * .1 + starving  * .2
    sickness = -sick
    return sickness
