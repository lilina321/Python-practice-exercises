import requests
import webbrowser

selectedAnimal = input('Please choose an animal: (cat or dog) ')

params = {
    'animal_type' : selectedAnimal
    }

response = requests.get('https://cat-fact.herokuapp.com/facts/random/', params)

fact = response.json()['text']

def display_selected_animal_and_fact(selectedAnimal):
    if selectedAnimal == 'cat':
        print(fact)
        response2 = requests.get('https://aws.random.cat/meow')
        randomCat = response2.json()['file']
        webbrowser.open_new_tab(randomCat)

    elif selectedAnimal == 'dog':
        print(fact)
        response2 = requests.get('https://random.dog/woof.json')
        randomDog = response2.json()['url']
        webbrowser.open_new_tab(randomDog)
    

display_selected_animal_and_fact(selectedAnimal)
