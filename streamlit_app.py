import streamlit
streamlit.title("my Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites') 
streamlit.text('🥣 Omega 3 & blueberry otatmeal')
streamlit.text('🥗Kale Spinach and rocket smoothy')
streamlit.text('🐔hard-boiled free-range egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")

# what does the next line do? 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# what does this do?
streamlit.dataframe(fruityvice_normalized)

