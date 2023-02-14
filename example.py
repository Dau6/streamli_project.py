import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
st.write("Hello world")

data_y=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82, 5.68]
data_x=[10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0,4.0,12.0, 7.0,5.0]


fig, ax=plt.subplots()
ax.scatter(x=data_x, y=data_y, c="#E69F00")
ax.set_xlabel("We should label the x-axis")
ax.set_ylabel("We should label the y axis")
ax.set_title("Some title")

st.pyplot(fig)

data = pd.read_csv('C://Users//DELL//Downloads//gapminder_with_codes.csv')

data_2007 = data[data["year"]==2007]

fig, ax=plt.subplots()
ax.scatter(x=data_2007['gdpPercap'], y=data_2007['lifeExp'], alpha=0.5)
ax.set_xlabel('GDP (USD) per capita')
ax.set_ylabel('life expectancy (years)')

st.pyplot(fig)
