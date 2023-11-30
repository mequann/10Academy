import panda as pd;
import streamlit as st
import plotly.express as px

import json

# Specify the path to your JSON file
json_file_path = 'I:/10Academy/data/channels.json'

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    print(data)

# Now, 'data' contains the Python representation of the JSON content
#print(data)def load_data():
    """function to loada data"""
   # df=pd.read_scv()