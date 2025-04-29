from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import lightgbm as lgb
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self, df_modelo, categorical_cols, numerical_cols, target):
        self.df_modelo = df_modelo
        self.categorical_cols = categorical_cols
        self.numerical_cols = numerical_cols
        self.target = target

    def train(self):
        X_train, X_test, y_train, y_test = self.__prepare_data()
        pipeline = self.__create_pipeline()
        random_search = self.__tune_model(pipeline, X_train, y_train)  
        return random_search, X_test, y_test


    def get_best_params(self,random_search):
        return random_search.best_params_

    def get_best_score(self,random_search):
        return random_search.best_score_

    def predict(self, random_search, X_test):
        return random_search.predict(X_test) 
    
    def predict_proba(self, random_search, X_test):
        return random_search.predict_proba(X_test)    
  
    def __prepare_data(self):
        X = self.df_modelo[self.categorical_cols + self.numerical_cols]
        y = self.df_modelo[self.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        return X_train, X_test, y_train, y_test 

    def __create_pipeline(self):
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_cols),
                ('num', StandardScaler(), self.numerical_cols)
            ]
        )
        pipeline = Pipeline(steps=[
            ('preprocess', preprocessor),
            ('model', lgb.LGBMClassifier(objective="binary", random_state=26))
        ])
        return pipeline

    def __tune_model(self, pipeline, X_train, y_train):
        # Best parameters local traning: {'model__num_leaves': 65, 'model__n_estimators': 100, 'model__max_depth': 3, 'model__learning_rate': 0.1}
        param_dist = {
            'model__num_leaves': randint(20, 100),
            'model__max_depth': randint(3, 10),
            'model__learning_rate': [0.01, 0.05, 0.1],
            'model__n_estimators': [100, 300],
        }
        random_search = RandomizedSearchCV(
            estimator=pipeline,
            param_distributions=param_dist,
            n_iter=10,
            scoring='roc_auc',
            cv=3,
            verbose=2,
            random_state=26,
            n_jobs=-1
        )
        return random_search.fit(X_train, y_train)

