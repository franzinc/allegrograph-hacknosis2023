# OpenText H:OPE (Hacknosis: Optimizing Patient Experiences) Challenge
This repository contains an implementation of solution to address the hacknosis challenge posted by OpenText to address patient experience within healthcare ecosystem. The solution is a submission by the franz team in response to the call. Following is the link to the call for submission -
[Hacknosis: Optimizing Patient Experiences](https://hacknosis.hackerearth.com/)

## OpenText Challenge Topics:
- Integration of healthcare and patient information for doctors
- Embedding accessibility into healthcare solutions
- Transforming Information capture
- Data analysis and presentation in doctor portals
- PHI and PII protection in patient data collection

We will be focusing on **Data analysis and presentation in doctor portals** topic.

## Problem Statement
The U.S. healthcare system's high costs, amounting to 16.9% of GDP and $730.4 billion spent on preventable diseases, make it crucial to reduce unhealthy patients for self-insured healthcare systems. A significant portion of expenses (68%) comes from the top 10% high-cost patients, including readmissions, diabetes, and heart failure cases. However, identifying and intervening with high-cost patients is challenging due to fragmented and complex data systems in healthcare.

Following bullets summarize problems impeding current healthcare solutions:
- Complexity of data model
- Incomplete and Inaccurate data

## The Solution
We will be looking into the problem of predicting patients at high risk for **30-day readmissions** and also **high-cost diabetes patients** with uncontrolled diabetes measurements. Following sections highlight how to address each of the individual problem domain listed above:

### Addressing data complexity
Knowledge Graphs are seen as a solution to this complexity, simplifying thousands of tables and columns into 350 classes and 1,000 attributes. This approach helps data scientists analyze patient data effectively, pinpoint high-cost patients, and enable timely and targeted care. Implementing the Knowledge Graph methodology can save an average-sized hospital system $10 to $20 million annually. Franz's PatientGraph solution is designed to facilitate the adoption of this approach for healthcare organizations, improving care outcomes and reducing costs.

Franz's PatientGraph solution is designed to fast track a healthcare organization's adoption of the Knowledge Graph approach and quickly begin to improve care outcomes and lower costs. We will be using an "Entity Event Knowledge Graph" (EEKG) model to represent patient data as event entities linked to a patient entity on a graph. The EEKG model simplifies the representation of patient data, facilitates temporal queries and enables a 360 view of patients. Following image shows an EEKG representation for Patient data loaded into AllegroGraph:
![Entity Event Knowledge Graph](/image/EEKG.png "Entity Event Knowledge Graph")

The EEKG model makes it easier to query for patient events leading to readmissions and uncontrolled diabetes.

### Addressing incomplete and inaccurate data
More than 70-80% of data in clinical encounters are documented as clinical notes and other free-text fields. In order to extract structured information from unstructured data, we will need to utilize text-mining tools such as the [OpenText Magellan Text Mining Engine](http://magellan-text-mining.opentext.com/) to extract concepts and entities from text as shown in the screenshot below:
![magellan text mining output](/image/text_mining.png "Magellan text mining output")

We can then use a NER (Name Entity Resolution) model to resolve entities to UMLS (Unified Medical Language System) concepts. For this demo, we will be using a UMLS tool to do a lookup of these concepts.
![Biomedical NER](/image/biomedical_ner.png "Biomedical NER")

## Project Setup and Run
The project has dependency on `streamlit` python library to create dashboards. It can be installed using following pip command:

```$> pip install streamlit```

### Data dependencies
The results of query on the EEKG model is persisted as csv files in the repository:

| file                | description                                       |
|---------------------|---------------------------------------------------|
| df_nqf.csv          | cohort of diabetes patients                       |
| diabetes_hier.csv   | hierarcy of diabetes concepts in UMLS             |
| predict_readmit.csv | ranked list of high-risk patients for readmission |
| readmit_df.csv      | patients with readmissions                        |

### Cloning the repository
You will need to get started by cloning this repostory:
```
$> git clone https://github.com/franzinc/allegrograph-hacknosis2023.git
$> cd allegrograph-hacknosis2023
```

### Running the nqf0059 diabetes dashboard
You can run the following streamlit command to view the dashboard:
```
$> streamlit run nqf0059_dash.py
```
![NQF0059 dashboard](/image/nqf_dashboard.png "NQF0059 diabetes quality metric dashboard")

### Running the readmissions dashboard
You can run the following streamlit command to view the readmissions dashboard:
```
$> streamlit run readmit_dash.py
```
![readmission dashboard](/image/readmission_dash.png "30 day readmission dashboard")
