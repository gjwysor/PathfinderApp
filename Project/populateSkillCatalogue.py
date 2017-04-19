#below is the description of skills from the pathfinder source material. Some properties may be unnecessary or purely cosmetic. Unsure which at this time.
#Skill descriptions adhere to the following guidelines.

#Skill Name: The skill name line includes (in addition to the name of the skill) the following information.
	#Key Ability: The abbreviation of the ability whose modifier applies to the skill check.
	#Trained Only: If this notation is included in the skill name line, you must have at least 1 rank in the skill to use it. If this notation is omitted, the skill can be used untrained (with a rank of 0). If any special notes apply to trained or untrained use, they are covered in the Untrained section (see below).
	#Armor Check Penalty: If this notation is included in the skill name line, an armor check penalty applies (see Equipment) to checks using this skill. If this entry is absent, an armor check penalty does not apply.
#Description: The skill name line is followed by a general description of what using the skill represents.
#Check: What a character ("you" in the skill description) can do with a successful skill check and the check's Difficulty Class (DC). **NOT IMPLEMENTED, Determined by DM and not relevant to calculations**
#Action: The type of action using the skill requires, or the amount of time required for a check. **NOT IMPLEMENTED, Not relevant to calculations**
#Try Again: Any conditions that apply to successive attempts to use the skill successfully. If the skill doesn't allow you to attempt the same task more than once, or if failure carries an inherent penalty (such as with the Climb skill), you can't take 20. If this paragraph is omitted, the skill can be retried without any inherent penalty other than the additional time required.
#Special: Any extra facts that apply to the skill, such as special effects deriving from its use or bonuses that certain characters receive because of class, feat choices, or race.
#Restriction: The full utility of certain skills is restricted to characters of certain classes. This entry indicates whether any such restrictions exist for the skill.
#Untrained: This entry indicates what a character without at least 1 rank in the skill can do with it. If this entry doesn't appear, it means that the skill functions normally for untrained characters (if it can be used untrained) or that an untrained character can't attempt checks with this skill (for skills that are designated "Trained Only").

#skill_name = ndb.StringProperty(required=True) #Name of Skill
#skill_ability = ndb.StringProperty(required=True) #Primary Ability. This is the modifier added to calculate the Skill Check Bonus
#skill_trainedOnly = ndb.BooleanProperty(required=True) #If True, a character must have at least 1 rank in this to use it, so characters with no ranks will not see this skill on their character sheets. If False, it should be populated and Skill Check Bonus should be calculated with rank of 0.
#skill_armorCheckPenalty = ndb.BooleanProperty(required=True) #If true, armor check penalty should be taken into account when calculating Skill Check Bonus
#skill_externalRef = ndb.StringProperty(required=True) #url for external reference with detailed info
#skill_descShort = ndb.StringProperty(required=True) #short general description of what the skill does
#skill_tryAgain = ndb.BooleanProperty(required=True) #If False, some penalty may need to be calculated into Skill Check Bonus. This Property may not be necessary.
#skill_special = ndb.BooleanProperty() #If True, special calculations may be applied
#skill_classRestrict = ndb.BooleanProperty(repeated=True) #If True, this skill is more effective or only used by certain classes.
#skill_untrained = ndb.BooleanProperty(repeated=True) #If True, functions normally if untrained. If False, untrained characters can not use this skill.
#skill_classSkill = ndb.StringProperty(required=True, repeated=True) #Classes for which this is a class skill
#skill_hasSubSkill = ndb.BooleanProperty(required=True, default=False) #If True, skill has a subset of skills included within it.

#Acrobatics
Skill(skill_name='Acrobatics', skill_ability='DEX', skill_trainedOnly=False, skill_armorCheckPenalty=True, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/acrobatics.html#acrobatics', 
	skill_descShort='The Acrobatics skill determines your ability to maintain balance on narrow or treacherous surfaces, as well as evade attacks and maneuver over obstacles.', skill_tryAgain=True, skill_special=True, 
	skill_classRestrict=False, skill_untrained=True, skill_classSkill=['Barbarian', 'Bard', 'Monk', 'Rogue']).put()

#Appraise
Skill(skill_name='Appraise', skill_ability='INT', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/appraise.html#appraise', 
	skill_descShort='The Appraise skill determines your ability to evaluate the value of an object, or identify the most valuable item in a treasure hoard.', skill_tryAgain=False, skill_special=True, 
	skill_classRestrict=False, skill_untrained=True, skill_classSkill=['Bard', 'Cleric', 'Rogue', 'Sorcerer', 'Wizard']).put()
	
#Bluff
Skill(skill_name='Bluff', skill_ability='CHA', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/bluff.html#bluff', 
	skill_descShort='The Bluff skill determines how well you are able to lie or deceive others.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Bard', 'Rogue', 'Sorcerer']).put()
	
#Climb
Skill(skill_name='Climb', skill_ability='STR', skill_trainedOnly=False, skill_armorCheckPenalty=True, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/climb.html#climb', 
	skill_descShort='The Climb skill determines your ability to scale vertical surfaces.', skill_tryAgain=True, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Barbarian', 'Bard', 'Druid', 'Fighter', 'Monk', 'Ranger', 'Rogue']).put()
	
#Craft
Skill(skill_name='Craft', skill_ability='INT', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/craft.html#craft', 
	skill_descShort='The Craft skill determines your ability to create an object from its base materials.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard'], skill_hasSubSkill=True).put()
	
#Diplomacy
Skill(skill_name='Diplomacy', skill_ability='CHA', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/diplomacy.html#diplomacy', 
	skill_descShort='The Diplomacy skill determines your ability to persuade others.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Bard', 'Cleric', 'Paladin', 'Rogue']).put()
	
#Disable Device
Skill(skill_name='Disable Device', skill_ability='DEX', skill_trainedOnly=True, skill_armorCheckPenalty=True, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/disableDevice.html#disable-device', 
	skill_descShort='The Disable Device skill determines your ability to disarm traps and open locks. It also allows you to sabotage simple mechanical devices.', skill_tryAgain=False, 
	skill_special=True, skill_classRestrict=True, skill_untrained=False, skill_classSkill=['Rogue']).put()
	
#Disguise
Skill(skill_name='Disguise', skill_ability='CHA', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/disguise.html#disguise', 
	skill_descShort='The Disguise skill determines your ability to change your appearance.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Bard', 'Rogue']).put()
	
#Escape Artist
Skill(skill_name='Escape Artist', skill_ability='DEX', skill_trainedOnly=False, skill_armorCheckPenalty=True, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/escapeArtist.html#escape-artist', 
	skill_descShort='The Escape Artist skill determines your ability to escape from bonds or grapples.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Bard', 'Monk', 'Rogue']).put()
	
#Fly
Skill(skill_name='Fly', skill_ability='DEX', skill_trainedOnly=False, skill_armorCheckPenalty=True, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/fly.html#fly', 
	skill_descShort='The Fly skill determines your skill at flying, using wings or magic. This skill does not give you the ability to fly.', skill_tryAgain=False, skill_special=True, 
	skill_classRestrict=False, skill_untrained=True, skill_classSkill=['Druid', 'Sorcerer', 'Wizard']).put()
	
#Handle Animal
Skill(skill_name='Handle Animal', skill_ability='CHA', skill_trainedOnly=True, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/handleAnimal.html#handle-animal', 
	skill_descShort='The Handle Animal skill allows you to domesticate animals, as well as train them to follow commands and teach them tricks.', skill_tryAgain=False, skill_special=True, 
	skill_classRestrict=False, skill_untrained=False, skill_classSkill=['Barbarian', 'Druid', 'Fighter', 'Paladin', 'Ranger']).put()

#Heal
Skill(skill_name='Heal', skill_ability='WIS', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/heal.html#heal', 
	skill_descShort='The Heal skill determines your ability to tend to wounds and heal ailments.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, skill_untrained=True, 
	skill_classSkill=['Cleric', 'Druid', 'Paladin', 'Ranger']).put()
	
#Intimidate
Skill(skill_name='Intimidate', skill_ability='CHA', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/intimidate.html#intimidate', 
	skill_descShort='The Intimidate Skill determines your ability to threaten or frighten an opponent into cooperating with you.', skill_tryAgain=False, skill_special=True, skill_classRestrict=False, 
	skill_untrained=True, skill_classSkill=['Barbarian', 'Bard', 'Fighter', 'Monk', 'Ranger', 'Rogue', 'Sorcerer']).put()
	
#Knowledge
Skill(skill_name='Knowledge', skill_ability='INT', skill_trainedOnly=True, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/knowledge.html#knowledge', 
	skill_descShort='The Knowledge skill determines your scholarly expertise on a particular subject matter.', skill_tryAgain=False, skill_special=False, skill_classRestrict=False, skill_untrained=False, 
	skill_classSkill=['Cleric'], skill_hasSubSkill=True).put() #Knowledge subskill classSkill property should exclude cleric as it is included by default
	
#Linguistics
Skill(skill_name='Linguistics', skill_ability='INT', skill_trainedOnly=True, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/linguistics.html#linguistics', 
	skill_descShort='The Linguistics skill determines your aptitude to read, write, and speak other languages. You can decipher nearly any language given enough time, and your ability to write allows you to create and detect forgeries with ease.', 
	skill_tryAgain=True, skill_special=True, skill_classRestrict=False, skill_untrained=False, 
	skill_classSkill=['Bard', 'Cleric', 'Rogue', 'Wizard']).put()
	
#Perception
Skill(skill_name='Perception', skill_ability='WIS', skill_trainedOnly=False, skill_armorCheckPenalty=False, skill_externalRef='http://paizo.com/pathfinderRPG/prd/coreRulebook/skills/perception.html#perception', 
	skill_descShort='The Perception skill determines your ability to notice details around you as well as sense impending danger. This skill includes all five senses, sight, hearing, touch, taste, and smell.',
	skill_tryAgain=True, skill_special=True, skill_classRestrict=False, skill_untrained=True, skill_classSkill=['Barbarian', 'Bard', 'Druid', 'Monk', 'Ranger', 'Rogue']).put()
	
#Perform


Skill(skill_name='', skill_ability='', skill_trainedOnly=, skill_armorCheckPenalty=, skill_externalRef='', 
	skill_descShort='', skill_tryAgain=, skill_special=, skill_classRestrict=, skill_untrained=, 
	skill_classSkill=[]).put()