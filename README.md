# Targeted Tastes, an iFood Case Study 🛵🍔

This project delivers actionable insights into customer behavior and offer effectiveness by identifying the best offer to send to each customer, aiming to maximize conversion rates through data-driven strategies.

It preprocesses raw data and explores historical trends to create a unified dataset that combines information about offers, transactions, and customer profiles.  
This enables the development of a predictive model capable of estimating the probability that a given customer will complete an offer they receive.

Key technologies used include:
- **Apache Spark** for large-scale data processing.
- **LightGBM** for building machine learning model.
- **Scikit-learn** for additional model evaluation and utilities.

Final outputs include:
- A clean, structured dataset ready for modeling.
- Visualizations to support analysis and reporting.
- A trained model prepared for deployment.

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
│   ├── impact_evaluate.py          
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
  - Visualize feature importance, confusion matrix, and assess model performance.

---

## Code Overview

| File                     | Description |
|---------------------------|-------------|
| `data_preprocessing.py`   | Cleans, filters, and merges data from the raw sources to create a model-ready dataset. |
| `historical_data_viz.py`  | Generates visualizations to explore customer behavior, offer success, and transaction history. |
| `model_evaluate.py`       | Evaluates model predictions with detailed metrics and visualizations (classification report, confusion matrix). |
| `model_train.py`          | Trains and tunes LightGBM models using a full pipeline (preprocessing + model). |
| `impact_evaluate.py`      | Calculation reference for model's impact, to be used for informational purposes only. |


