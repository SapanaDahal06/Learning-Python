import random
def simple_reflex_agent():
    environment = {
        'A':random.choice(['clean','Dirty']),
        'B':random.choice(['Clean','Dirty'])
        
    }
    vacumm_location = random.choice('A','B')
    print('Initial Environment:',environment)
    print('Vacume starts at Room',vacumm_location)
    print("---------------------------------")
    for step in range (4):
        print(f"\n Step {step + 1}")
        if environment [vacumm_location]=='Dirty':
            print(f"Room{vacumm_location}is Dirty-> Vacum clean")
            environment[vacumm_location]= 'Clean'
        else:
            print(f"Room {vacumm_location} is already clean'-Vacum Move ")
            if vacumm_location =="A":
                vacumm_location = "B"
            else:
                vacumm_location = "A"


    print("\n-----------------------------------")
    print("Final Environment:",environment)
    print("Cleanning Complete!")
simple_reflex_agent()

                
        