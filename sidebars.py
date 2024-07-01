import os 
import string

categoryList = ['geometry','trigonometry', 'complex_number', 'number_theory'] # Enter category names here (same as )
categoryDct = { category :os.listdir(f'_{category}') for category in categoryList}

result = ""

for key in categoryDct.keys():
    category = " ".join(key.split("_"))
    result += category + ":\n"
    result += f"  - title: {string.capwords(category)}\n{" "*4}children:\n"
    for page in categoryDct[key]:
        with open(f"_{key}/{page}",'r') as f:
            title = f.read().split("title")[1].split("\n")[0].lstrip(": ")
        result += f"{" "*6}- title: {title}\n{" "*8}url: {key}/{page.split(".")[0]}\n"


with open("_data/navigation.yml", "r") as f:
    beforeData = f.read().split("# Sidebars")[0]

with open("_data/navigation.yml", "w") as f:
    f.write(beforeData + "# Sidebars\n" + result)
