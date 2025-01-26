# CS 203 Assignment-3

**Team Members:**  
- Jeet Joshi (23110148)
- Kain Harshil Shivkumar (23110151) 

---

### Task 1: Environment Setup

#### Steps Taken:

1. **Clearing Terminal History:**  
   We used a command to clear the terminal history, ensuring no record of previous commands.

2. **Checking Python Installation:**  
   We verified if Python 3.10 was installed on our system

3. **Installing Python 3.10:**  
   Python 3.10 was downloaded and installed using the tarball method

4. **Setting Up Python Virtual Environment:**  
   A virtual environment was created with the newly installed Python 3.10.

5. **Installing Label Studio:**  
   After setting up the environment, we installed Label Studio for dataset annotation.

6. **Running Label Studio:**  
   After installation, we successfully launched Label Studio and accessed it through a browser

7. **Saving Terminal History:**  
   We saved the terminal history in a text file and uploaded it to the repository.

---

### Task 2: Annotating a Dataset Using Label Studio

#### Datasets Annotated:

- **NLP Dataset:**  
  We performed Part-of-Speech (POS) Tagging for the Hindi-English dataset. The POS tags used for annotation included categories such as NOUN, PROPN, VERB, ADJ, ADV, ADP, PRON, DET, CONJ, PART, PRON_WH, PART_NEG, NUM and X.

- **CV Dataset:**  
  We annotated the Computer Vision (CV) dataset with labels indicating whether or not the images contained trucks (Truck, No Truck).

#### Annotation Process:
- Each member annotated 20 data points from POS and CV datasets, and thus, in total, 40 data points.
- For the CV dataset, we also received help from Team 4 member Anuj Joshi (23110033) to label 20 data points, thus adding to 60 for the CV labelling task.

---

### Task 3: Inter-Annotator Agreement (IAA) Calculation

#### Data Export:
We exported the labelled data for both datasets in JSON format so that the kappas could be calculated.

#### Cohen's Kappa (NLP Dataset):  
We used Cohen's Kappa to measure the agreement between the two annotators on the NLP dataset.

- **Cohen's Kappa Score for NLP Dataset:** **0.784**

**Interpretation:**  
A Kappa score of **0.784** indicates good agreement between the two annotators on the NLP task, a positive indicator of reasonable consistency in the POS tagging annotations. The disagreement could be due to bias, basic human mistakes or interpretation errors, and ambiguity in understanding.

#### Fleiss' Kappa (CV Dataset):  
For the CV dataset, we used Fleiss' Kappa, which is used to calculate agreement among three or more annotators. We used the annotations from our team and a third set of annotations from a different team member.

- **Fleiss' Kappa Score for CV Dataset:** **1**

**Interpretation:**  
A Kappa score of **1** represents a perfect agreement among the annotators, suggesting that the annotators were entirely in accordance in labelling the images of containing trucks. It could be because the identification of trucks was way too easy due to various zoom features in the label studio itself, and there was no ambiguity.

---

### Conclusion:
- **Cohen's Kappa for the NLP dataset** reveals good agreement (0.784) between the two annotators, suggesting good consistency in the POS tagging task.
- **Fleiss' Kappa for the CV dataset** shows perfect agreement (1) across all three annotators, indicating a high level of consistency in the truck classification task.

---

### Instructions for Running the Code:

1. **Clone the repository:**
   Clone the repository to your local machine using the GitHub account URL `https://github.com/jeet1248/CS_203_Assignment_3.git`.

2. **Install dependencies as needed:**
   Navigate to the cloned directory and install the required dependencies (such as `sklearn`, `json`, etc.).

3. **Run the Code:**
   Execute the appropriate Python scripts to calculate Cohen's and Fleiss' Kappa.
   
4. **View the Results:**
   After running the scripts, check the terminal for Cohen's Kappa and Fleiss' Kappa output.

