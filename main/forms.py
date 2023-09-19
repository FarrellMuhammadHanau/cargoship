from django.forms import ModelForm, ChoiceField
from main.models import Item, Container

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "owner", "type", "amount", "weight", "container", "description"]

    type_choices = [
        ('Consumable', 'Consumable'),
        ('Tools', 'Tools'),
        ('Electronic', 'Electronic'),
        ('Fuel', 'Fuel'),
        ('Valuables', "Valuables")
    ]

    type = ChoiceField(choices=type_choices)

class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = ["name"]