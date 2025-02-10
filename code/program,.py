'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

import json
import packaging
packages = []
packages_parsed = []

with open('data/packaging.txt', 'r') as handle:
    for line in handle.readlines():
        packages.append(line.strip())
    for i in packages:
        packages_parsed.append(parse_packaging(packages[i]))
        print(calc_total_units(parse_packaging(packages[i])))
        print(get_unit(parse_packaging(packages[i])))


with open("packages.json", "w") as file:
    json.dump(packages_parsed, file)