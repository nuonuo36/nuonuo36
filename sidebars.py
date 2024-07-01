import os 

categoryList = ['geometry','trigonometry']
categoryDct = {f'_{category}':os.listdir(f'_{category}') for category in categoryList}

result = ""

for key in categoryDct.keys():
    result += key.strip('_')
    result += "\t-title: {}"
    for page in categoryDct[key]:




