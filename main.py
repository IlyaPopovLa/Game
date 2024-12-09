import file_operations
from faker import Faker
import random
import os

fake = Faker("ru_RU")


def generate_character():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18)
    }


def rep_letters(skills):
    letters_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 'г': 'г͒͠', 'д': 'д̋',
        'е': 'е͠', 'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋', 'и': 'и',
        'й': 'й͒͠', 'к': 'к̋̋', 'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠', 'с': 'с͒', 'т': 'т͒',
        'у': 'у͒͠', 'ф': 'ф̋̋', 'х': 'х͒͠', 'ц': 'ц̋', 'ч': 'ч̋͠',
        'ш': 'ш͒͠', 'щ': 'щ̋', 'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠', 'ю': 'ю̋͠', 'я': 'я̋', ' ': ' ',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠', 'Г': 'Г͒͠', 'Д': 'Д̋',
        'Е': 'Е', 'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋', 'И': 'И',
        'Й': 'Й͒͠', 'К': 'К̋̋', 'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠', 'С': 'С͒', 'Т': 'Т͒',
        'У': 'У͒͠', 'Ф': 'Ф̋̋', 'Х': 'Х͒͠', 'Ц': 'Ц̋', 'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠', 'Щ': 'Щ̋', 'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    }  
    runic_skills = []
    for skill in skills:
        for letters, new_letters in letters_mapping.items():
            skill = skill.replace(letters, new_letters)
        runic_skills.append(skill)
    return runic_skills


def generate_skills():
    skills_list = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]
    return random.sample(skills_list, 3)


def save(context, fname):
    os.makedirs("../test", mode=0o777, exist_ok=True)
    file_operations.render_template("charsheet.svg", fname, context)


def main(): 
    for character in range(10):
        for fname in range(10):
            character = generate_character()
            skills = generate_skills()
            runic_skills = rep_letters(skills)
            character.update({
                "skill_1": runic_skills[0],
                "skill_2": runic_skills[1],
                "skill_3": runic_skills[2],
            })
            fname = fr"../test/result_{fname}.svg"
            save(character, fname)


if __name__ == '__main__':
    main()