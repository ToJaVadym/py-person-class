class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self
        self.spouse = None


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    for p in people_data:
        Person(p['name'], p['age'])

    result_list = []
    for p in people_data:
        current_person = Person.people[p['name']]

        spouse_name = p.get('wife') or p.get('husband')

        if spouse_name and spouse_name in Person.people:
            current_person.spouse = Person.people[spouse_name]

        result_list.append(current_person)

    return result_list
