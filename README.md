# **Rasa Driven Movie Recommendation Chatbot & Facial Emotion Detection**

## Overview
This project is divided into two parts:
- Part A: Development of a level 2/3 conversational movie recommendation chatbot using Rasa, with datasets, intents, and actions
- Part B: Development of a facial emotion detection system using the FER-2013 dataset

## Project Objectives
- Build, train, and evaluate a conversational AI chatbot using the Rasa framework.
- Develop a facial emotion detection model to classify emotions into categories using deep learning.
- Analyze, design, and present solutions with appropriate diagrams and metrics.

## Part A: Movie Recommendation Chatbot
### Description
The chatbot aims to provide intelligent conversational capabilities for providing movie recommendations to the user based on their request.
### Key Features
- Custom intents, entities, and actions for the problem domain.
- Training and validation using a custom dataset.
- Designed with UML diagrams (use case, sequence, and activity diagrams).
- Evaluation using metrics such as accuracy and F1-score.
### Technologies Used
- Framework: Rasa
- Programming Language: Python
- Tools: NLU, Rasa core
### Setup & Usage
```
# Clone the repository
git clone [repository link]

# Navigate to the project directory
cd chatbot

# Install required dependencies
pip install -r requirements.txt

# Train the Rasa model
rasa train

# Start the chatbot
rasa run actions & rasa shell
``` 

## Part B: Facial Emotion Detection
### Descripton
The emotion detection system uses the FER-2013 dataset to clasify the emotions into distinct categories and is trained using deep learning.
### Key Features
- Image processing using the FER-2013 dataset converted to PNG format.
- Emotion classification.
- Evaluation using Precision, Recall, and F-measure.
### Technologies 
- Framework: Opencv
- Programming Language: Python
- Dataset: FER-2013
### Setup & Usage
```
# Clone the repository
git clone [repository link]

# Navigate to the project directory
cd facial-emotion-detection

# Install required dependencies
pip install -r requirements.txt

# Convert FER-2013 CSV to PNG format
python convert_dataset.py

# Train the model
python train_model.py

# Test the model
python test_model.py
```

## Results & Evaluation
### Part A: Rasa Chatbot
Evaluation Metrics: 
- Accuracy- 
- F1-score- 
- Confusion matrix-
Screenshots/Diagrams: [Add dialog flow, training results, etc.]
### Part B: Facial Emotion Detection
Evaluation Metrics: 
- Precision- 
- Recall- 
- F-measure for each emotion category-
Screenshots/Diagrams: [Add confusion matrix, loss/accuracy graphs, etc.]

## References
FER-2013 Dataset: [Link]
Rasa Documentation: [Link]
