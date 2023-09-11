from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Cargo1':
        {
            'Goods1': 
            {
                'name': 'Tomato',
                'owner': 'Farrell',
                'type': 'Consumable',  
                'ammount': '10',
                'weight': '1.3'
            },
            'Goods2':
            {
                'name': 'Spoon',
                'owner': 'Farrell',
                'type': 'Tools',  
                'ammount': '8',
                'weight': '0.8'
            },
            'Goods3':
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
            'Goods1':
            {
                'name': 'Gasoline',
                'owner': 'Unknown',
                'type': 'Flamable',
                'ammount': '2',
                'weight': '5.7'
            },
            'Goods2':
                {
                    'name': 'Diesel',
                    'owner': 'Unknown',
                    'type': 'Flamable',
                    'ammount': '3',
                    'weight': '9.6'
                }
        }
    }

    return render (request, 'main.html', context)