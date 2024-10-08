from abc import ABC, abstractmethod
from family.models.parent import Parent
from family.models.child import Child

class PersonFactory(ABC):
    @abstractmethod
    def create_person(self, first_name, last_name, age):
        pass

class ParentFactory(PersonFactory):
    def create_person(self, first_name, last_name, age):
        return Parent.objects.create(first_name=first_name, last_name=last_name, age=age)

class ChildFactory(PersonFactory):
    def create_person(self, first_name, last_name, age, score=0, level=1):
        return Child.objects.create(first_name=first_name, last_name=last_name, age=age, score=score, level=level)
