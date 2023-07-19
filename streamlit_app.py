import streamlit
import pandas





streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruits_to_show)

# Display the table on the page.

# New section to display Fruity Advice
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#   streamlit.text(fruityvice_response.json())

# takes the json version and normilzes it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as a table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_row)

fruit_add = streamlit.text_input('What fruit would you like to add?')
my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur1 = my_cnx1.cursor()
my_cur1.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('" + fruit_add + "')")
my_data_row= my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_row)








   
