import random

class character():

   ABILITY_SCORES = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
   ABILITY_SCORE_MODIFIER ={
      1: -5,
      2: -4,
      3: -4,
      4: -3,
      5: -3,
      6: -2,
      7: -2,
      8: -1,
      9: -1,
      10: 0,
      11: 0,
      12: 1,
      13: 1,
      14: 2,
      15: 2,
      16: 3,
      17: 3,
      18: 4,
      19: 4,
      20: 5,
      21: 5,
      22: 6,
      23: 6,
      24: 7,
      25: 7,
      26: 8,
      27: 8,
      28: 9,
      29: 9,
      30: 10
   }

   def __init__(self, character_name):
      self.name = character_name
      self.character_class = None
      self.primary_ability = None
      self.stats = {
         armor_class: 0,
         initiative: 0,
         speed: 0,
         cur_hit_points: 0,
         temp_hit_points: 0,
         max_hit_points: 0,
         hit_dice: None,
         death_success: 0,
         death_fail: 0,
         proficiency_bonus: 0
         ability_score: {
            strength: 0,
            dexterity: 0,
            constitution: 0,
            intelligence: 0,
            wisdom:  0,
            charisma: 0
         }
      }
      self.spells = {
         known: None,
         slots: None,
         spell_list: None,
         prepared_spells: None,
         casting_ability: 0,
         save_dc: 0,
         attack_bonus: 0,
      }

   def increase_strength(x):
      self.stats.ability_score.strength += x

   def increase_dexterity(x):
      self.stats.ability_score.dexterity += x

   def increase_constitution(x):
      self.stats.ability_score.constitution += x

   def increase_intelligence(x):
      self.stats.ability_score.intelligence += x

   def increase_wisdom(x):
      self.stats.ability_score.wisdom += x

   def increase_charisma(x):
      self.stats.ability_score.charisma += x
   
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
         self.stats.proficiency_bonus += 2
         self.rage = 2
         self.stats.max_hit_points += (12 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Strength']
         self.stats.hit_dice = [12]

      elif pick_class.lower() == "bard":
         self.stats.proficiency_bonus += 2
         self.spells.known = 4
         self.spells.slots = [2,2]
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.charisma]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.attack_bonus = self.stats.proficiency_bonus + ABILITY_SCORE_MODIFIER[self.stats.ability_score.charisma]
         self.stats.max_hit_points += (8 + self.spell.casting_ability)
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Charisma']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "cleric":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [3,2]
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.wisdom]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (8 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Wisdom']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "druid":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [2,2]
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.wisdom]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (8 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Wisdom']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "fighter":
         self.stats.proficiency_bonus += 2
         self.stats.max_hit_points += (10 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Strength', 'Dexterity']
         self.stats.hit_dice = [10]

      elif pick_class.lower() == "monk":
         self.stats.proficiency_bonus += 2
         self.martial = [4]
         self.ki = 0
         self.stats.max_hit_points += (8 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Strength', 'Wisdom']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "paladin":
         self.stats.proficiency_bonus += 2
         self.stats.max_hit_points += (10 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Strength', 'Charisma']
         self.stats.hit_dice = [10]

      elif pick_class.lower() == "ranger":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [0,0]
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.wisdom]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (10 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Dexterity', 'Wisdom']
         self.stats.hit_dice = [10]

      elif pick_class.lower() == "rogue":
         self.stats.proficiency_bonus += 2
         self.sneak_attack = [6]
         self.stats.max_hit_points += (8 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Dexterity']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "sorcerer":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [4,2]
         self.spells.known = 2
         self.sorcery_points = 2
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.charisma]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (6 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Charisma']
         self.stats.hit_dice = [6]

      elif pick_class.lower() == "warlock":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [2,1]
         self.invocations_known = 0
         self.spells.known = 2
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.charisma]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (8 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Charisma']
         self.stats.hit_dice = [8]

      elif pick_class.lower() == "wizard":
         self.stats.proficiency_bonus += 2
         self.spells.slots = [3,2]
         self.spells.casting_ability = ABILITY_SCORE_MODIFIER[self.stats.ability_score.Intelligence]
         self.spells.save_dc = 8 + self.stats.proficiency_bonus + self.spell.casting_ability
         self.spells.attack_bonus = self.stats.proficiency_bonus +  self.spells.casting_ability 
         self.stats.max_hit_points += (6 + ABILITY_SCORE_MODIFIER[self.stats.ability_score.constitution])
         self.stats.cur_hit_points = self.stats.max_hit_points
         self.primary_ability = ['Intelligence']
         self.stats.hit_dice = [6]

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
