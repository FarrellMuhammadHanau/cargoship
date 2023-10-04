from django.forms import ModelForm, ChoiceField
from main.models import Item, Container

class ItemForm(ModelForm):
    def __init__ (self, request, instance=None):
        if (instance is None):
            super().__init__(request.POST or None)
        else:
            
            super().__init__(request.POST or None, instance=instance)
        
        self.fields['container'].queryset = Container.objects.filter(user=request.user)


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