
class Character_Stats:

	def __init__(self):
		self.armor_class = 0
		self.initiative= 0
		self.speed= 0
		self.cur_hit_points= 0
		self.temp_hit_points= 0
		self.max_hit_points= 0
		self.hit_dice= None
		self.death_success= 0
		self.death_fail= 0
		self.proficiency_bonus= 0
		self.strength= 0
		self.dexterity= 0
		self.constitution= 0
		self.intelligence= 0
		self.wisdom=  0
		self.charisma= 0
	      

class Character_Spells:
	def __init__(self):
		self.known= None
		self.slots= None
		self.spell_list= None
		self.prepared_spells= None
		self.casting_ability= 0
		self.save_dc= 0
		self.attack_bonus= 0
