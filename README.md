# iFood Case Study 🛵🍔

## Overview
Este repositório contém o estudo de caso do iFood, focado em análise de dados de ofertas e previsão de conversões utilizando Machine Learning.

## 📂 Project Structure

ifood_case/
    ├── notebooks/
    │   ├── 1_data_preprocessing.ipynb    
    │   └── 2_modeling.ipynb    
    ├── presentation/        
    ├── src/
    │       ├── __init__.py
    │       ├── data_preprocessing.py   
    │       ├── historical_data_viz.py    
    │       ├── model_evaluate.py               
    │       └── model_train.py         
    ├── data
    │   ├── raw/
    │       ├── profile.json 
    │       ├── transactions.json 
    │   │   └── offers.json        
    │   └── processed/
    │       ├── df_model.parquet
    │       └── df_all.parquet
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
4. Install directory as package:
    ```bash
    pip install -e .
    ```
