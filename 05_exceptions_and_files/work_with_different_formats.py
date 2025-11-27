# File formats

# .csv (each comma separates columns) -> ALWAYS with pandas
"""
name,age,city
Daniel,23,Barcelona
Lucía,30,Madrid
Pedro,28,Valencia
"""

# .json (written similar to a Python dictionary) -> if it is nested/complex: WITH OPEN, if it is simple: pandas
"""
[
  {
    "name": "Daniel",
    "age": 23,
    "city": "Barcelona"
  },
  {
    "name": "Lucía",
    "age": 30,
    "city": "Madrid"
  }
]
"""

# .xml (structure with tags, similar to HTML) -> ALWAYS with xml.etree or similar libraries
"""
<people>
    <person>
        <name>Daniel</name>
        <age>23</age>
        <city>Barcelona</city>
    </person>
    <person>
        <name>Lucía</name>
        <age>30</age>
        <city>Madrid</city>
    </person>
    <person>
        <name>Pedro</name>
        <age>28</age>
        <city>Valencia</city>
    </person>
</people>
"""

# Python Libraries

# 1 - Pandas Library
import pandas as pd   # used to easily read files

# Read CSV file using pandas

file = "FileExample.csv"

df = pd.read_csv(file)

df.columns = ["Name", "Phone Number", "Birthday"]  
# rename/add header columns to organize the output


# 2 - with open (for JSON or simple text files)

import json   # import json library to read JSON files

# Open the file "filesample.json" in read mode ("r")
with open("filesample.json", "r") as openfile:
    json_object = json.load(openfile)  # converts JSON content into a Python object (dict/list)

print(json_object)  # prints the converted Python object


# 3 - xml.etree to read XML elements (pandas cannot read XML directly)

import xml.etree.ElementTree as etree   # Library to parse XML
import pandas as pd

tree = etree.parse("fileExample.xml")   # Load and parse the XML file
root = tree.getroot()                   # Get the root element of the XML tree

columns = ["Name", "Phone Number", "Birthday"]   # Define DataFrame columns
df = pd.DataFrame(columns=columns)               # Create empty DataFrame with these columns

for node in root:                                # Iterate through each child element in the XML
    name = node.find("name").text                # read <name>
    phonenumber = node.find("phonenumber").text  # read <phonenumber>
    birthday = node.find("birthday").text        # read <birthday>

    df.loc[len(df)] = [name, phonenumber, birthday]  # Add row to DataFrame

print(df)                                        # Display final DataFrame


# Parsing meaning:
# Converting raw text (JSON, XML, CSV…) into a structure Python can understand
# (dictionary, list, node tree, etc.)

# getroot() → returns the first element of the XML, the parent of all other elements.



