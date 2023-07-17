import streamlit as st
import pandas as pd
import plotly.express as px

# read the dataframe
def load_data(path):
    data = pd.read_csv(path, index_col=0)
    return data

# dataset path
path = 'Data/pokemon.csv'
data = load_data(path)

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
    st.image("Images\pokemons.jpg", caption="Pokémon Species Image (source: Wikipedia)",
            use_column_width=True)

st.markdown("""
            Each Pokémon has one or two "types", such as ***Fire, Water, or Grass.*** 
            In battle, certain types are strong against other types. For example, a Fire-type attack
            will do more damage to a Grass-type Pokémon—rather than a Water-type attack.
            Pokémon's abilities/attributes like ***Speed***, ***Attack***, and ***Defense*** are given as certain points which determines
            their effectiveness. For example, a Fire-type Pokémon's Speed is given as 10, while a Water-type
            Pokémon's Speed is given as 100. Moreover, Their ***Hit points(HP)*** determine how much damage each pokémon can receive before
            fainting. we will explore each Pokémon's skills through interactive visualization and learn more about 
            Pokémon world! So are you excited to see what's ahead?😃         
            """)

# add the vizes here by columns
_, col2, _ = st.columns([1, 6, 1])
with col2:
    st.subheader("What are the types and skill scores of your favourite Pokémon?")
    options = data['Names']
    selection = st.selectbox("Try entering some of names from below list",options=options)
    def pokemon_skills(df, name):
        cat_val = list(df[df['Names'] == name][['image_url','Type1','Type2']].values[0])
        num_val = list(df[df['Names'] == name][['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']].values[0])
        ps_df = pd.DataFrame({'Metric':['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'],
                    'Points':num_val})
        
        fig = px.bar(ps_df, x=ps_df['Metric'], y=ps_df['Points'], color=ps_df['Points'], 
                labels={'color':'Points level'}, height=400)
        
        # update the layout
        fig.update_layout(title=f'Skill levels of Pokemon {name}',
                                xaxis_title='Skills',
                            yaxis_title='Points level',
                            title_font_family="Sitka Small",
                            title_font_color="Black",
                            title_font_size=22,
                            xaxis_title_font_color='black',
                            xaxis_title_font_size=17,
                            yaxis_title_font_color='black',
                            yaxis_title_font_size=17
                            )
        return cat_val, fig
    
    # display the plotly chart
    cats, fig = pokemon_skills(data, selection)
    st.plotly_chart(fig,use_container_width=True)
    
# expander with explnation or image and other infor on viz output
    with st.expander(f"See the image of {selection}"):
        url = cats[0]
        type1 = cats[1]
        type2 = cats[2]
        st.write(f"Pokémon types are {type1} and {type1}")
        st.image(url, caption=selection)


# chart 2 viz
_, col2, _ = st.columns([1, 6, 1])
with col2:
    st.subheader("What is the distribution of each skill attribute?")
    selection2 = st.selectbox("Enter any of these skills",
                            options=('HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'))
    def dist_plt(df, skill):
        # Create the distribution plot using Plotly
        fig = px.histogram(df,x=skill,
                    nbins=30, marginal='rug', 
                    labels={'value': skill})
                
        # update the layout
        fig.update_layout(title=f'Distribution of {skill}',
                        xaxis_title=skill,
                        yaxis_title='Count',
                        title_font_family="Sitka Small",
                        title_font_color="Black",
                        title_font_size=22,
                        xaxis_title_font_color='black',
                        xaxis_title_font_size=17,
                        yaxis_title_font_color='black',
                        yaxis_title_font_size=17
                        )
        return fig
    
    # display the chart 2
    fig = dist_plt(data, selection2)
    st.plotly_chart(fig,use_container_width=True)
    
    with st.expander(f"Learn about the {selection2}"):
        if selection2 == 'HP':
            st.text("""Hit Points (HP) represent a Pokémon's health or stamina. It is a metric 
that indicates how much damage a Pokémon can sustain before it faints or
becomes unable to battle. HP serves as an important aspect of gameplay as it
determines a Pokémon's overall durability and ability to withstand attacks.""")
        elif selection2 == 'Attack':
            st.text("""Attack (often referred to as "ATK") is a metric that measures a Pokémon's 
physical offensive power. It determines the damage dealt with by physical moves, 
such as using physical attacks like Tackle or Scratch. A higher Attack stat means 
the Pokémon will inflict more damage with physical moves.""")
        elif selection2 == 'Defense':
            st.text("""Defense (often referred to as "DEF") is a metric that measures a Pokémon's physical 
defensive capabilities. It determines how well a Pokémon can resist and mitigate
damage from physical moves used by opponents. A higher Defense stat means the Pokémon
can withstand physical attacks more effectively.""")
        elif selection2 == 'Sp. Atk':
            st.text("""Special Attack (often referred to as "Sp. Atk" or "SATK") is a metric that measures 
a Pokémon's special offensive power. It determines the damage dealt by special moves, 
such as using elemental attacks like Flamethrower or Thunderbolt. A higher Special 
Attack stat means the Pokémon will inflict more damage with special moves.""")
        elif selection2 == 'Sp. Def':
            st.text("""Special Defense (often referred to as "Sp. Def" or "SDEF") is a metric that measures 
a Pokémon's special defensive capabilities. It determines how well a Pokémon can 
resist and mitigate damage from special moves used by opponents. A higher Special
Defense stat means the Pokémon can withstand special attacks more effectively.
                    """)
        else:
            st.text("""Speed is a metric that measures a Pokémon's speed or agility in battles. 
It determines the order in which Pokémon and their moves are executed during a battle.
A higher Speed stat means the Pokémon will generally act before Pokémon with a lower
Speed stats. Speed can impact the ability to attack first, dodge the opponent's moves, 
and utilize certain moves that depend on speed, such as Quick Attack or Agility.
                    """)
            
# chart 3 viz
_, col2, _ = st.columns([1, 6, 1])
with col2:
    st.subheader("What is the relationship between Attack and Defense skill attributes?")
    # plot the scatter plot func
    def scatter(df):
        fig = px.scatter(df, x="Attack", y="Defense",
                    size='Total', hover_data=['Names','Type1'])
        
        # update the layout 
        fig.update_layout(title='Pokémon Species: Defense w.r.t to Attack',
                xaxis_title='Attack',
                yaxis_title='Defense',
                title_font_family="Sitka Small",
                title_font_color="Black",
                title_font_size=22,
                xaxis_title_font_color='black',
                xaxis_title_font_size=17,
                yaxis_title_font_color='black',
                yaxis_title_font_size=17
        )
        return fig
    
    # display the chart 3
    fig = scatter(data)
    st.plotly_chart(fig,use_container_width=True)
    
    with st.expander(f"See the explanation"):
        st.text("""We can see that attack and defense are highly correlated with other which 
shows that any Pokémon who's having higher attacking capacity has higher defense
capacity in general.
                """)
    
# chart 4 viz
_, col2, _ = st.columns([1, 6, 1])
with col2:
    st.subheader("Who are the best 10 Pokémons in each skill attribute?")
    selection3 = st.selectbox("Enter any of these skills",
                            options=('HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'),
                            key='Speed')
    
    def top10(df, skill):
        Top10 = df.sort_values(by=skill,ascending=False)[:10]
        
        # plot the bar chart
        fig = px.bar(Top10, x='Names', y=skill,
                hover_data=['Type1', 'Total'], color=skill,
                labels={'legend':skill}, height=500)
        # update the layout
        fig.update_layout(title=f'Pokémon Species: Top 10 in {skill} points',
                    xaxis_title='Name of Pokémons',
                    title_font_family="Sitka Small",
                    title_font_color="Black",
                    title_font_size=22,
                    xaxis_title_font_color='black',
                    xaxis_title_font_size=17,
                    yaxis_title_font_color='black',
                    yaxis_title_font_size=17
                    )
        return Top10, fig
    
    # display the fig
    topdf, fig = top10(data, selection3)
    st.plotly_chart(fig, use_container_width=True)
    
    # visualize the images of top10
    with st.expander(f"See the images of top 10 Pokémons"):
        st.write(f"Top 10 in {selection3} points")
        for i in range(10):
            url = topdf.iloc[i,0]
            #type1 = topdf.iloc[i,3]
            #type2 = topdf.iloc[i,4]
            st.image(url, caption=topdf.iloc[i,2]) 
            # yeee! ballooons!!!
            st.balloons()
