import random

def pro_skill(change_it):
    skills = ('100% - Бог😇','54% - Ученик📈','2% - Новичок🐾','89% - Мастер⚡')
    for i in range(change_it):
        skillz = random.choice(skills)
    return skillz