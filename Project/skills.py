# Skill NBD Model Class
import logging
from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel

class Skill(polymodel.PolyModel):
    	skill_name = ndb.StringProperty(required=True) #Name of Skill
	skill_ability = ndb.StringProperty(required=True) #Primary Ability. This is the modifier added to calculate the Skill Check Bonus
	skill_trainedOnly = ndb.BooleanProperty(required=True) #If True, a character must have at least 1 rank in this to use it, so characters with no ranks will not see this skill on their character sheets. If False, it should be populated and Skill Check Bonus should be calculated with rank of 0.
	skill_armorCheckPenalty = ndb.BooleanProperty(required=True) #If true, armor check penalty should be taken into account when calculating Skill Check Bonus
	skill_externalRef = ndb.StringProperty(required=True) #url for external reference with detailed info
	skill_descShort = ndb.StringProperty(required=True) #short general description of what the skill does
	skill_tryAgain = ndb.BooleanProperty(required=True) #If False, some penalty may need to be calculated into Skill Check Bonus. This Property may not be necessary.
	skill_special = ndb.BooleanProperty(required=True) #If True, special calculations may be applied
	skill_classRestrict = ndb.BooleanProperty(required=True) #If True, this skill is more effective or only used by certain classes.
	skill_untrained = ndb.BooleanProperty(repeated=True) #If True, functions normally if untrained. If False, untrained characters can not use this skill.
	skill_classSkill = ndb.StringProperty(required=True, repeated=True) #Classes for which this is a class skill
	skill_hasSubSkill = ndb.BooleanProperty(required=True, default=False) #If True, skill has a subset of skills included within it.

#sub class for skills that fall under an umbrella skill
class subSkill(Skill):
	parentSkill = ndb.KeyProperty(kind=Skill, required=True) #Key of the skill the subskill belongs to

	
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
