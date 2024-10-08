from django.http import HttpResponse
from .factories.factory import ParentFactory, ChildFactory

def home(request):
    return HttpResponse("Welcome to the Family Project!")

def create_family(request):
    parent_factory = ParentFactory()
    child_factory = ChildFactory()

    parent = parent_factory.create_person("John", "Doe", 40)
    child = child_factory.create_person("Jane", "Doe", 10, score=85, level=2)

    parent.child_id = {'id': child.id}
    parent.save()

    child.parent_id = {'id': parent.id}
    child.save()

    return HttpResponse(f"Created family: Parent {parent.first_name} and Child {child.first_name}")
