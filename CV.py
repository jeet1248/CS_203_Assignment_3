import json

# Loading the JSON data from the file
with open("CV.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initializing the count matrix for the two labels: "Truck" and "No Truck"
matrix = [[0, 0] for i in range(len(data))]

# Mapping labels to indices: "Truck" to 0 and  "No Truck" to 1
label_index = {"Truck": 0, "No Truck": 1}

# Populating the matrix with annotation counts
for index in range(len(data)):
    label = data[index]['truck_label']
    matrix[index][label_index[label]] += 1

# Calculating observed agreement (Po)
num_items = len(data)
num_annotators = 3
total_annotations = num_items * num_annotators
observed_agreement = sum(count * (count - 1) for row in matrix for count in row)
observed_agreement /= (total_annotations * (num_annotators - 1))

# Calculating expected agreement (Pe)
label_totals = [sum(row[i] for row in matrix) for i in range(2)] 
expected_agreement = sum((total / total_annotations) ** 2 for total in label_totals)

# Fleiss' Kappa Calculation
kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)

# Printing the Fleiss' Kappa score
print(f"Fleiss' Kappa score: {kappa}")
