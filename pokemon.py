import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
import random
from PIL import Image
st.title("Pokemon Explorer!")


def get_random_pokemon():
    poke_number = random.randint(1, 151)  # Generate a random Pokemon number between 1 and 150
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
    response = requests.get(url)
    pokemon = response.json()
    return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites'], pokemon['cries']

def get_details(poke_number):
	try:
		url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
		response = requests.get(url)
		pokemon = response.json()
		return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), pokemon['sprites'], pokemon['cries']
	except:
		return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, npNAN
	

pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=150
						   )

name, height, weight, moves, images, sound= get_details(pokemon_number)
if st.button('Show Random Pokemon'):
    name, height, weight, moves, images, sound = get_random_pokemon()
height = height*10
height_data=pd.DataFrame({'Pokemon': ['Weedle', name, 'victreebel'], 'Heights': [3, height, 17]})


graph = sns.barplot(data = height_data,
				   x= 'Pokemon',
				   y = 'Heights',
				   palette = colours)
st.write(f'Name: {name}')
st.write(f'Height: {height}')
st.write(f'Weight: {weight}')
st.write(f'Move Count: {moves}')
st.image(images['other']['home']['front_default'])
st.audio(sound['latest'], format='audio/ogg')
st.pyplot(graph.figure)
