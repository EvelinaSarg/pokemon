import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
st.title("Pokemon Explorer!")

def get_details(poke_number):
	try:
		url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
		response = requests.get(url)
		pokemon = response.json()
		return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves'])
	except:
		return 'Error', np.NAN, np.NAN, np.NAN
	

pokemon_number = st.slider("Pick a pokemon",
						   min_value=1,
						   max_value=150
						   )
name, height, weight, moves= get_details(pokemon_number)
height = height*10
height_data=pd.DataFrame({'Pokemon': ['Weedle', name, 'victreebel'], 'Heights': [3, height, 17]})
colours=['grey', 'blue', 'red']

graph = sns.barplot(data = height_data,
				   x= 'Pokemon',
				   y = 'Heights',
				   palette = colours)

st.write(f'Name: {name}')
st.write(f'Height: {height}')
st.write(f'Weight: {weight}')
st.write(f'Move Count: {moves}')
st.pyplot(graph.figure)
