class Player:

    def __init__(self, player_class, user):
        self.player_class = player_class
        user_id = user.id
        self.health = 100
        self.max_health = 100
        self.mana = 100
        self.max_mana = 100
        self.gold = 500
        self.level = 1
        self.experience = 0
        self.max_experience = 100
        self.skill_points = 100
        self.strength = 0
        self.dexterity = 0
        self.agility = 0
        self.magic = 0
        
        if (player_class == 'mage'):
            self.single_target = 7
            self.area_of_effect = 9
            self.defense = 4
            self.speed = 5
        elif (player_class == 'knight'):
            self.single_target = 7
            self.area_of_effect = 3
            self.defense = 9
            self.speed = 6
        elif (player_class == 'rogue'):
            self.single_target = 10
            self.area_of_effect = 3
            self.defense = 2
            self.speed = 10
        elif (player_class == 'archer'):
            self.single_target = 7
            self.area_of_effect = 9
            self.defense = 4
            self.speed = 5

    def level_up(self):
        self.experience -= self.max_experience
        self.max_experience = round( 0.04 * (self.level ^ 3) + 0.8 * (self.level ^ 2) + 2 * self.level)
        level += 1
        self.max_health += 10
        self.health = max_health
        self.skill_points += 2

        if (player_class == 'mage'):
            self.area_of_effect += 1
            if (level % 2 == 0):
                self.single_target += 1
            if (level % 4 == 0):
                self.defense += 1
            if (level % 3 == 0):
                self.speed += 1

        if (player_class == 'knight'):
            self.defense += 1
            if (level % 2 == 0):
                self.single_target += 1
            if (level % 4 == 0):
                self.area_of_effect += 1
            if (level % 2 == 0):
                self.speed += 1

        if (player_class == 'rogue'):
            self.single_target += 1
            self.speed += 1
            if (level % 4 == 0):
                self.area_of_effect += 1
            if (level % 4 == 0):
                self.defense += 1

        if (player_class == 'archer'):
            self.area_of_effect += 1
            if (level % 2 == 0):
                self.single_target += 1
            if (level % 3 == 0):
                self.defense += 1
            if (level % 3 == 0):
                self.speed += 1

    def print_profile(self, username):
        skills = ""
        if (self.skill_points > 0):
            skills = "\nYou have " + str(self.skill_points) + " skill points available!\n"

        output = ("\n```glsl\n========================================\n " + username + "'s profile \n========================================\n"
        + "Level: " + str(self.level) + "\n"
        + "Experience: " + str(self.experience) + "/" + str(self.max_experience) + "\n"
        + "Health: " + str(self.health) + "/" + str(self.max_health) + "\n"
        + "Mana: " + str(self.mana) + "/" + str(self.max_mana) + "\n"
        + "Gold: " + str(self.gold) + "\n"
        + "Single Target Attack: " + str(self.single_target) + "\n"
        + "Area of Effect Attack: " + str(self.area_of_effect) + "\n"
        + "Defense: " + str(self.defense) + "\n"
        + "Speed: " + str(self.speed) + "\n" + skills
        + "To see your skills, type !skills \n"
        + "========================================\n```")
        return output

    def print_skills(self, username):
        
        output = ("\n```glsl\n========================================\n " + username + "'s skills \n========================================\n"
        + "Available skill points: " + str(self.skill_points) + "\n\n"
        + "Strength: " + str(self.strength) + "\n"
        + "Dexterity: " + str(self.dexterity) + "\n"
        + "Agility: " + str(self.agility) + "\n"
        + "Magic: " + str(self.magic) + "\n"
        + "========================================\n```")
        return output

    def add_points(self, skill, amount):
        if int(amount) > self.skill_points:
            return "\n```glsl\nYou don't have that many skill points left!\n```"
        elif int(amount) <= 0:
            return "\n```yaml\nPlease enter a positive integer greater than zero!\n```"
        if skill is "strength":
            self.strength += int(amount)
            self.skill_points -= int(amount)
        elif skill is "dexterity":
            self.dexterity += int(amount)
            self.skill_points -= int(amount)
        elif skill is "agility":
            self.agility += int(amount)
            self.skill_points -= int(amount)
        elif skill is "magic":
            self.magic += int(amount)
            self.skill_points -= int(amount)
        skill[0] = skill[0].upper
        return("\n```glsl\nSuccessfully added " + str(amount) + " points to your " + skill + " skill!\n```")
            
                
        
