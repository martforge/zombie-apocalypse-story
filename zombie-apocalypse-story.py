# Zombie Apocalypse
import random

class Survivor:
    def __init__(self, name, occupation, skill):
        self.name = name
        self.occupation = occupation
        self.skill = skill

    def __str__(self):
        return f'{self.name} - {self.occupation} with skill: {self.skill}'

names = [
    "Jin",    # Chinese/Korean (Asia)
    "Aya",    # Japanese (Asia)
    "Ravi",   # Indian (Asia)
    "Zara",   # Arabic (Asia)
    "Liam",   # Irish (Europe)
    "Olivia", # U.S. (North America)
    "Jackson",# U.S. (North America)
    "Emma",   # U.S. (North America)
    "Sofia",  # Spanish (Europe)
    "Kai"     # Hawaiian (North America)
]

occupations_skill = {
    "Doctor": "First Aid",
    "Engineer": "Building",
    "Farmer": "Food Production",
    "Chef": "Cooking",
    "Mechanic": "Vehicle Repair",
    "Soldier": "Combat",
    "Teacher": "Leadership",
    "Hunter": "Tracking",
    "Scavenger": "Resource Gathering",
    "Scientist": "Research"
}

# character creation
def creation(used_names=[]):
    name = random.choice([n for n in name if n not in used_names])
    occupation = random.choice(list(occupations_skill.keys()))
    skill = occupations_skill[occupation]
    survivor = Survivor(name, occupation, skill)
    return survivor

def main():
    num_survivor = 0
    used_names = []
    while num_survivor < 5:
        survivor = creation(used_names)
        print(survivor)
        num_survivor += 1
    #survivors = ''

    #character1 = 
    #character2 = 
    #character3 = 
    #print(survivor)


if __name__ == '__main__':
    main()



