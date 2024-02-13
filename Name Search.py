import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import re

setting = True
"""
The list of the most common names from 1923 until 2022 was scraped
from the social security website
(https://www.ssa.gov/oact/babynames/top5names.html) using BeautifulSoup
The table of names was cleaned (all html tags were removed and the names
were assembled into lists based on the gender)
and assembled into the dictionary below
Refer to https://github.com/sportsfanatic1010/MostCommonNames
for the source code for the webscraper
"""
names = {"2022": [["Olivia", "Emma", "Charlotte", "Amelia", "Sophia"], ["Liam", "Noah", "Oliver", "James", "Elijah"]],
"2021": [["Olivia", "Emma", "Charlotte", "Amelia", "Ava"], ["Liam", "Noah", "Oliver", "Elijah", "James"]],
"2020": [["Olivia", "Emma", "Ava", "Charlotte", "Sophia"], ["Liam", "Noah", "Oliver", "Elijah", "William"]],
"2019": [["Olivia", "Emma", "Ava", "Sophia", "Isabella"], ["Liam", "Noah", "Oliver", "William", "Elijah"]],
"2018": [["Emma", "Olivia", "Ava", "Isabella", "Sophia"], ["Liam", "Noah", "William", "James", "Oliver"]],
"2017": [["Emma", "Olivia", "Ava", "Isabella", "Sophia"], ["Liam", "Noah", "William", "James", "Logan"]],
"2016": [["Emma", "Olivia", "Ava", "Sophia", "Isabella"], ["Noah", "Liam", "William", "Mason", "James"]],
"2015": [["Emma", "Olivia", "Sophia", "Ava", "Isabella"], ["Noah", "Liam", "Mason", "Jacob", "William"]],
"2014": [["Emma", "Olivia", "Sophia", "Isabella", "Ava"], ["Noah", "Liam", "Mason", "Jacob", "William"]],
"2013": [["Sophia", "Emma", "Olivia", "Isabella", "Ava"], ["Noah", "Jacob", "Liam", "Mason", "William"]],
"2012": [["Sophia", "Emma", "Isabella", "Olivia", "Ava"], ["Jacob", "Mason", "Ethan", "Noah", "William"]],
"2011": [["Sophia", "Isabella", "Emma", "Olivia", "Ava"], ["Jacob", "Mason", "William", "Jayden", "Noah"]],
"2010": [["Isabella", "Sophia", "Emma", "Olivia", "Ava"], ["Jacob", "Ethan", "Michael", "Jayden", "William"]],
"2009": [["Isabella", "Emma", "Olivia", "Sophia", "Ava"], ["Jacob", "Ethan", "Michael", "Alexander", "William"]],
"2008": [["Emma", "Isabella", "Emily", "Olivia", "Ava"], ["Jacob", "Michael", "Ethan", "Joshua", "Daniel"]],
"2007": [["Emily", "Isabella", "Emma", "Ava", "Madison"], ["Jacob", "Michael", "Ethan", "Joshua", "Daniel"]],
"2006": [["Emily", "Emma", "Madison", "Isabella", "Ava"], ["Jacob", "Michael", "Joshua", "Ethan", "Matthew"]],
"2005": [["Emily", "Emma", "Madison", "Abigail", "Olivia"], ["Jacob", "Michael", "Joshua", "Matthew", "Ethan"]],
"2004": [["Emily", "Emma", "Madison", "Olivia", "Hannah"], ["Jacob", "Michael", "Joshua", "Matthew", "Ethan"]],
"2003": [["Emily", "Emma", "Madison", "Hannah", "Olivia"], ["Jacob", "Michael", "Joshua", "Matthew", "Andrew"]],
"2002": [["Emily", "Madison", "Hannah", "Emma", "Alexis"], ["Jacob", "Michael", "Joshua", "Matthew", "Ethan"]],
"2001": [["Emily", "Madison", "Hannah", "Ashley", "Alexis"], ["Jacob", "Michael", "Matthew", "Joshua", "Christopher"]],
"2000": [["Emily", "Hannah", "Madison", "Ashley", "Sarah"], ["Jacob", "Michael", "Matthew", "Joshua", "Christopher"]],
"1999": [["Emily", "Hannah", "Alexis", "Sarah", "Samantha"], ["Jacob", "Michael", "Matthew", "Joshua", "Nicholas"]],
"1998": [["Emily", "Hannah", "Samantha", "Sarah", "Ashley"], ["Michael", "Jacob", "Matthew", "Joshua", "Christopher"]],
"1997": [["Emily", "Jessica", "Ashley", "Sarah", "Hannah"], ["Michael", "Jacob", "Matthew", "Christopher", "Joshua"]],
"1996": [["Emily", "Jessica", "Ashley", "Sarah", "Samantha"], ["Michael", "Matthew", "Jacob", "Christopher", "Joshua"]],
"1995": [["Jessica", "Ashley", "Emily", "Samantha", "Sarah"], ["Michael", "Matthew", "Christopher", "Jacob", "Joshua"]],
"1994": [["Jessica", "Ashley", "Emily", "Samantha", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "Tyler"]],
"1993": [["Jessica", "Ashley", "Sarah", "Samantha", "Emily"], ["Michael", "Christopher", "Matthew", "Joshua", "Tyler"]],
"1992": [["Ashley", "Jessica", "Amanda", "Brittany", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "Andrew"]],
"1991": [["Ashley", "Jessica", "Brittany", "Amanda", "Samantha"], ["Michael", "Christopher", "Matthew", "Joshua", "Andrew"]],
"1990": [["Jessica", "Ashley", "Brittany", "Amanda", "Samantha"], ["Michael", "Christopher", "Matthew", "Joshua", "Daniel"]],
"1989": [["Jessica", "Ashley", "Brittany", "Amanda", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "David"]],
"1988": [["Jessica", "Ashley", "Amanda", "Sarah", "Jennifer"], ["Michael", "Christopher", "Matthew", "Joshua", "Andrew"]],
"1987": [["Jessica", "Ashley", "Amanda", "Jennifer", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "David"]],
"1986": [["Jessica", "Ashley", "Amanda", "Jennifer", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "David"]],
"1985": [["Jessica", "Ashley", "Jennifer", "Amanda", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "Daniel"]],
"1984": [["Jennifer", "Jessica", "Ashley", "Amanda", "Sarah"], ["Michael", "Christopher", "Matthew", "Joshua", "David"]],
"1983": [["Jennifer", "Jessica", "Amanda", "Ashley", "Sarah"], ["Michael", "Christopher", "Matthew", "David", "Joshua"]],
"1982": [["Jennifer", "Jessica", "Amanda", "Sarah", "Melissa"], ["Michael", "Christopher", "Matthew", "Jason", "David"]],
"1981": [["Jennifer", "Jessica", "Amanda", "Sarah", "Melissa"], ["Michael", "Christopher", "Matthew", "Jason", "David"]],
"1980": [["Jennifer", "Amanda", "Jessica", "Melissa", "Sarah"], ["Michael", "Christopher", "Jason", "David", "James"]],
"1979": [["Jennifer", "Melissa", "Amanda", "Jessica", "Amy"], ["Michael", "Christopher", "Jason", "David", "James"]],
"1978": [["Jennifer", "Melissa", "Jessica", "Amy", "Heather"], ["Michael", "Jason", "Christopher", "David", "James"]],
"1977": [["Jennifer", "Melissa", "Amy", "Jessica", "Heather"], ["Michael", "Jason", "Christopher", "David", "James"]],
"1976": [["Jennifer", "Amy", "Melissa", "Heather", "Angela"], ["Michael", "Jason", "Christopher", "David", "James"]],
"1975": [["Jennifer", "Amy", "Heather", "Melissa", "Angela"], ["Michael", "Jason", "Christopher", "James", "David"]],
"1974": [["Jennifer", "Amy", "Michelle", "Heather", "Angela"], ["Michael", "Jason", "Christopher", "David", "James"]],
"1973": [["Jennifer", "Amy", "Michelle", "Kimberly", "Lisa"], ["Michael", "Christopher", "Jason", "James", "David"]],
"1972": [["Jennifer", "Michelle", "Lisa", "Kimberly", "Amy"], ["Michael", "Christopher", "James", "David", "John"]],
"1971": [["Jennifer", "Michelle", "Lisa", "Kimberly", "Amy"], ["Michael", "James", "David", "John", "Robert"]],
"1970": [["Jennifer", "Lisa", "Kimberly", "Michelle", "Amy"], ["Michael", "James", "David", "John", "Robert"]],
"1969": [["Lisa", "Michelle", "Jennifer", "Kimberly", "Melissa"], ["Michael", "David", "James", "John", "Robert"]],
"1968": [["Lisa", "Michelle", "Kimberly", "Jennifer", "Melissa"], ["Michael", "David", "John", "James", "Robert"]],
"1967": [["Lisa", "Kimberly", "Michelle", "Mary", "Susan"], ["Michael", "David", "James", "John", "Robert"]],
"1966": [["Lisa", "Kimberly", "Mary", "Michelle", "Karen"], ["Michael", "David", "James", "John", "Robert"]],
"1965": [["Lisa", "Mary", "Karen", "Kimberly", "Susan"], ["Michael", "John", "David", "James", "Robert"]],
"1964": [["Lisa", "Mary", "Susan", "Karen", "Patricia"], ["Michael", "John", "David", "James", "Robert"]],
"1963": [["Lisa", "Mary", "Susan", "Karen", "Linda"], ["Michael", "John", "David", "James", "Robert"]],
"1962": [["Lisa", "Mary", "Susan", "Karen", "Linda"], ["Michael", "David", "John", "James", "Robert"]],
"1961": [["Mary", "Lisa", "Susan", "Linda", "Karen"], ["Michael", "David", "John", "James", "Robert"]],
"1960": [["Mary", "Susan", "Linda", "Karen", "Donna"], ["David", "Michael", "James", "John", "Robert"]],
"1959": [["Mary", "Susan", "Linda", "Karen", "Donna"], ["Michael", "David", "James", "John", "Robert"]],
"1958": [["Mary", "Susan", "Linda", "Karen", "Patricia"], ["Michael", "David", "James", "Robert", "John"]],
"1957": [["Mary", "Susan", "Linda", "Debra", "Karen"], ["Michael", "James", "David", "Robert", "John"]],
"1956": [["Mary", "Debra", "Linda", "Deborah", "Susan"], ["Michael", "James", "Robert", "David", "John"]],
"1955": [["Mary", "Deborah", "Linda", "Debra", "Susan"], ["Michael", "David", "James", "Robert", "John"]],
"1954": [["Mary", "Linda", "Deborah", "Patricia", "Susan"], ["Michael", "Robert", "James", "John", "David"]],
"1953": [["Mary", "Linda", "Deborah", "Patricia", "Susan"], ["Robert", "James", "Michael", "John", "David"]],
"1952": [["Linda", "Mary", "Patricia", "Deborah", "Susan"], ["James", "Robert", "John", "Michael", "David"]],
"1951": [["Linda", "Mary", "Patricia", "Deborah", "Barbara"], ["James", "Robert", "John", "Michael", "David"]],
"1950": [["Linda", "Mary", "Patricia", "Barbara", "Susan"], ["James", "Robert", "John", "Michael", "David"]],
"1949": [["Linda", "Mary", "Patricia", "Barbara", "Susan"], ["James", "Robert", "John", "William", "Michael"]],
"1948": [["Linda", "Mary", "Barbara", "Patricia", "Susan"], ["James", "Robert", "John", "William", "David"]],
"1947": [["Linda", "Mary", "Patricia", "Barbara", "Sandra"], ["James", "Robert", "John", "William", "Richard"]],
"1946": [["Mary", "Linda", "Patricia", "Barbara", "Carol"], ["James", "Robert", "John", "William", "Richard"]],
"1945": [["Mary", "Linda", "Barbara", "Patricia", "Carol"], ["James", "Robert", "John", "William", "Richard"]],
"1944": [["Mary", "Barbara", "Linda", "Patricia", "Carol"], ["James", "Robert", "John", "William", "Richard"]],
"1943": [["Mary", "Barbara", "Patricia", "Linda", "Carol"], ["James", "Robert", "John", "William", "Richard"]],
"1942": [["Mary", "Barbara", "Patricia", "Linda", "Carol"], ["James", "Robert", "John", "William", "Richard"]],
"1941": [["Mary", "Barbara", "Patricia", "Carol", "Linda"], ["James", "Robert", "John", "William", "Richard"]],
"1940": [["Mary", "Barbara", "Patricia", "Judith", "Betty"], ["James", "Robert", "John", "William", "Richard"]],
"1939": [["Mary", "Barbara", "Patricia", "Betty", "Shirley"], ["Robert", "James", "John", "William", "Richard"]],
"1938": [["Mary", "Barbara", "Patricia", "Betty", "Shirley"], ["Robert", "James", "John", "William", "Richard"]],
"1937": [["Mary", "Barbara", "Patricia", "Shirley", "Betty"], ["Robert", "James", "John", "William", "Richard"]],
"1936": [["Mary", "Shirley", "Barbara", "Betty", "Patricia"], ["Robert", "James", "John", "William", "Richard"]],
"1935": [["Mary", "Shirley", "Barbara", "Betty", "Patricia"], ["Robert", "James", "John", "William", "Richard"]],
"1934": [["Mary", "Betty", "Barbara", "Shirley", "Dorothy"], ["Robert", "James", "John", "William", "Richard"]],
"1933": [["Mary", "Betty", "Barbara", "Dorothy", "Joan"], ["Robert", "James", "John", "William", "Richard"]],
"1932": [["Mary", "Betty", "Barbara", "Dorothy", "Joan"], ["Robert", "James", "John", "William", "Richard"]],
"1931": [["Mary", "Betty", "Dorothy", "Barbara", "Joan"], ["Robert", "James", "John", "William", "Richard"]],
"1930": [["Mary", "Betty", "Dorothy", "Helen", "Margaret"], ["Robert", "James", "John", "William", "Richard"]],
"1929": [["Mary", "Betty", "Dorothy", "Helen", "Margaret"], ["Robert", "James", "John", "William", "Charles"]],
"1928": [["Mary", "Betty", "Dorothy", "Helen", "Margaret"], ["Robert", "John", "James", "William", "Charles"]],
"1927": [["Mary", "Dorothy", "Betty", "Helen", "Margaret"], ["Robert", "John", "James", "William", "Charles"]],
"1926": [["Mary", "Dorothy", "Betty", "Helen", "Margaret"], ["Robert", "John", "James", "William", "Charles"]],
"1925": [["Mary", "Dorothy", "Betty", "Helen", "Margaret"], ["Robert", "John", "William", "James", "Charles"]],
"1924": [["Mary", "Dorothy", "Helen", "Betty", "Margaret"], ["Robert", "John", "William", "James", "Charles"]],
"1923": [["Mary", "Dorothy", "Helen", "Margaret", "Betty"], ["John", "Robert", "William", "James", "Charles"]]}

# To gather the top 5 names from a specific year via gender:
# use index 0 for females and index 1 for males
# names[year][index]
def nameHistory(name):
    URL = f'https://www.behindthename.com/name/{name}'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    request = requests.get(URL, headers=headers)
    soup = BeautifulSoup(request.content, 'html5lib')

    important = soup.find('div', class_='namedef')
    for data in important(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    entry_list = [name, ' (history)']
    entry = ''.join(entry_list)
    text.delete(1.0, tk.END)
    text.insert(tk.END, ' '.join(important.stripped_strings))
    history.insert('1.0', entry)
    history.insert('1.0', "\n")
    
   



def display_text():
    global entry
    string= entry.get()
    label.configure(text=string)
    if setting == True:
        search_name(string)

    else:
       nameHistory(string)


def search_name(entry):
    found = {}
    positions = {
        0 : "1",
        1 : "2",
        2 : "3",
        3 : "4",
        4 : "5"
        
    }
    for key in names:

        key1 = False
        iteration = 0
        for i in names[key][0]:
            if str(names[key][0][iteration]).lower() == str(entry).lower():
            
                position = positions[iteration]
                found[int(key)] = position  
                iteration2 = 0
                for i in key[1]:
                    if str(names[key][1][iteration2]).lower == str(entry).lower():
                        position = positions[iteration]
                        found[key] += position
                        key1 = True
                    iteration2 += 1
            iteration += 1 
        if not key1:
            iteration = 0
            for i in names[key][1]:
                
                if str(names[key][1][iteration]).lower() == str(entry).lower():
                    position = positions[iteration]
                    found[key] = position
    print("Finished")
    print(found)
    found_str = """Years Found:
    """
    history.insert('1.0', entry)
    history.insert('1.0', "\n")
    if len(found) != 0:
        text.delete(1.0, tk.END)
        for key in found:
            string = f"Found {entry} in position {found[key]} in {key}"
            newline = "\n"           
            text.insert(tk.END, string)
            text.insert(tk.END, newline)
    elif len(found) == 0:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Name Not Found")
        
def switch():

    global setting
    setting = not setting
    update_label()

win = tk.Tk()
win.title("Most Common Names (1923 - 2022)")
width = 800
height = 800
win.geometry(f"{width}x{height}")
label=tk.Label(win, text="Enter a Name", font=("Arial 22"), width=20)
history = tk.Text(win, font="Arial 15", width=15, height=25)


entry= tk.Entry(win, width= 40)

text = tk.Text(win, font=("Arial 15"), width=150, height=20)
text.tag_configure("center", justify='center')
text.tag_add("center", "1.0", "end")


history.place(relx=0.005,
              rely=0.1)
label.pack(pady=5)
entry.pack(padx=5, pady=10)
switch_button = ttk.Button(win, text="Switch", command=switch, width=5)

switch_button.place(relx=0.005,
                    rely=0.0,
                    anchor="nw"
                    

                    )
ttk.Button(win, text= "Search",width= 20, command= display_text).pack(padx=5, pady=15)
text.pack(padx=200)
status = tk.Label(win, text="")
status.place(relx=0.005,
             rely=0.05,
             anchor = "nw"
             )
def update_label():

    if setting == True:
        
        label = """Currently Viewing:
Name Popularity"""
    else:
        label = """Currently Viewing:
Name History"""
    status["text"] = label
    win.after(1000, update_label)
win.after(1, update_label)
win.resizable(False, False)
win.mainloop()
