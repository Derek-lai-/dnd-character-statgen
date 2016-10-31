class Character_Play:

	ABILITY_SCORE = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

	def __init__(self, character):
		self.character = character

	def update_character_hp(self):
		print("Enter new Hit Point value \n")
		character_hp = raw_input("> ")

		self.character.stats.cur_hit_points = character_hp
		print ("Character now has {0} Hit points \n").format(self.character.stats.cur_hit_points)

	def character_level_up(self):
		print("Enter new level\n")
		character_lvl = raw_input("> ")

		self.character.level = character_lvl
		print ("Character now level {0} \n").format(self.character.level)

	def cast_spell(self):
		if self.character.spells.slots:
			

	def show_character_options():
		using_character = True

		if !self.character:
				print("No Character has been chosen to use")
				using_character = False

		while using_character:
			
			print ("Current Character:\n")
			pprint(self.character)

			print("Select an option")
			print ("1: Update Hit Points")
			print ("2: Update Character Level")
			print ("3: Cast Spell")
			print ("4: Learn New Spell")
			print ("5: Update Prepared Spells")
			print ("6: ")
			print ("7: Quit")

			if choice == 1:
				update_character_hp()
			elif choice == 2:
				character_level_up()
			elif choice == 3:
				cast_spell()
			elif choice == 4:
			elif choice == 5:
			elif choice == 6:
			elif choice == 7:
				using_character = False
