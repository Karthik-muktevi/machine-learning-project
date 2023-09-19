# machine-learning-project
Title:Zomato delivery time Prediction

This is a complete end to end machine learning project with modular coding for predicting the food delievery time prediction.

Table of Contents

Overview

Installation

Usage

Project Structure

Modules

Dependencies

License

Overview

Food Delivery services like Zomato and Swiggy need to show the accurate time it will take to deliver your order to keep transparency with their customers. These companies use Machine Learning algorithms to predict the food delivery time based on how much time the delivery partners took for the same distance in the past.

To predict the food delivery time in real-time, we need to calculate the distance between the food preparation point and the point of food consumption. After finding the distance between the restaurant and the delivery locations, we need to find relationships between the time taken by delivery partners to deliver the food in the past for the same distance.

Installation
# Clone the repository
git clone https://github.com/muktevi-karthik/machine-learning-project.git

# Change to the project directory
cd machine-learning-project

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Usage
The application can be executed using the command : streamlit run app.py
--input data/input.csv --output results/output.csv

Project Structure
machine-learning-project/
│
├── .git/
│   └── ... (Git-related files and directories)
│
├── .venv/
│   └── ... (Virtual environment files)
│
├── Artifact/
│   └── ... (Artifact files)
│
├── Data/
│   └── ... (Data files)
│
├── Include/
│   └── ... (Include files)
│
├── Lib/
│   └── ... (Lib files)
│
├── logs/
│   └── ... (Log files)
│
├── Machine_Learning_Project.egg-info/
│   └── ... (Egg info files)
│
├── Prediction/
│   └── ... (Prediction files)
│
├── Scripts/
│   └── ... (Script files)
│
├── src/
│   ├── __pycache__/          # Subfolder for Python cache files
│   │   └── ...
│   │
│   ├── components/           # Subfolder for components code
│   │   └── ...
│   │
│   ├── config/               # Subfolder for configuration code
│   │   └── ...
│   │
│   ├── constants/            # Subfolder for constants code
│   │   └── ...
│   │
│   ├── exception/            # Subfolder for exception code
│   │   └── ...
│   │
│   ├── logger/               # Subfolder for logger code
│   │   └── ...
│   │
│   ├── pipeline/             # Subfolder for pipeline code
│   │   └── ...
│   │
│   ├── utils/                # Subfolder for utility functions
│   │   └── ...
│   │
│   ├── __init__.py
│   ├── delivery_time.ipynb   # Jupyter notebook file
│   └── ...                   
│
├── templates/
│   └── ... (Template files)
│
├── .gitignore
├── app.py
├── exceptions.py
├── LICENSE
├── logs.py
├── predictions.csv
├── pyvenv.cfg
├── README.md
├── requirements.txt
├── setup.py
├── template.py
├── test_data.csv
└── train_data.csv



Modules

Data Extraction 
Data Validation
Data Analysis
Data preparation
Model training
Model evaluation
Model valuation



Dependencies:
requirements.txt

License: Apache 




