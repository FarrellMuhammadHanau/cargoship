from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Cargo1':
        {
            'Item1': 
            {
                'name': 'Tomato',
                'owner': 'Farrell',
                'type': 'Consumable',  
                'ammount': '10',
                'weight': '1.3'
            },
            'Item2':
            {
                'name': 'Spoon',
                'owner': 'Farrell',
                'type': 'Tools',  
                'ammount': '8',
                'weight': '0.8'
            },
            'Item3':
            {
                'name': 'Phone',
                'owner': 'Hanau',
                'type': 'Electronic',
                'ammount': '5',
                'weight': '1'
            }
        },
        'Cargo2':
        {
            'Item1':
            {
                'name': 'Gasoline',
                'owner': 'Unknown',
                'type': 'Flammable',
                'ammount': '2',
                'weight': '5.7'
            },
            'Item2':
                {
                    'name': 'Diesel',
                    'owner': 'Unknown',
                    'type': 'Flammable',
                    'ammount': '3',
                    'weight': '9.6'
                }
        }
    }

    return render (request, 'main.html', context)