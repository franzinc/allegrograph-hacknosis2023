# OpenText H:OPE (Hacknosis: Optimizing Patient Experiences) Challenge
This repository contains an implementation of ... to address the hacknosis challenge posted by OpenText to address patient experience within healthcare ecosystem. The solution is a submission by the franz team in response to the call. Following is the link to the call for submission -

![Hacknosis: Optimizing Patient Experiences](https://hacknosis.hackerearth.com/)

## The Challenge
Gaps in healthcare still exist and the need for better solutions to bridge those gaps is critical. Today, more than half of the world’s population lives one to two hours away from a doctor. The pandemic taught us that telehealth can be a great option. It allows patients and doctors to maintain routine contact and, therefore, good health—but only if the right tools are available. The challenge faced by health providers is how to incorporate new technologies that enable doctors and patients to have real conversations, supported by a simple experience.

### OpenText has identified following challenges
- Integration of healthcare and patient information for doctors
- Embedding accessibility into healthcare solutions
- Transforming Information capture
- Data analysis and presentation in doctor portals
- PHI and PII protection in patient data collection

### Problem statement:
Among the listed challenges, we will be targetting the **Data analysis and presentation in doctor portals** challenge. Following is the description of the challenge:

> Healthcare data lakes pose challenges, one of those being how to effectively manage and analyze unstructured data. This requires advanced techniques for text mining, natural language processing and image recognition to drive meaningful insights from sources such as clinical notes, research articles, medical images and tests.
>
> Data analytics and healthcare services can be combined to address every aspect of patient care and management and unlock new ways of improving healthcare services.
>
> Build a solution to analyze and display data for doctors.

As highlighted in the challenge statement above, we will be targetting the problem of managing and analyzing unstructured data in healthcare.

## The Solution
One of the basic problems with free-text data in health records is extracting medical concept mentions and mapping them to the underlying controlled vocabularies and coding systems for purposes of downstream use such as billing applications to data analytics and other applications. We will be using the ![OpenText Magellan Text Mining Engine](http://magellan-text-mining.opentext.com/) to extract concepts and entities from text as shown in the screenshot below:
![magellan text mining output](/image/text_mining.png "Magellan text mining output")

We can then use a NER (Name Entity Resolution) model to resolve entities to UMLS (Unified Medical Language System) concepts. For this demo, we will be using a UMLS tool to do a lookup of these concepts. The next step is to construct a graph/network based on structured data in patient medical record and also those extracted from the text mining process above. We will be using an "Entity Event Knowledge Graph" (EEKG) model to represent patient data as event entities linked to a patient entity on a graph. The EEKG model simplifies the representation of patient data, facilitates temporal queries and enables a 360 view of patients. Following image shows an EEKG representation for Patient data loaded into AllegroGraph:
![Entity Event Knowledge Graph](/image/EEKG.png "Entity Event Knowledge Graph")


