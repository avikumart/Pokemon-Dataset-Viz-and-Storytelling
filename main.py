import streamlit as st
import pandas as pd
import plotly.express as px

# read the dataframe
def load_data(path):
    data = pd.read_csv(path, index_col=0)
    return data

data = load_data("Data\pokemon.csv")

# title of the dataviz page
_, col2, _ = st.columns([1, 10, 1])
with col2:
    st.title("Pokémon Species and their Skills")

# description about the Pokemon and add the intro image about any of the pokemon
_, col2, _ = st.columns([1, 5, 1])
with col2:
    st.image("Images\pokemon.jpeg", caption="Pokémon Cartoon Image (source: official website)",
            use_column_width=True)
    # add the header
    st.header("Pokémon Origin and History")
    
st.markdown("""The Pokémon franchise revolves around ***1010 fictional species*** of collectible monsters, 
            each having unique designs, skills and powers. Conceived by ***Satoshi Tajiri*** in early 1989,
            Pokémon (or Pocket Monsters) are fictional creatures that inhabit the fictional Pokémon World. 
            The designs for the multitude of species can draw inspiration from anything such as animals, 
            plants and mythological creatures. Many Pokémon are capable of evolving into more powerful 
            species, while others can undergo form changes and achieve similar results. Originally, 
            only a handful of artists led by ***Ken Sugimori*** designed Pokémon. However, by 2013 a team 
            of 20 artists worked together to create new species designs. ***Sugimori*** and ***Hironobu Yoshida*** 
            lead the team and determine the final designs.""")

# all pokemon images
_, col2, _ = st.columns([1, 4, 1])
with col2:
    st.image("Images\pokemons.jpg", caption="Pokémon Species Image (source: wikipedia)",
            use_column_width=True)

st.markdown("""
            Each Pokémon has one or two "types", such as ***Fire, Water, or Grass.*** 
            In battle, certain types are strong against other types. For example, a Fire-type attack
            will do more damage to a Grass-type Pokémon—rather than a Water-type attack.
            Pokémon's abilities like ***Speed***, ***Attack*** and ***Defense*** are given as a certain points which determines
            their effectiveness. For example, a Fire-type Pokémon's Speed is given as 10, while a Water-type
            Pokémon's Speed is given as 100. Moveover, Their ***Hit points(HP)*** determine how much damage each pokémon can receive before
            fainting. we will explore each Pokémon's skills thorugh interactive vizualization and learn more about 
            Pokémon world! So are excited to to see what's ahead?😃         
            """)


