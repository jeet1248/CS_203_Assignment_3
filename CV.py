import json

# Loading the JSON data from the file
with open("CV.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extracting the annotations (labels) from all annotators
annotations = {}

# Iterating through the data and separate annotations by annotator
for entry in data:
    id = entry['id']
    annotator = entry['annotator']
    label = entry['truck_label']
    
    if id not in annotations:
        annotations[id] = {}
    annotations[id][annotator] = label

# Getting unique labels
labels = []
for id, annotation in annotations.items():
    for annotator, label in annotation.items():
        if label not in labels:
            labels.append(label)

# Mapping labels to indices
label_index = {}
for i in range(len(labels)):
    label_index[labels[i]] = i

num_labels = len(labels)
num_items = len(annotations)
num_annotators = 3

# Creating a matrix of counts
matrix = []
for i in range(num_items):
    row = []
    for j in range(num_labels):
        row.append(0)
    matrix.append(row)

index = 0
for id, annotation in annotations.items():
    for annotator, label in annotation.items():
        matrix[index][label_index[label]] += 1
    index += 1

# Calculating observed agreement (Po)
total_annotations = num_items * num_annotators
observed_agreement = 0
for row in matrix:
    for count in row:
        observed_agreement += count * (count - 1)
observed_agreement /= (total_annotations * (num_annotators - 1))

# Calculating expected agreement (Pe)
label_totals = []
for i in range(num_labels):
    label_totals.append(0)

for row in matrix:
    for i in range(num_labels):
        label_totals[i] += row[i]

expected_agreement = 0
for total in label_totals:
    expected_agreement += (total / total_annotations) ** 2

# Calculating Fleiss' Kappa
kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)

# Printing the Fleiss' Kappa score
print(f"Fleiss' Kappa score: {kappa}")