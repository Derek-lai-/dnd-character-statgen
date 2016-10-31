from character import Character

import json
import pprint
import os

class Character_Gen_Menu:

	ABILITY_SCORE = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
	CLASSES = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Palidin', 'Ranger', 'Rouge', 'Sorcere', 'Warlock', 'Wiard']
	RACES = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

	def __init__(self):
		self.character = None

	def generate_character(self):
		self.character = Character()
		choose_character_name()
		pick_character_race()
		pick_character_class()
		assign_ability_points()

	def choose_character_name(self):
		print ("Choose a name for your character: \n")
		choice_name = raw_input("> ")
		self.character.character_name == choice_name

	def pick_character_race(self):
		print ("Select a character race:\n")

		for race_index in range(len(RACES)):
			print '{0}: {1} \n'.format(race_index, RACES[race_index]) 

		choice_race = raw_input('> ')
		self.character.choose_class(CLASSES[choice_race - 1])

	def pick_character_class(self):
		print ("Select a class: \n")

		for class_index in range(len(CLASSES)):
			print '{0}: {1} \n'.format(class_index, CLASSES[class_index])

		choice_class = raw_input('> ')
		self.character.choose_class(CLASSES[choice_class - 1])

	def assign_ability_points(self):

		print ("Primary Ability is: {0} \n The avalible ability scores rolled are:").format(self.character.primary_ability)
		rolled_stats = self.character.generate_character_stats().sort()
		
		for ability in ABILITY_SCORE:
			print rolled_stats
			print 'Assign point for: {0} '.format(ability)
			ability_value = raw_input('> ')

			try:
				if ability_value in rolled_stats:
					self.character.stats[ability.lower()] = ability_value
					rolled_stats.pop(ability_value)
				else:
					raise ValueError
			except ValueError:
				print 'Invalid Value'

		print "Character ability point assigned"

	def save_character(self):
		character_json = json.dumps(self.character)
		file_name = self.character.character_name + "_" + self.character.character_class
		with open(file_name + ".json", "w") as save_file:
			save_file.write(character_json)

		print("Character saved to file {0}").format(file_name)


	def load_character(self, file_name):
		with open(file_name) as save_file:
			self.character = json.load(file_name)

		print("Character loaded from {0}").format(file_name)

	def main(self):
		running = True
		while running:
			if self.character:
				print "Current Character: {0}".format(self.character.character_name)
				pprint(self.character)

			print("Select an option")
			print ("1: Create new character")
			print ("2: Play as character")
			print ("3: Save character")
			print ("4: Load character")
			print ("5: Quit")

			choice = raw_input("> ")

			if choice == 1:
				generate_character()

			elif choice == 2:


			elif choice == 3:
				save_character()

			elif choice == 4:
				dir_path = os.path.dirname(os.path.realpath(__file__))
				file_dict = []

				for file in os.listdir(dir_path):
					if file.endswith(".json"):
						file_dict.append(file)

				file_dict = dict(enumerate(file_dict), start=1)
				pprint (file_dict)

				file_choice = raw_input("> ")

				load_character(file_dict[file_choice])
				 
			elif choice == 5:
				running = False

if __name__ == "__main__":
	character_gen = Character_Gen_Menu()
	character_gen.main()