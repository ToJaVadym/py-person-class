class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name]= self

def create_person_list(people: list) -> list:
    for p in people:
        Person(p['name'], p['age'])

    result_list = []
    for p in people:
        current_person = Person.people[p['name']]

        spouse_name = p.get('wife') or p.get('husband')

        spouse_name = p.get('wife')
        if spouse_name is None:
            spouse_name = p.get('husband')

        if spouse_name and spouse_name in Person.people:
            attr_name = 'wife' if p.get('wife') is not None else 'husband'
            setattr(current_person, attr_name, Person.people[spouse_name])

        result_list.append(current_person)

    return result_list
