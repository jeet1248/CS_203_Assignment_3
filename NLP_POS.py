import json
from sklearn.metrics import cohen_kappa_score

# Loading the JSON data from the file
with open("NLP_POS.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extracting annotations (labels) from both annotators
annotations_annotator_1 = []
annotations_annotator_2 = []

# Separating annotations by annotator
for i in range(0, len(data), 2):
    for tag in data[i + 1]['pos_tag']:
        annotations_annotator_1.append(tag['labels'][0])
    
    for tag in data[i]['pos_tag']:
        annotations_annotator_2.append(tag['labels'][0])

# Printing the annotations for both annotators
print(annotations_annotator_1)
print(annotations_annotator_2)

# Calculating Cohen's Kappa using sklearn
kappa = cohen_kappa_score(annotations_annotator_1, annotations_annotator_2)

# Printing the Cohen's Kappa score
print(f"Cohen's Kappa score: {kappa}")
