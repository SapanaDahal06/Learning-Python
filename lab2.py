import random
def model_based_reflex_agent():
    environment = {
        'A':random.choice(['Clean','Dirty']),
        'B':random.choice(['Clean','Dirty']),
        
    }
    vacum_location = random.choice(['A','B'])
    model = {'A':'Unknown','B':'Unknown'}
    print('Initial Environment:' environment)
    print('Vacum starts as Room',vacum_location)
    print('-------------------------------------')
    for steps in range(4):
        print(f'\n Step(step + 1)')
        print('Current Location',vacum_location)
        print('Preived Room State',environment[vacum_location])
        model[vacum_location]= environment[vacum_location]
        if environment[vacum_location]=='Dirty':
        print(f'\Room'{vacum_location}is Dirty -> vacum clean)
        model[vacum_location]= 'Clean'
    else:
        print(f'Room{vacum_location}is already Clean -> Deside next Move')
      if model ['A'] == Clean