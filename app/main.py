class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if person.get("wife") is not None:
            name_spouse = person.get("wife")
            Person.people[person["name"]].wife = Person.people[name_spouse]
        if person.get("husband") is not None:
            name_spouse = person.get("husband")
            Person.people[person["name"]].husband = Person.people[name_spouse]

    return list(Person.people.values())
