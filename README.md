# iFood Case Study 🛵🍔

## Overview
This project focuses on analyzing offer data and predicting customer conversions using machine learning techniques.  
It involves **preprocessing raw data**, **exploring historical trends**, and **building predictive models** to optimize business outcomes.  

By leveraging **Apache Spark** for large-scale data processing and **Scikit-learn** for model training, the project delivers key insights into **customer behavior**, **offer performance**, and **conversion rates**.  
Final outputs include:
- A unified, clean dataset.
- Visualizations for analysis and reporting.
- A trained model ready for deployment.  

## Project Structure

ifood_case/  
├── notebooks/  
│   ├── 1_data_preprocessing.ipynb      
│   └── 2_modeling.ipynb                 
│  
├── presentation/                        
│  
├── src/                                 
│   ├── __init__.py  
│   ├── data_preprocessing.py            
│   ├── historical_data_viz.py           
│   ├── model_evaluate.py                
│   └── model_train.py                   
│  
├── data/  
│   ├── raw/                             
│   │   ├── profile.json  
│   │   ├── transactions.json  
│   │   └── offers.json  
│   │  
│   └── processed/                       
│       ├── df_model.parquet  
│       └── df_all.parquet  
│  
├── __init__.py  
├── .gitignore                           
├── setup.py                             
├── requirements.txt                     
└── README.md                           

## Installation

1. Clone repository:
    ```bash
    git clone https://github.com/yourusername/poultryhealthpredict.git
    cd poultryhealthpredict
    ```

2. Create virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Install directory as package in editable mode:
    ```bash
    pip install -e .
    ```

## Usage

The project is divided into two main steps, each handled by a separate notebook:

### 1. Data Preprocessing
- **Notebook**: `1_data_preprocessing.ipynb`
- **Technologies**: Apache Spark and Pandas
- **Description**:
  - Clean, preprocess, and prepare the dataset for modeling.
  - Use **Spark** for scalable data operations.
  - Perform **exploratory data analysis (EDA)** using **Pandas** for easy visualization and insights.

### 2. Modeling
- **Notebook**: `2_modeling.ipynb`
- **Technology**: Pandas
- **Description**:
  - Train and evaluate machine learning models (LightGBM).
  - Perform hyperparameter tuning using `RandomizedSearchCV`.
  - Visualize feature importance, confusion matrix, ROC curves, and assess model performance.

---

## Code Overview

| File                     | Description |
|---------------------------|-------------|
| `data_preprocessing.py`   | Cleans, filters, and merges data from the raw sources to create a model-ready dataset. |
| `historical_data_viz.py`  | Generates visualizations to explore customer behavior, offer success, and transaction history. |
| `model_evaluate.py`       | Evaluates model predictions with detailed metrics and visualizations (classification report, confusion matrix, ROC curve). |
| `model_train.py`          | Trains and tunes LightGBM models using a full pipeline (preprocessing + model). |


