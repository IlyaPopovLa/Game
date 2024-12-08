import file_operations
from faker import Faker
import random
import os


fake = Faker("ru_RU")
first_name = fake.first_name()
last_name = fake.last_name()
job = fake.job()
town = fake.city()
strength = random.randint(3, 18)
agility = random.randint(3, 18)
endurance = random.randint(3, 18)
intelligence = random.randint(3, 18)
luck = random.randint(3, 18)

def rep_letters():
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
    skills = random.sample(skills_list, 8)

    skills1 = skills[0]
    skills2 = skills[1]
    skills3 = skills[2]

    letters_maping = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }

    for letters, new_letters in letters_maping.items():
        skills1 = skills1.replace(letters, new_letters)
        skills2 = skills2.replace(letters, new_letters)
        skills3 = skills3.replace(letters, new_letters)

        runic_skills = []
        runic_skills.append(skills1)
        runic_skills.append(skills2)
        runic_skills.append(skills3)

    return rep_letters

context = {
    "first_name": first_name,
    "last_name": last_name,
    "job": job,
    "town": town,
    "strength": strength,
    "agility": agility,
    "endurance": endurance,
    "intelligence": intelligence,
    "luck": luck,
    "skill_1": rep_letters,
    "skill_2": rep_letters,
    "skill_3": rep_letters
}

def save():
    os.makedirs("../test", mode=0o777, exist_ok=True)
    for fname in range(10):
        file_operations.render_template("charsheet.svg", fr"../test/result_{fname}.svg", context)
    return save()

def main():
    rep_letters()
    save()

if __name__ == '__main__':
    main()