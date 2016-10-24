from character import character

class start_charater_gen:

	ABILITY_SCORE = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
	CLASSES = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Palidin', 'Ranger', 'Rouge', 'Sorcere', 'Warlock', 'Wiard']
	RACES = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']

	def generate_character():
		new_character = character()
		pick_character_race(new_character)
		pick_character_class(new_character)
		assign_ability_points(new_character)


	def pick_character_race(character):
		print ("Select a character race:\n")

		for race_index in range(len(RACES)):
			print '$1: $2 \n'.format(race_index, RACES[race_index]) 

		choice_race = raw_input('> ')
		character.choose_class(CLASSES[choice_race - 1])

	def pick_character_class(character):
		print ("Select a class: \n")

		for class_index in range(len(CLASSES)):
			print '$1: $2 \n'.format(class_index, CLASSES[class_index])

		choice_class = raw_input('> ')
		character.choose_class(CLASSES[choice_class - 1])

	def assign_ability_points(character):

		print ("Primary Ability is: $1 \n The avalible ability scores rolled are:").format(character.primary_ability)
		rolled_stats = character.generate_character_stats().sort()
		
		for ability in ABILITY_SCORE:
			print rolled_stats
			print 'Assign point for: $1 '.format(ability)
			ability_value = raw_input('> ')

			try:
				if ability_value in rolled_stats:
					character.stats[ability.lower()] = ability_value
					rolled_stats.pop(ability_value)
				else:
					raise ValueError:
			except ValueError:
				print 'invalid value'

		print "Character ability point assigned"
			