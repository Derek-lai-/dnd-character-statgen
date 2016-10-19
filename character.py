import random

class character():

   ABILITY_SCORE = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

   def __init__(self, character_name):
      self.name = character_name
      self.character_class = None
      self.character_points = {
         armor_class: 0,
         initiative: 0,
         speed: 0,
         cur_hit_points: None,
         temp_hit_points: None,
         hit_dice: None,
         death_success: 0,
         death_fail: 0
      }
      self.stats = {
         proficiency_bonus: 0,
         strength: 0,
         dexterity: 0,
         constitution: 0,
         intelligence: 0,
         wisdom:  0,
         charisma: 0,
      }

   def increase_strength(x):
      self.stats.strength += x

   def increase_dexterity(x):
      self.stats.dexterity += x

   def increase_constitution(x):
      self.stats.constitution += x

   def increase_intelligence(x):
      self.stats.intelligence += x

   def increase_wisdom(x):
      self.stats.wisdom += x

   def increase_charisma(x):
      self.stats.charisma += x
   
   def roll_dice():
      roll = random.randint(1,6)
      return roll

   def generate_character_stats():
      stats = []
      #roll for ability scoes
      for ability in range(5):
         #dice roll scores
         dice_rolls = []
         #roll 4 times
         for rolls in range(3):
            dice_roll.append(roll_dice())
         #remove lowest roll
         stats.append(sum(dice_rolls.remove(min(dice_rolls))))
      return stats

   def choose_class(pick_class):
      if pick_class.lower() == "barbarian":
         self.character_points.proficiency_bonus += 2

      elif pick_class.lower() == "bard":

      elif pick_class.lower() == "cleric":

      elif pick_class.lower() == "druid":

      elif pick_class.lower() == "fighter":

      elif pick_class.lower() == "monk":

      elif pick_class.lower() == "paladin":

      elif pick_class.lower() == "ranger":

      elif pick_class.lower() == "rogue":

      elif pick_class.lower() == "sorcerer":

      elif pick_class.lower() == "warlock":

      elif pick_class.lower() == "wizard":


   def choose_race(pick_race):
      if pick_race.lower() == "dwarf":
         increase_strength(2)
         increase_constitution(2)
         increase_wisdom(1)

      elif pick_race.lower() == "elf":
         increase_intelligence(1)
         increase_wisdom(1)
         increase_charisma(2)

      elif pick_race.lower() == "halfling":
         increase_dexterity(2)
         increase_constitution(1)
         increase_charisma(1)

      elif pick_race.lower() == "human":
         increase_strength(1)
         increase_dexterity(1)
         increase_wisdom(1)
         increase_charisma(1)
         increase_intelligence(1)

      elif pick_race.lower() == "dragonborn":
         increase_strength(2)
         increase_charisma(1)

      elif pick_race.lower() == "gnome":
         increase_dexterity(1)
         increase_constitution(1)
         increase_intelligence(2)

      elif pick_race.lower() == "half-elf" or pick_race.lower() == "halfelf":
         increase_dexterity(2)
         extra_ability_score(2)

      elif pick_race.lower() == "half-orc" or pick_race.lower() == "halforc":
         increase_strength(2)
         increase_constitution(1)

      elif pick_race.lower() == "tiefling":
         increase_intelligence(1)
         increase_charisma(2)

   def extra_ability_score(x):
      for i in range(1,x):
         print("Chose where to allocate your extra point:")

         for i in range(1, len(ABILITY_SCORE)):
            print("$0 : $1 \n".format(i, ABILITY_SCORE[i]))

         choice = raw_input(">")
         if choice.lower() == "strength":
            increase_strength(1)
         if choice.lower() == "dexterity":
            increase_dexterity(1)
         if choice.lower() == "constitution":
            increase_constitution(1)
         if choice.lower() == "intelligence":
            increase_intelligence(1)
         if choice.lower() == "wisdom":
            increase_wisdom(1)
         if choice.lower() == "charisma":
            increase_charisma(1)

  