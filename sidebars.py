import os 
import string

categoryList = ['geometry', 'complex_number', 'number_theory', 'trigonometry','sequence'] # Enter category names here (same as )
categoryDct = { category :os.listdir(f'_{category}') for category in categoryList}

result = ""

for key in categoryDct.keys():
    groupDct = {}
    for page in categoryDct[key]:
        with open(f"_{key}/{page}", 'r') as f:
            group = f.read().split("group")[1].split("[")[1].split("]")[0]
        if group in groupDct.keys():
            groupDct[group].append(page)
        else:
            groupDct[group] = [page]
    category = " ".join(key.split("_"))
    result += category + ":\n"
    for group in groupDct.keys():
        result += f"  - title: {string.capwords(group)}\n{" "*4}children:\n"
        for page in groupDct[group]:
            with open(f"_{key}/{page}",'r') as f:
                title = f.read().split("title")[1].split("\n")[0].lstrip(": ")
            result += f"{" "*6}- title: {title}\n{" "*8}url: {key}/{page.split(".")[0]}\n"


with open("_data/navigation.yml", "r") as f:
    beforeData = f.read().split("# Sidebars")[0]

with open("_data/navigation.yml", "w") as f:
    f.write(beforeData + "# Sidebars\n" + result)
